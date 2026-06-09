#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# ///
"""Claude Code statusline — single-line format with context, cost, git, and lines."""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        print("Claude Code")
        return

    # --- ANSI codes ---
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    WHITE = "\033[97m"

    # --- Parse fields ---
    model_id = _get(data, "model.id", "unknown")
    model_display = _get(data, "model.display_name", "Claude")
    context_size = int(_get(data, "context_window.context_window_size", 200000))
    usage = _get(data, "context_window.current_usage", None)
    total_duration_ms = int(_get(data, "cost.total_duration_ms", 0))
    lines_added = int(_get(data, "cost.total_lines_added", 0))
    lines_removed = int(_get(data, "cost.total_lines_removed", 0))
    total_cost = _get(data, "cost.total_cost_usd", None)
    output_style = _get(data, "output_style.name", None)
    agent_name = _get(data, "agent.name", None)

    # Project name from launch directory (stays constant during session)
    project_dir = _get(data, "workspace.project_dir", os.getcwd())
    project_name = os.path.basename(project_dir) if project_dir else "~"

    # Model version from id (e.g. "claude-opus-4-6-20251101" -> "4.6")
    model_version = ""
    m = re.search(r"(\d+)-(\d+)", model_id)
    if m:
        model_version = f"{m.group(1)}.{m.group(2)}"

    # Auto-detect Max plan from context window size (1M+ = Max)
    is_max_plan = context_size >= 1_000_000

    # Auto-compact threshold
    compact_threshold = int(os.environ.get("CLAUDE_AUTOCOMPACT_PCT_OVERRIDE", "80"))

    # --- Context usage ---
    if usage and isinstance(usage, dict):
        input_tokens = int(usage.get("input_tokens", 0))
        cache_creation = int(usage.get("cache_creation_input_tokens", 0))
        cache_read = int(usage.get("cache_read_input_tokens", 0))

        current_tokens = input_tokens + cache_creation + cache_read
        context_percent = current_tokens * 100 // context_size if context_size else 0
        until_compact = max(0, compact_threshold - context_percent)

    else:
        current_tokens = 0
        context_percent = 0
        until_compact = compact_threshold

    # --- Helpers ---
    def fmt_tokens(n: int) -> str:
        if n >= 1_000_000:
            return f"{n // 1_000_000}M"
        if n >= 1000:
            return f"{n // 1000}k"
        return str(n)

    def fmt_duration(ms: int) -> str:
        s = ms // 1000
        m = s // 60
        h = m // 60
        if h > 0:
            return f"{h}h{m % 60}m"
        if m > 0:
            return f"{m}m{s % 60}s"
        return f"{s}s"

    def progress_bar(pct: int, width: int = 10) -> str:
        filled = pct * width // 100
        return "█" * filled + "░" * (width - filled)

    # Context color
    if context_percent < 50:
        ctx_color = GREEN
    elif context_percent < 80:
        ctx_color = YELLOW
    else:
        ctx_color = RED

    # Until-compact color
    if until_compact > 20:
        compact_color = GREEN
    elif until_compact > 5:
        compact_color = YELLOW
    else:
        compact_color = RED

    # --- Model label ---
    if model_version and model_version not in model_display:
        model_label = f"{model_display} {model_version}"
    else:
        model_label = model_display

    # --- Single line: model | progress | context | project [branch] | lines | duration | cost/Max ---
    parts = []
    parts.append(f"{BOLD}{CYAN}{model_label}{RESET}")
    parts.append(
        f"{ctx_color}{progress_bar(context_percent)} {context_percent}%{RESET}"
    )
    parts.append(f"{compact_color}{until_compact}% left{RESET}")
    parts.append(f"{DIM}{fmt_tokens(current_tokens)}/{fmt_tokens(context_size)}{RESET}")

    # Project name + git branch as a single segment: "project [branch*]"
    git_info = _git_info()
    if git_info:
        parts.append(f"{BLUE}{project_name}{RESET} {MAGENTA}[{git_info}]{RESET}")
    else:
        parts.append(f"{BLUE}{project_name}{RESET}")

    # Lines
    parts.append(f"{GREEN}+{lines_added}{RESET}/{RED}-{lines_removed}{RESET}")

    # Duration
    parts.append(f"{DIM}{fmt_duration(total_duration_ms)}{RESET}")

    # Cost or Max label
    if is_max_plan:
        parts.append(f"{BOLD}{MAGENTA}Max{RESET}")
    elif total_cost is not None:
        try:
            cost_val = float(total_cost)
            parts.append(f"{BOLD}{WHITE}${cost_val:.2f}{RESET}")
        except (ValueError, TypeError):
            pass

    # Output style
    if output_style:
        parts.append(f"{BOLD}{YELLOW}[{output_style}]{RESET}")

    # Agent name
    if agent_name:
        parts.append(f"{BOLD}{CYAN}[{agent_name}]{RESET}")

    sep = f" {DIM}|{RESET} "
    print(sep.join(parts))


def _get(d: dict, path: str, default=None):
    """Safely navigate nested dict with dot-separated path."""
    keys = path.split(".")
    current = d
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return default
    return current if current is not None else default


def shorten_path(path, max_length=20):
    """Shorten a path for display."""
    if not path:
        return "~"

    # Replace home directory with ~
    home = str(Path.home())
    if path.startswith(home):
        path = "~" + path[len(home) :]

    # If still too long, show only last parts
    if len(path) > max_length:
        parts = path.split(os.sep)
        if len(parts) > 2:
            # Show first and last parts
            return f"{parts[0]}/.../{parts[-1]}"

    return path


def _git_info() -> str:
    """Get git branch + dirty indicator."""
    try:
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        if branch.returncode != 0 or not branch.stdout.strip():
            return ""
        name = branch.stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        if dirty.stdout.strip():
            return f"{name}*"
        return name
    except Exception:
        return ""


if __name__ == "__main__":
    main()
