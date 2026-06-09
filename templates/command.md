# Plantilla de Command (comando `/`)

Un **command** ("comando") es un atajo que **tú** invocas escribiendo `/nombre`
en Claude Code. Es un skill que decides correr a mano —a diferencia de un skill
que Claude activa solo cuando detecta que aplica—. Sirve para flujos repetibles
que quieres disparar cuando tú quieras: `/commit`, `/reporte-semanal`,
`/revisar-base`.

Desde las versiones recientes de Claude Code, los comandos viven en
`.claude/skills/` igual que los skills. Lo que los vuelve "solo para ti" es la
línea `disable-model-invocation: true` en el frontmatter: con ella, Claude **no**
lo activa por su cuenta; solo corre cuando tú escribes `/nombre`.

> **No tienes que escribir esto a mano.** Puedes pedirle a Claude Code:
> "créame un comando `/reporte-semanal` que haga X, Y, Z". Esta plantilla sirve
> para entender qué genera y para ajustarlo después.

---

## Dónde vive

```
.claude/skills/reporte-semanal/SKILL.md   →  se invoca con /reporte-semanal
```

Si lo pones en una subcarpeta, el nombre lleva el prefijo de la carpeta:

```
.claude/skills/equipo/commit/SKILL.md     →  se invoca con /equipo:commit
```

---

## Plantilla

```markdown
---
description: >
  Una línea: qué hace este comando cuando lo invocas. (Se ve en el menú de /).
argument-hint: "[archivo] [--opcion]"
disable-model-invocation: true
---

# Nombre legible del comando

## Propósito

Qué resuelve este comando, en una frase.

## Proceso

Sigue estos pasos:

1. **Primer paso** — instrucción concreta.
2. **Segundo paso** — instrucción concreta.
3. **Tercer paso** — entrega el resultado.

## Argumentos

- Si te paso un argumento, úsalo como: $ARGUMENTS[0]  (o $0)
- Si no te paso ninguno: comportamiento por omisión.

## Salida

Qué entrega y en qué formato.

## Resguardos

- Qué NO debe hacer.
- Dónde queda el juicio humano (la IA prepara, una persona decide).
```

---

## Ejemplo mínimo

```markdown
---
description: >
  Genera el borrador del reporte semanal de asistencia a partir del CSV de la
  semana. Solo se corre a mano con /reporte-semanal.
argument-hint: "[archivo-csv]"
disable-model-invocation: true
---

# Reporte semanal de asistencia

## Propósito

Convierte el CSV de asistencia de la semana en un borrador de reporte con las
escuelas en alerta, listo para revisión humana.

## Proceso

1. Lee el CSV que te indique ($0); si no indico ninguno, usa el más reciente en
   `datos/asistencia/`.
2. Calcula asistencia por escuela y marca las que bajaron más de 10 puntos.
3. Redacta un borrador de media página con una tabla de escuelas en alerta.

## Salida

- Un archivo `borrador-reporte-semana.md` con la tabla y el resumen.

## Resguardos

- No envíes el reporte a nadie: es un **borrador** para que una persona lo revise.
- Si faltan datos de una escuela, márcala como "sin dato", no inventes cifras.
```
