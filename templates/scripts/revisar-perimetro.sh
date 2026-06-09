#!/usr/bin/env bash
# revisar-perimetro.sh — freno de seguridad de "dignidad de datos".
#
# Este es un hook PreToolUse de ejemplo: se ejecuta ANTES de que Claude Code
# corra un comando de shell (Bash). Revisa el comando y, si parece que va a
# SUBIR datos a internet (sacarlos del perímetro del IEEC), lo BLOQUEA.
#
# Cómo se conecta: en .claude/settings.json, un hook PreToolUse con
# "matcher": "Bash" apunta a este archivo (ver templates/settings.example.json).
#
# Cómo bloquea: si sale con código 2, Claude Code cancela la acción. Si sale con
# 0, la deja pasar.
#
# Instalación: cópialo a .claude/scripts/revisar-perimetro.sh y dale permisos:
#   chmod +x .claude/scripts/revisar-perimetro.sh

set -euo pipefail

# Claude Code envía la información de la herramienta como JSON por la entrada
# estándar. Leemos todo ese JSON en una variable.
entrada="$(cat)"

# Extraemos el texto del comando que se va a ejecutar. Usamos jq si está
# disponible (más robusto); si no, caemos a grep sobre el JSON crudo.
if command -v jq >/dev/null 2>&1; then
  comando="$(printf '%s' "$entrada" | jq -r '.tool_input.command // empty')"
else
  comando="$entrada"
fi

# Patrones que sugieren que se están sacando datos del perímetro.
patrones_peligrosos='curl .*(-T|--upload-file|-F|--data)|scp |rsync .*:|aws s3 cp .* s3://|wget .*--post-file'

if printf '%s' "$comando" | grep -Eiq "$patrones_peligrosos"; then
  # Mensaje a stderr para que la persona sepa POR QUÉ se bloqueó.
  echo "[perímetro] BLOQUEADO: el comando parece subir datos fuera del IEEC." >&2
  echo "            Revisa la regla de dignidad de datos antes de continuar." >&2
  echo "            Comando: $comando" >&2
  exit 2   # 2 = cancelar la acción
fi

exit 0     # 0 = dejar pasar
