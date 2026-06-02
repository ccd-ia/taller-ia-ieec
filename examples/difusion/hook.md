# Hook del ejemplo de difusión

Este gancho cierra el ciclo del ejemplo: **cuando llega un estudio nuevo a la
carpeta `estudios/`, Claude Code te recuerda (o lanza) la extracción de mensajes
de difusión.** Así no tienes que acordarte de hacerlo a mano.

Es un hook de tipo `PostToolUse`: se dispara **después** de que la IA escribe un
archivo. Si el archivo cae en `estudios/`, imprime un recordatorio para correr el
skill `extraer-mensajes-difusion`.

## Configuración (`.claude/settings.json`)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '[difusion] Se guardó un estudio. Sugerencia: corre el skill extraer-mensajes-difusion para generar los borradores de hilo, boletin y mensaje a decisores.'"
          }
        ]
      }
    ]
  }
}
```

### Cómo leerlo

- **`PostToolUse`**: el evento. Ocurre justo después de usar una herramienta.
- **`matcher": "Write"`**: el filtro. Solo cuando la herramienta fue *escribir*
  un archivo.
- **`command`**: lo que se ejecuta. Aquí solo imprime un recordatorio en
  pantalla, que es lo más seguro para empezar.

## Variante: solo cuando el archivo está en `estudios/`

El ejemplo de arriba se dispara con *cualquier* escritura. Para limitarlo a la
carpeta `estudios/`, el comando puede revisar la ruta del archivo recién escrito
(Claude Code la pasa al hook) y avisar solo si corresponde. Ese filtro fino lo
puedes pedirle a Claude Code: "haz que este hook avise únicamente cuando el
archivo guardado esté dentro de examples/difusion/estudios/". La idea pedagógica
ya queda clara con la versión simple.

## De recordatorio a automático

Empezamos con un hook que **sugiere**. Cuando el equipo confíe en el flujo, el
mismo hook puede **lanzar** directamente el agente
`examples/difusion/agent.md` para que prepare los borradores en automático
(siempre dejándolos para revisión humana antes de publicar).

> Nota: los nombres de campo del `settings.json` pueden variar entre versiones de
> Claude Code. Si el hook no se dispara, pregúntale a Claude Code cómo se
> configura un hook `PostToolUse` en tu versión.
