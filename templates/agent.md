# Plantilla de subagente (agent)

Un **subagente** (o simplemente "agente") es un asistente especializado al que le
das un encargo acotado, sus propias herramientas y sus propias instrucciones.
Mientras que un **skill** es *un procedimiento* y un **hook** es *un disparador
automático*, un **agente** es *quien orquesta*: recibe una tarea, decide qué
skills usar y entrega un resultado.

El patrón completo que enseñamos en el taller:

```
  [hook]  detecta que pasó algo
     │
     ▼
  [agente]  toma el encargo y lo coordina
     │
     ▼
  [skill]  ejecuta el procedimiento concreto
     │
     ▼
  resultado para revisión humana
```

Los agentes se definen en archivos dentro de `.claude/agents/<nombre>.md`. La
parte de arriba (frontmatter) declara su nombre, cuándo usarlo y qué
herramientas puede tocar. Abajo va su **system prompt**: las instrucciones que
guían su comportamiento.

---

## Plantilla

```markdown
---
name: nombre-del-agente
description: >
  Para qué sirve y CUÁNDO invocarlo. Describe la situación típica que lo
  amerita (p. ej. "cuando llega un estudio nuevo y hay que sacar mensajes de
  difusión"). Esta descripción es lo que permite que el agente se elija en el
  momento correcto.
tools: Read, Write, Grep, Glob
---

Eres un agente especializado del IEEC para [tarea].

Tu objetivo es [resultado concreto que debe entregar].

Cómo trabajas:
1. [Primer paso: qué lees o revisas primero.]
2. [Usa el skill <nombre-del-skill> para la parte central del procedimiento.]
3. [Cómo presentas el resultado y a quién va dirigido.]

Reglas (dignidad de los datos):
- Entregas SIEMPRE borradores para revisión humana; no publicas ni decides por
  tu cuenta.
- Si la tarea toca datos sensibles, mantén todo local y avisa.
- Cita fuente y dato; distingue dato de interpretación; no inventes citas.

Si algo es ambiguo o faltan datos, detente y pregunta antes de continuar.
```

Notas sobre el frontmatter:

- **`tools`**: la lista de herramientas que el agente puede usar. Dale solo las
  que necesite. Para tareas de lectura y redacción suelen bastar `Read`,
  `Write`, `Grep`, `Glob`. Si no necesita ejecutar comandos, **no** le des
  `Bash` (principio de mínimo privilegio: así no puede hacer de más).
- **`description`**: igual que en los skills, es lo que decide *cuándo* se usa.
  Sé específico.

---

## Cómo se conecta con skill + hook

Un agente bien armado **reutiliza** un skill en lugar de repetir el procedimiento
en su prompt, y suele ser **invocado** por un hook cuando ocurre el evento que lo
amerita. Ejemplo concreto, totalmente desarrollado, en
`examples/difusion/agent.md`:

- El **hook** (`examples/difusion/hook.md`) detecta que llegó un estudio nuevo a
  `estudios/`.
- El **agente** (`examples/difusion/agent.md`) toma ese estudio como encargo.
- El **skill** (`examples/difusion/SKILL.md`, `extraer-mensajes-difusion`) hace
  el trabajo: leer el estudio, extraer hallazgos y redactar los mensajes.
- El resultado son borradores de mensajes que una persona del equipo de difusión
  revisa antes de publicar.

Empieza por el skill (es lo más reutilizable), luego el hook, y al final el
agente que los une.
