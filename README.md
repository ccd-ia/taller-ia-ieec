# Taller de IA con Claude Code — IEEC

Repositorio base ("starter repo") del **Taller de IA con Claude Code para el IEEC**
(Iniciativa de Educación con Equidad y Calidad, dir. Marco Fernández).

Cada participante clona este repositorio al inicio de la Sesión 1 y trabaja
dentro de él durante todo el taller. El repositorio es propiedad del IEEC: lo que
construyamos aquí (sobre todo el `CLAUDE.md` institucional) queda como activo del
equipo para seguir usándolo después del taller.

---

## ¿Qué es esto?

Una carpeta con plantillas, ejemplos y datos sintéticos pensados para que un
equipo **no especializado en programación** aprenda a usar Claude Code en tareas
reales de política educativa: limpiar bases, redactar mensajes de difusión,
resumir estudios, construir tableros, automatizar reportes, etc.

No necesitas saber programar. Necesitas:

1. Tener Claude Code instalado (ver `INSTALL.md`).
2. Saber describir bien una tarea que ya haces a mano.
3. Curiosidad para iterar.

---

## Los 5 equipos del IEEC

Los ejercicios del taller corren sobre tareas reales de cada equipo. Si no sabes
en cuál estás, pregúntale a tu líder de equipo.

| # | Equipo | Personas | Tareas representativas |
|---|--------|----------|------------------------|
| 1 | Evaluaciones y rutas formativas | Sandra, Daniel, Luis | Actualizar bancos de reactivos; limpiar y uniformar bases; innovar presentaciones de resultados (mapas/dashboards); calificar respuestas abiertas (sensible) |
| 2 | Aprendizajes para Todos (APT) | Ileana, Ana, Pablo | Chatbot de preguntas frecuentes de APT; automatizar reportes semanales de asistencia; predicción de bajas (sensible) |
| 3 | Skills / mercado laboral | Rubén, Noemi | Scraping de bolsas de trabajo (Conocer); tablero de indicadores (ENOE, IMSS); automatizar la etapa inicial de estudios de habilidades |
| 4 | Auditorías / presupuesto — Infraestructura LEN | Javier, Roberto | Resúmenes de estudios con imágenes; resumir entrevistas en audio/video (sensible); gráficas mejor diseñadas; web scraping de movilizaciones magisteriales; análisis de sentimiento en redes |
| 5 | Difusión y Clase de Marco | Marco, Karla, Pablo | Monitoreo y sistematización de noticias por línea de investigación; extracción de mensajes de difusión; gestión y recuperación de notas; asistente virtual de Marco (calendario + correo vía MCP); asistente de calificaciones (crítico); recopilación de participaciones (crítico) |

> El **Equipo 5** tiene un ejemplo completamente desarrollado en
> `examples/difusion/` que sirve de modelo para todos los demás.

---

## Dignidad de los datos (regla del taller)

Algunas tareas manejan datos de **sensibilidad crítica**: calificación de
estudiantes, participaciones grabadas en clase, audio de entrevistas,
expedientes y notas internas. Para esas tareas la regla es clara:

- **Mantener local**: el dato no sale del perímetro del IEEC.
- **Humano en el bucle**: la IA propone, una persona decide.
- **Consentimiento**: si hay personas grabadas o identificables, debe haber
  consentimiento.
- **La IA valida, no decide**: úsala para revisar, ordenar y borrador, nunca
  para emitir el veredicto final sobre una persona.

Cuando evaluemos una idea (Ejercicio 2) la puntuamos en cuatro ejes:
**impacto**, **factibilidad**, **sensibilidad de los datos** (¿sale del
perímetro?) y **dónde queda el juicio humano**.

---

## Cómo se usa este repositorio

### Sesión 1 — Ejercicios (martes 2 de junio, 11:00–15:00)

Trabajamos con las plantillas y los datos sintéticos para aprender el modelo
mental de Claude Code:

- **Plantillas** (`templates/`): CRAFT para prompts, `CLAUDE.personal.md`,
  y las plantillas de skill, hook y agente.
- **Meta-prompt** (`meta-prompts/build-a-skill.md`): el corazón del taller.
  Lo pegas en Claude Code, te entrevista sobre un procedimiento que repites, y
  te **genera** un skill funcional sin que tengas que programarlo.
- **Ejemplo** (`examples/difusion/`): un caso completo de extremo a extremo.
- **Datos** (`demo-data/`): archivos sintéticos para practicar sin tocar datos
  reales.

### Sesión 2 — `CLAUDE.md` institucional

Tomamos el esqueleto `CLAUDE.institutional.md` y entre todos lo extendemos:
definimos el tono institucional, los criterios de evidencia, y completamos las
**seis líneas de investigación** del IEEC. Al activarlo como el `CLAUDE.md` del
equipo, se vuelve la memoria compartida que Claude Code lee en cada sesión.

---

## Estructura del repositorio

```
taller-ia-ieec/
├── README.md                      ← este archivo
├── INSTALL.md                     ← cómo instalar Claude Code
├── CLAUDE.institutional.md        ← esqueleto institucional (se activa como CLAUDE.md en Sesión 2)
├── templates/
│   ├── CLAUDE.personal.md         ← contexto personal de cada participante
│   ├── craft-prompt.md            ← andamiaje CRAFT para prompts
│   ├── skill.md                   ← plantilla de SKILL.md
│   ├── hook.md                    ← qué son los hooks y cómo configurarlos
│   └── agent.md                   ← plantilla de subagente (une skill + hook)
├── meta-prompts/
│   └── build-a-skill.md           ← meta-prompt que te genera un skill
├── examples/
│   └── difusion/                  ← ejemplo completo del Equipo 5
│       ├── SKILL.md
│       ├── hook.md
│       ├── agent.md
│       └── estudios/estudio-ejemplo.md
└── demo-data/
    ├── resultados-evaluacion.csv
    ├── asistencia.csv
    └── estudio-ejemplo.md
```

---

## Antes de empezar

1. Lee `INSTALL.md` y verifica que `claude` funcione en tu terminal.
2. Copia `templates/CLAUDE.personal.md` a la raíz como `CLAUDE.personal.md`
   y llénalo con tu rol, equipo y tareas.
3. Abre la carpeta del repositorio con `claude` y escribe `hola`.

¡Nos vemos en el taller!
