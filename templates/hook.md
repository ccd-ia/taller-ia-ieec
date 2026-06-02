# Hooks (ganchos) en Claude Code

Un **hook** ("gancho") es una acción que se dispara **automáticamente** en cierto
momento del trabajo de Claude Code. No lo ejecuta la IA: lo ejecuta el programa,
siempre, sin que tengas que pedirlo. Sirven para poner reglas y automatismos.

Piensa en un hook como un "cuando pase X, haz Y" que se cumple sin falta.

---

## ¿Cuándo se disparan? (eventos)

Los eventos más útiles para nosotros:

| Evento | Cuándo se dispara | Para qué sirve (ejemplos) |
|--------|-------------------|----------------------------|
| `PreToolUse` | **Antes** de que la IA use una herramienta (leer/escribir un archivo, correr un comando). | Bloquear acciones peligrosas; impedir que se toquen datos sensibles; pedir confirmación. |
| `PostToolUse` | **Después** de que la IA usó una herramienta. | Formatear un archivo recién guardado; registrar qué se cambió; validar el resultado. |
| `Stop` | Cuando la IA **termina** de responder. | Recordar guardar; lanzar una revisión final; avisar que terminó. |
| `UserPromptSubmit` | Cuando **tú** envías un mensaje. | Inyectar contexto automático; registrar la consulta. |
| `SessionStart` | Al **abrir** una sesión. | Cargar contexto, recordar reglas del equipo. |

> Para el taller, los dos que más usaremos son `PostToolUse` (reaccionar a un
> archivo que acaba de aparecer o cambiar) y `PreToolUse` (poner un freno de
> seguridad).

---

## Dónde se configuran

Los hooks viven en un archivo `settings.json` dentro de `.claude/`. Cada hook
asocia un **evento** + un **filtro** (qué herramienta o archivo) + un **comando**
que se ejecuta.

### Ejemplo: avisar cuando se guarda un archivo en `estudios/`

Este hook se dispara **después** de que la IA escribe un archivo y, si el archivo
está en la carpeta `estudios/`, imprime un aviso. Es el gancho del ejemplo de
difusión (ver `examples/difusion/hook.md`).

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '[hook] Llegó o cambió un estudio. Sugerencia: corre el skill extraer-mensajes-difusion.'"
          }
        ]
      }
    ]
  }
}
```

Cómo leer este bloque:

- `"PostToolUse"` → el evento: ocurre **después** de usar una herramienta.
- `"matcher": "Write"` → el filtro: solo cuando la herramienta fue **escribir**
  un archivo.
- `"command"` → lo que se ejecuta: aquí solo imprime un recordatorio. Podría ser
  cualquier comando (formatear, validar, registrar en una bitácora).

### Ejemplo: freno de seguridad (no salir del perímetro)

Un `PreToolUse` puede revisar lo que la IA está a punto de hacer y detenerlo.
Aquí la idea, en lenguaje simple: **antes** de ejecutar un comando, revisa si
intenta subir archivos a internet; si es así, bloquéalo y pide revisión humana.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/Users/<tu-usuario>/taller-ia-ieec/.claude/scripts/revisar-perimetro.sh"
          }
        ]
      }
    ]
  }
}
```

El script `revisar-perimetro.sh` lo escribiríamos para inspeccionar el comando y
**salir con error** (lo que cancela la acción) si detecta algo como `curl
--upload` o envíos de datos sensibles. Este es el patrón de "dignidad de los
datos" hecho automático.

---

## Buenas prácticas

- **Empieza simple.** Un hook que solo imprime un recordatorio (como el primero)
  ya es útil y no rompe nada.
- **Los hooks que bloquean deben ser claros.** Si un `PreToolUse` cancela algo,
  el mensaje debe explicar por qué, para que la persona sepa qué hacer.
- **No abuses.** Demasiados hooks vuelven lento e impredecible el trabajo. Pon
  solo los que correspondan a una regla real del equipo.
- **Combínalos con skills y agentes.** El patrón completo es: un **hook** detecta
  el evento → sugiere o lanza un **skill** → un **agente** orquesta todo. Ver
  `templates/agent.md` y el ejemplo en `examples/difusion/`.

> Nota: la ruta exacta y los nombres de campo del `settings.json` pueden variar
> entre versiones de Claude Code. Si un hook no se dispara, revisa la
> documentación de tu versión con `claude --help` o pregúntale a Claude Code
> "¿cómo configuro un hook PostToolUse en esta versión?".
