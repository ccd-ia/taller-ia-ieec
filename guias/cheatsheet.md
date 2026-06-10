---
title: "Guía rápida de Claude Code"
description: "Una página imprimible con lo esencial del día a día para sacar el máximo provecho de Claude Code"
tags: [guia-rapida, referencia]
---

# Guía rápida de Claude Code

**Autor**: Florian BRUNIAUX | Founding Engineer [@Méthode Aristote](https://methode-aristote.fr)

**Adaptación al español para el Taller del IEEC**

---

## Comandos esenciales

| Comando | Acción |
|---------|--------|
| `/help` | Ayuda contextual |
| `/powerup` | Lecciones interactivas y animadas que enseñan las funciones de Claude Code |
| `/clear` | Reinicia la conversación |
| `/compact` | Libera context |
| `/status` | Estado de la sesión + uso de context |
| `/context` | Desglose detallado de tokens |
| `/plan` | Entra a plan mode (sin hacer cambios) |
| `/ultraplan` | Plan mode en la nube — se redacta en la nube y se revisa en el navegador (v2.1.91+) |
| `/execute` | Sale de plan mode (aplica los cambios) |
| `/model` | Cambia de modelo (sonnet/opus/opusplan) |
| `/insights` | Analítica de uso + reporte de optimización |
| `/simplify` | Detecta sobreingeniería en el código modificado y la corrige automáticamente |
| `/batch` | Refactorizaciones a gran escala con 5–30 agentes paralelos en worktrees |
| `/teleport` | Trae («teleporta») la sesión desde la web |
| `/tasks` | Monitorea tareas en segundo plano |
| `/remote-env` | Configura el entorno en la nube |
| `/remote-control` | Inicia una sesión de control remoto (Research Preview, Pro/Max) |
| `/rc` | Atajo de /remote-control |
| `/mobile` | Muestra los enlaces de descarga de la app móvil de Claude |
| `/fast` | Activa/desactiva el modo rápido (2.5x de velocidad, 6x de costo) |
| `/voice` | Activa/desactiva la entrada por voz (mantén Space para hablar, suelta para enviar) |
| `/recap` | Resumen del context de la sesión al regresar de una pausa (v2.1.108) |
| `/effort [nivel]` | Profundidad de razonamiento: low/medium/high/xhigh/max; sin argumento = control interactivo (v2.1.111) |
| `/tui [fullscreen]` | Renderizado TUI a pantalla completa, sin parpadeos (v2.1.110) |
| `/focus` | Activa/desactiva la vista de enfoque mínima, distinta de Ctrl+O (v2.1.110) |
| `/less-permission-prompts` | Revisa los transcripts y propone una lista blanca de herramientas de solo lectura (v2.1.111) |
| `/btw [pregunta]` | Pregunta lateral superpuesta — agente efímero de solo lectura, sin contaminar el historial, sin herramientas |
| `/loop [intervalo] [prompt]` | Ejecuta un prompt en repetición (ej.: `/loop 5m check the deploy`, por defecto 10m) |
| `/stats` | Gráfica de uso, modelo favorito, racha *(atajo de `/usage` desde v2.1.118)* |
| `/usage` | Uso de tokens + costo por modelo (v2.1.118) |
| `/ultrareview` | Revisión de código en la nube con múltiples agentes (v2.1.114) |
| `/goal [condición]` | Modo autónomo de varios turnos: Claude trabaja hasta cumplir la condición; una vista en vivo muestra tiempo transcurrido/turnos/tokens (v2.1.139) |
| `/scroll-speed` | Ajusta la velocidad de desplazamiento de la rueda del ratón con vista previa interactiva en vivo (v2.1.139) |
| `/rename [nombre]` | Nombra o renombra la sesión actual |
| `/copy` | Selector interactivo para copiar un bloque de código o la respuesta completa |
| `/debug` | Diagnóstico sistemático de problemas |
| `/exit` | Salir (o Ctrl+D) |

---

## Atajos de teclado

| Atajo | Acción |
|----------|--------|
| `Shift+Tab` | Rota entre los modos de permisos |
| `Esc` × 2 | Rebobina (deshace) |
| `Ctrl+C` | Interrumpe |
| `Ctrl+R` | Busca en el historial de comandos |
| `Ctrl+L` | Limpia la pantalla (conserva el context) |
| `Tab` | Autocompletar |
| `Shift+Enter` | Salto de línea |
| `Ctrl+B` | Tareas en segundo plano |
| `Ctrl+F` | Detiene todos los agentes en segundo plano (doble pulsación) |
| `Alt+T` | Activa/desactiva el pensamiento (thinking) |
| `Space` (mantener) | Entrada por voz (requiere `/voice` activado) |
| `Ctrl+D` | Salir |

---

## Referencias a archivos

```
@path/to/file.ts    → Referencia un archivo
@agent-name         → Llama a un agent
!shell-command      → Ejecuta un comando de shell
```

| IDE | Atajo |
|-----|----------|
| VS Code | `Alt+K` |
| JetBrains | `Cmd+Option+K` |

---

## Funciones poco conocidas (¡pero oficiales!)

| Función | Desde | Qué hace |
|---------|-------|--------------|
| **Tasks API** | v2.1.16 | Listas de tareas persistentes con dependencias |
| **Background Agents** | v2.0.60 | Sub-agentes trabajan mientras tú programas |
| **Agent Teams** | v2.1.32 | Coordinación de múltiples agents (TeamCreate/SendMessage) |
| **Auto-Memories** | v2.1.32 | Captura automática de context entre sesiones |
| **Session Forking** | v2.1.19 | Rebobina + crea una línea de tiempo paralela |
| **LSP Tool** | v2.0.74 | Navegación tipo IDE: símbolos, tipos, referencias. ~50ms frente a 45s con grep. 11 lenguajes |
| **Voice Mode** | v2.1.x | Entrada por voz nativa, transcripción gratuita, sin impacto en los límites de uso |
| **Remote Control** | v2.1.51 | Controla la sesión local desde el teléfono/navegador (Research Preview, Pro/Max) |
| **`/loop`** | v2.1.71 | Programador recurrente con alcance de sesión: `/loop 5m check the deploy` (se detiene al terminar la sesión). Mínimo 1 min, máximo 50 tareas/sesión |
| **`/goal`** | v2.1.139 | Bucle de finalización autónoma: defines una condición y Claude trabaja a lo largo de varios turnos hasta que un evaluador independiente (Haiku) verifica que se cumplió. Una vista en vivo muestra el tiempo transcurrido, los turnos y los tokens. Fórmula de tres elementos: estado final medible + mecanismo de verificación + restricciones. |
| **Cloud Scheduled Tasks** | 2026 | Programación con la máquina apagada vía `/schedule` o `claude.ai/code/scheduled`. Corre en la infraestructura de Anthropic, clona el repo en limpio en cada ejecución, intervalo mínimo de 1h. Pro/Max/Team/Enterprise |
| **Desktop Scheduled Tasks** | 2026 | Programación en la máquina local vía la app de escritorio. Mínimo 1 min, acceso completo a los archivos locales, sin necesidad de una sesión |
| **Skill Evals** | mar. 2026 | Dos tipos de skill: Capability Uplift (cubre un hueco del modelo, se desvanece) / Encoded Preference (codifica un flujo de trabajo, permanece). Modo Benchmark, pruebas A/B, Trigger Tuning. |
| **Output Styles** | v2.1.108 | `/config` → "Preferred output style": **Default** (conciso), **Explanatory** (agrega el porqué del diseño), **Learning** (programación en pareja, marcadores `TODO(human)`). Estilos personalizados vía `.claude/styles/`. |

**Activar LSP**: agrega a `~/.claude/settings.json` → `{ "env": { "ENABLE_LSP_TOOL": "1" } }` (requiere tener instalado el servidor LSP de tu lenguaje: `tsserver`, `pylsp`, `gopls`, `rust-analyzer`, `sourcekit-lsp`...)

**Consejo**: no son «secretos» — están en el [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). ¡Léelo!

---

## Modos de permisos

| Modo | Edición | Ejecución |
|------|---------|-----------|
| Default | Pregunta | Pregunta |
| acceptEdits | Automática | Pregunta |
| Plan Mode | ❌ | ❌ |
| auto | Decide el clasificador | Decide el clasificador |
| dontAsk | Solo si está en las reglas allow | Solo si está en las reglas allow |
| bypassPermissions | Automática | Automática (solo CI/CD) |

**Shift+Tab** para cambiar de modo

---

## Memoria y configuración (3 niveles)

Claude Code carga la memoria desde tres niveles. Regla de oro: **lo más específico gana (local > project > global)**.

| Nivel | Ubicación | Alcance | Git |
|-------|-----------|---------|-----|
| **Global** | `~/.claude/CLAUDE.md` | Tú, en todos los proyectos | ❌ (personal) |
| **Project** | `/proyecto/CLAUDE.md` | Todo el equipo del proyecto | ✅ (se versiona en git) |
| **Local** | `/proyecto/.claude/` | Tú, solo en este proyecto (overrides personales) | ❌ (gitignored) |

**Prioridad**: lo Local sobrescribe lo de Project, y lo de Project sobrescribe lo Global. Cuanto más cerca del archivo, más manda.

| Archivo | Dónde | Uso |
|------|-------|-------|
| `CLAUDE.md` | `~/.claude/` (Win: `%USERPROFILE%\.claude\`) | Memoria global (tus preferencias para todos los proyectos) |
| `CLAUDE.md` | Raíz del proyecto | Memoria del equipo (instrucciones del proyecto, se versiona) |
| `settings.json` | `.claude/` | Configuración del equipo (hooks) |
| `settings.local.json` | `.claude/` | Tus overrides personales de configuración (gitignored) |

---

## Estructura de la carpeta `.claude/`

```
.claude/
├── CLAUDE.md           # Memoria local (gitignored)
├── settings.json       # Hooks (se versiona)
├── settings.local.json # Permisos (no se versiona)
├── agents/             # Agents personalizados
├── hooks/              # Scripts de eventos
├── rules/              # Reglas que se cargan automáticamente
└── skills/             # Slash commands + módulos de conocimiento (unificados)
```

---

## Flujo de trabajo típico

```
1. Inicia la sesión    → claude
2. Revisa el context   → /status
3. Plan mode           → Shift+Tab × 2 (para tareas complejas)
4. Describe la tarea   → Prompt claro y específico
5. Revisa los cambios  → ¡Lee siempre el diff!
6. Acepta/Rechaza      → y/n
7. Verifica            → Corre las pruebas
8. Commit              → Cuando la tarea esté completa
9. /compact            → Cuando el context pase de 70%
```

---

## Gestión del context (CRÍTICO)

### Statusline

```
Model: Sonnet | Ctx: 89.5k | Cost: $2.11 | Ctx(u): 56.0%
```
**Vigila `Ctx(u):`** → >70% = `/compact`, >85% = `/clear`

**Statusline del taller ([templates/statusline.py](../templates/statusline.py)):** usa la que viene en este repo. Cópiala a tu carpeta personal y apúntale desde `~/.claude/settings.json`:
```bash
cp templates/statusline.py ~/.claude/statusline.py
chmod +x ~/.claude/statusline.py
```
```json
{ "statusLine": { "type": "command", "command": "python3 ~/.claude/statusline.py", "padding": 0 } }
```
> Solo usa la librería estándar de Python; no instala nada (no necesitas `uv`). Si prefieres `uv`, puedes poner `"command": "uv run ~/.claude/statusline.py"` en su lugar.

*Alternativa de terceros: existe [ccstatusline](https://github.com/sirmalloc/ccstatusline) (`npx -y ccstatusline@latest`), pero en el taller usamos la nuestra.*

### Umbrales de context

| Context % | Estado | Acción |
|-----------|--------|--------|
| 0-50% | Verde | Trabaja con libertad |
| 50-70% | Amarillo | Sé selectivo |
| 70-90% | Naranja | `/compact` ya |
| 90%+ | Rojo | `/clear` obligatorio |

### Acciones según el síntoma

| Señal | Acción |
|------|--------|
| Respuestas cortas | `/compact` |
| Olvida cosas seguido | `/clear` |
| Más de 70% de context | `/compact` |
| Tarea completa | `/clear` |

### Comandos de recuperación de context

| Comando | Uso |
|---------|-------|
| `/compact` | Resume y libera context |
| `/clear` | Empieza de cero |
| `/rewind` | Deshace cambios recientes |
| `claude -c` | Reanuda la última sesión (flag de CLI) |
| `claude -r <id>` | Reanuda una sesión específica (flag de CLI) |

---

## Bajo el capó (datos rápidos)

| Concepto | Punto clave |
|---------|-----------|
| **Master Loop** | Un simple `while(tool_call)` — sin DAGs, sin clasificadores |
| **Tools** | 8 esenciales: Bash, Read, Edit, Write, Grep, Glob, Agent, TodoWrite ([referencia completa de 40 tools](./core/tools-reference.md)) |
| **Context** | ~200K tokens, se compacta automáticamente entre 75-92% |
| **Sub-agents** | Context aislado, profundidad máxima = 1 |
| **Filosofía** | «Menos andamiaje, más modelo» — confía en el razonamiento de Claude |


---

## Plan mode y pensamiento (thinking)

| Función | Activación | Uso |
|---------|------------|-----|
| **Plan Mode** | `Shift+Tab × 2` o `/plan` | Explora sin modificar |
| **OpusPlan** | `/model opusplan` | Opus para planear, Sonnet para ejecutar |
| **Ultraplan** | `/ultraplan <prompt>` | Planeación en la nube, revisión en el navegador, la terminal queda libre (v2.1.91+, requiere GitHub) |

> **Opus 4.8** (v2.1.114+): el effort por defecto en Claude Code = **xhigh** (en todos los planes). El nuevo nivel `xhigh` queda entre `high` y `max` — control más fino de razonamiento/latencia. Usa `ultrathink` para forzar el effort máximo en el siguiente turno.

| Control | Acción | Persistencia |
|---------|--------|-------------|
| **Alt+T** | Activa/desactiva el pensamiento | Sesión |
| **/config** | Activa/desactiva de forma global | Permanente |
| **Control deslizante de `/model`** | Flechas izquierda/derecha: `low\|medium\|high\|xhigh` | Sesión |
| **`CLAUDE_CODE_EFFORT_LEVEL`** | Variable de entorno: `low\|medium\|high\|xhigh\|max` | Sesión de shell |
| **Ajuste `effortLevel`** | En settings.json: `low\|medium\|high\|xhigh\|max` | Permanente |
| **`effort` en el frontmatter de un skill** (v2.1.80+) | Override por skill: `low\|medium\|high\|xhigh` | Por invocación |

**Consejo de costo**: para tareas simples, Alt+T para desactivar el pensamiento → más rápido y más barato.

**Effort por skill** — agrega `effort: low` a los skills mecánicos (commit, sync, scaffold) y `effort: high` a los analíticos (security-audit, architecture-review). Sobrescribe el ajuste de la sesión automáticamente.

**Flujo de OpusPlan**: `/model opusplan` → `Shift+Tab × 2` (planea con Opus) → `Shift+Tab` (ejecuta con Sonnet)

**Flujo de Ultraplan**: `/ultraplan <tarea>` → terminal libre mientras la nube redacta → revisa en línea en el navegador → aprueba → ejecuta en la web (PR) o «teleporta» de regreso a la terminal

**Requerido para**: funciones de más de 3 archivos, arquitectura, depuración compleja

### Selección rápida de modelo

| Tarea | Modelo | Effort |
|------|-------|--------|
| Renombrar, boilerplate, generar pruebas | Haiku | low |
| Desarrollo de funciones, depurar, refactorizar | Sonnet | medium–high |
| Arquitectura, auditoría de seguridad | Opus | high–max |

### Cambio dinámico de modelo (a mitad de sesión)

**Patrón**: empieza con Sonnet (velocidad) → cambia a Opus (complejidad) → de vuelta a Sonnet

**Flujo**:
```bash
# Inicio de sesión (Sonnet por defecto)
claude

# Aparece una función compleja
> "Implement OAuth2 flow with PKCE"
/model opus                    # Cambia a razonamiento profundo

# Función terminada, de vuelta a lo rutinario
/model sonnet                  # Optimiza velocidad + costo
```

**Buenas prácticas**:
- ✅ Cambia **en los límites entre tareas**, no a mitad de una tarea
- ✅ Usa Opus para: decisiones de arquitectura, depuración compleja, código crítico de seguridad
- ✅ Usa Sonnet para: ediciones rutinarias, refactorizaciones, escritura de pruebas
- ✅ Usa Haiku para: correcciones simples, erratas, validaciones
- ❌ No cambies a mitad de una implementación (se pierde context)

**Impacto en el costo**:
| Modelo | Entrada | Salida | Caso de uso |
|-------|--------|--------|----------|
| Opus 4.8 (`claude-opus-4-8`, 1M ctx) | $5.00/MTok | $25.00/MTok | Razonamiento complejo (10-20% de las tareas) |
| Sonnet 4.6 (`claude-sonnet-4-6`, 1M ctx, 64K out) | $3.00/MTok | $15.00/MTok | La mayoría del desarrollo (70-80% de las tareas) |
| Haiku 4.5 (`claude-haiku-4-5`, 200K ctx, 64K out) | $1.00/MTok | $5.00/MTok | Validaciones simples (5-10% de las tareas) |

**El cambio dinámico** optimiza el costo manteniendo la calidad en las tareas complejas.

**Fuente**: [Flujo de trabajo de Gur Sannikov en embedded engineering](https://www.linkedin.com/posts/gursannikov_claudecode-embeddedengineering-aiagents-activity-7423851983331328001-DrFb)

---

## Servidores MCP

| Servidor | Propósito |
|--------|---------|
| **grepai** | Búsqueda semántica + análisis del grafo de llamadas |
| **Context7** | Documentación de librerías |
| **Sequential** | Razonamiento estructurado |
| **Playwright** | Automatización de navegador |
| **Postgres** | Consultas a la base de datos |

Revisa el estado: `/mcp`

---

## Cómo crear componentes personalizados

### Agent (`.claude/agents/my-agent.md`)
```yaml
---
name: my-agent
description: Use when [trigger]
model: sonnet
tools: Read, Write, Edit, Bash
---
# Instructions here
```
> Plantilla completa: [../templates/agent.md](../templates/agent.md)

### Skill — invocable por el usuario (`.claude/skills/my-command/SKILL.md`)
```markdown
---
description: Brief description
argument-hint: "<required_arg> [--flag]"
disable-model-invocation: true
---
# Command Name
Instructions for what to do...
$ARGUMENTS[0] $ARGUMENTS[1] (or $0 $1) - user args
```
> Plantilla completa: [../templates/skill.md](../templates/skill.md)

### Command (slash command, `.claude/skills/{categoría}/{nombre}/SKILL.md`)
```markdown
---
description: <qué hace el comando>
argument-hint: <pista de argumentos>
---
## Purpose
## Process
## Arguments
## Examples
```
> Plantilla completa: [../templates/command.md](../templates/command.md)

### Hook (macOS/Linux: `.sh` | Windows: `.ps1`)

**Bash** (macOS/Linux):
```bash
#!/bin/bash
INPUT=$(cat)
# Process JSON input
exit 0  # 0=continue, 2=block
```

**PowerShell** (Windows):
```powershell
$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
# Process JSON input
exit 0  # 0=continue, 2=block
```
> Plantilla completa: [../templates/hook.md](../templates/hook.md) · registro en [../templates/settings.example.json](../templates/settings.example.json) · script de ejemplo [../templates/scripts/revisar-perimetro.sh](../templates/scripts/revisar-perimetro.sh)

---

## Antipatrones

| ❌ No hagas | ✅ Haz |
|----------|-------|
| Prompts vagos | Especifica archivo + línea con @referencias |
| Aceptar sin leer | Lee cada diff |
| Ignorar las advertencias | Usa `/compact` al 70% |
| Saltarte los permisos | Nunca en producción |
| Solo restricciones negativas | Ofrece alternativas |

---

## Fórmula para prompts: CRAFT

El andamiaje **CRAFT** son las cinco piezas que casi siempre mejoran el resultado. No siempre necesitas las cinco, pero entre más completes, mejor sale. (Plantilla completa: [templates/craft-prompt.md](../templates/craft-prompt.md))

| Letra | Pieza | Pregunta que responde |
|-------|-------|------------------------|
| **C** | Contexto | ¿Qué situación, datos o antecedentes necesita conocer la IA? |
| **R** | Rol | ¿Desde qué perspectiva o expertise debe responder? |
| **A** | Acción | ¿Qué quiero exactamente que haga? (un verbo claro) |
| **F** | Formato | ¿Cómo quiero el resultado? (tabla, viñetas, longitud) |
| **T** | Tono | ¿Con qué registro? (formal, divulgativo, para autoridades) |

**Ejemplo:**
```
CONTEXTO: Tengo demo-data/resultados-evaluacion.csv con promedios de matemáticas
y español por estado, más n_estudiantes. Es un corte estatal de una aplicación.
ROL: Actúa como analista de evaluación educativa del IEEC, sin sobreinterpretar
diferencias pequeñas entre estados.
ACCIÓN: Identifica los 3 estados con el promedio más bajo en matemáticas y los 3
más altos; reporta también su promedio en español y su n_estudiantes.
FORMATO: Tabla en Markdown (estado, promedio_matematicas, promedio_espanol,
n_estudiantes, nota) y debajo dos viñetas con los hallazgos principales.
TONO: Profesional y basado en evidencia; distingue el dato de la interpretación.
```

> **Fórmula rápida (alternativa breve)** — para tareas chicas basta con cuatro líneas: **QUÉ** (entregable concreto) · **DÓNDE** (rutas de archivos) · **CÓMO** (restricciones, enfoque) · **VERIFICAR** (criterios de éxito).

---

## Referencia rápida de flags de CLI

| Flag | Uso |
|------|-------|
| `-p "query"` | Modo no interactivo (CI/CD) |
| `-c` / `--continue` | Continúa la última sesión |
| `-r` / `--resume <id>` | Reanuda una sesión específica |
| `--teleport` | Trae («teleporta») la sesión desde la web |
| `remote-control` | Subcomando: inicia una sesión de control remoto |
| `--model sonnet` | Cambia de modelo |
| `--add-dir ../lib` | Permite acceso fuera del directorio actual |
| `--permission-mode plan` | Plan mode |
| `--tools "Tool1,Tool2"` | Habilita herramientas específicas para la sesión |
| `--max-budget-usd 5.00` | Límite máximo de gasto de la API (modo print) |
| `--system-prompt "..."` | Anexa un system prompt personalizado |
| `--worktree` / `-w` | Corre en un worktree de git aislado |
| `--dangerously-skip-permissions` | Auto-acepta (úsalo con cuidado) |
| `--debug` | Salida de depuración |
| `--allowedTools "Edit,Read"` | Lista blanca de herramientas |

> Referencia completa de la CLI (~45 flags): consulta [cli-reference en code.claude.com](https://docs.anthropic.com/en/docs/claude-code/cli-reference)

## Subcomandos clave de la CLI

| Comando | Descripción |
|---------|-------------|
| `claude project purge [path]` | Borra todo el estado de Claude Code de un proyecto (transcripts, tareas, configuración). `--dry-run` para previsualizar. (v2.1.126) |
| `claude ultrareview [target]` | Revisión de código en la nube no interactiva para CI. Salida `--json`. Termina con 0/1. (v2.1.120) |
| `claude plugin prune` | Elimina dependencias de plugins huérfanas instaladas automáticamente. (v2.1.121) |
| `claude plugin details <name>` | Muestra el inventario del plugin y la estimación de costo en tokens. (v2.1.139) |
| `claude --plugin-url <url>` | Carga un plugin `.zip` desde una URL para esta sesión. (v2.1.129) |

---

## Comandos de depuración

```bash
claude --version     # Versión
claude update        # Revisa/instala actualizaciones
claude doctor        # Diagnóstico
claude --debug       # Modo detallado
claude --mcp-debug   # Depura los MCPs
/mcp                 # Estado de MCP (dentro de Claude)
```

---

## Modo CI/CD (sin interfaz, headless)

```bash
# Ejecución no interactiva
claude -p "analyze this file" src/api.ts

# Salida en JSON
claude -p "review" --output-format json

# Modelo económico
claude -p "lint" --model haiku

# Con auto-aceptación
claude -p "fix typos" --dangerously-skip-permissions
```

---

## Control remoto — Acceso móvil (v2.1.51+, Research Preview)

> **Solo Pro/Max** — no disponible en Team, Enterprise ni con claves de API

```bash
# Inicia desde la terminal (sesión nueva)
claude remote-control

# O desde dentro de una sesión activa:
/rc        # (o /remote-control)
```

**Conéctate desde teléfono/tableta/navegador:**
1. Escanea el **código QR** (presiona la barra espaciadora tras iniciar)
2. O abre la **URL de la sesión** en el navegador / app móvil de Claude
3. O: `/mobile` → muestra los enlaces de App Store + Play Store

| ⚠️ Limitación conocida | Detalle |
|--------------------|--------|
| 1 sesión a la vez | Solo una sesión remota activa |
| Slash commands rotos | `/new`, `/compact` = texto plano en remoto → úsalos desde la terminal local |
| La terminal debe quedar abierta | Cerrar la terminal local termina la sesión |
| Timeout de red | ~10 min de desconexión → la sesión expira |

**Avanzado: multi-sesión con tmux** (esquiva el límite de 1 sesión)
```bash
tmux new-session -s dev
# Cada panel = su propia sesión de claude
# Corre /rc en el panel que quieras controlar de forma remota
```

**Auto-activación:** `/config` → activa "Remote Control: auto-enable"

**Documentación completa**: [§9.22 Control remoto](ultimate-guide.md#922-remote-control-mobile-access) | [Notas de seguridad](security/security-hardening.md#remote-control-security)

---

## Gestión de tareas (v2.1.16+)

**Dos sistemas disponibles:**

| Sistema | Cuándo usarlo | Persistencia |
|--------|-------------|-------------|
| **Tasks API** (v2.1.16+) | Proyectos de varias sesiones, dependencias | ✅ Disco (`~/.claude/tasks/`) |

### Comandos de la Tasks API

```bash
# Habilita la persistencia entre sesiones
export CLAUDE_CODE_TASK_LIST_ID="project-name"
claude

# Dentro de Claude: crea la jerarquía de tareas
> "Create tasks for auth system with dependencies"

# Reanuda más tarde (sesión nueva)
export CLAUDE_CODE_TASK_LIST_ID="project-name"
claude
> "TaskList to see current state"
```

**Capacidades clave:**
- 📁 **Persistente**: sobrevive al fin de la sesión y a la compactación del context
- 🔗 **Dependencias**: la Tarea A bloquea la Tarea B
- 🔄 **Multi-sesión**: difunde el estado a varias terminales
- 📊 **Estado**: pending → in_progress → completed/failed

**⚠️ Limitación**: TaskList solo muestra `id`, `subject`, `status`, `blockedBy`.
Para `description`/`metadata` → usa `TaskGet(taskId)` por tarea.

**Consejo**: guarda la información clave en `subject` para revisarla de un vistazo.

**Flag de migración** (v2.1.19+):
```bash
# Vuelve al sistema antiguo TodoWrite
CLAUDE_CODE_ENABLE_TASKS=false claude
```

**→ Flujo completo**: [guide/workflows/task-management.md](workflows/task-management.md)

---

## Las reglas de oro

1. **Revisa siempre los diffs** antes de aceptar
2. **Usa `/compact`** antes de que el context llegue a un punto crítico (>70%)
3. **Sé específico** en tus peticiones — usa **CRAFT** (Contexto, Rol, Acción, Formato, Tono)
4. **Plan mode primero** para tareas complejas o riesgosas
5. **Crea un CLAUDE.md** para cada proyecto
6. **Haz commits con frecuencia** después de cada tarea completada
7. **Sabe qué se envía** — prompts, archivos, resultados de MCP → Anthropic ([excluirse del entrenamiento](https://claude.ai/settings/data-privacy-controls))

---

## Árbol de decisión rápido

```
Tarea simple      → Solo pídele a Claude
Tarea compleja    → Usa la Tasks API para planear primero
Cambio riesgoso   → Plan mode primero
Tarea repetitiva  → Crea un agent o un comando
Context lleno     → /compact o /clear
Análisis profundo → Usa Opus (pensamiento activado por defecto)
```

---

## Solución rápida a problemas comunes

| Problema                 | Solución                                                               |
|-------------------------|------------------------------------------------------------------------|
| "Command not found"     | Revisa el PATH, reinstala: `curl -fsSL https://claude.ai/install.sh \| sh` |
| Context muy alto (>70%) | `/compact` de inmediato                                                |
| Respuestas lentas        | `/compact` o `/clear`                                                  |
| MCP no funciona          | `claude mcp list`, revisa la configuración                             |
| Permiso denegado         | Revisa `settings.local.json`                                           |
| Hook bloqueando          | Revisa el código de salida del hook, repasa la lógica                  |

**Script de chequeo de salud** (guárdalo y córrelo):
```bash
# macOS/Linux
which claude && claude doctor && claude mcp list

# Windows PowerShell
where.exe claude; claude doctor; claude mcp list
```

---

## Optimización de costos

| Modelo   | Úsalo para                     | Costo |
|----------|--------------------------------|------|
| Haiku    | Correcciones simples, revisiones | $    |
| Sonnet   | La mayoría del desarrollo        | $$   |
| Opus     | Arquitectura, bugs complejos     | $$$  |
| OpusPlan | Planear (Opus) + Ejecutar (Sonnet) | $$   |

**Consejo**: usa `--add-dir` para dar acceso a las herramientas a directorios fuera de tu directorio de trabajo actual

---


## Recursos

- **Documentación oficial**: [docs.anthropic.com/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- **Guía avanzada**: [Claudelog.com](https://claudelog.com/) — consejos y patrones

---

## Notas

- **Versiones de Claude Code**: la guía original rastrea versiones recientes (hasta ~v2.1.139 en la columna «Desde»). El número de versión del encabezado (3.41.1, mayo de 2026) proviene del documento fuente y no se modificó; consulta `claude --version` para conocer tu versión instalada y el [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) para lo más reciente.
- **Precios de los modelos**: las cifras de costo ($/MTok) y los nombres de versión de los modelos (Opus 4.8 `claude-opus-4-8`, Sonnet 4.6 `claude-sonnet-4-6`, Haiku 4.5 `claude-haiku-4-5`) se verificaron vigentes (junio de 2026): Opus 4.8 $5.00/$25.00 (1M ctx), Sonnet 4.6 $3.00/$15.00 (1M ctx, 64K out), Haiku 4.5 $1.00/$5.00 (200K ctx, 64K out). Opus 4.7 sigue existiendo, pero 4.8 es el Opus por defecto. Aun así, confirma los precios vigentes en la documentación de Anthropic antes de presupuestar.

---


*Última actualización: junio de 2026*
