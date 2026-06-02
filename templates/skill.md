# Plantilla de SKILL.md

Un **skill** (habilidad) es un procedimiento reutilizable que le enseñas a Claude
Code una vez y que luego puede ejecutar cuando lo necesites. Vive en un archivo
llamado `SKILL.md` dentro de `.claude/skills/<nombre-del-skill>/`.

La parte de arriba (entre las líneas con `---`) es el **frontmatter**: le dice a
Claude *cómo se llama* el skill y *cuándo* debe activarse. La `description` es la
parte más importante: ahí van las palabras que disparan el skill.

> **No tienes que escribir esto a mano.** El meta-prompt
> `meta-prompts/build-a-skill.md` te entrevista y genera este archivo por ti.
> Esta plantilla sirve para entender qué produce ese meta-prompt y para
> ajustarlo después.

---

## Plantilla

```markdown
---
name: nombre-del-skill
description: >
  Qué hace este skill y CUÁNDO debe activarse. Incluye las palabras y
  situaciones que lo disparan (p. ej. "cuando el usuario pida limpiar una base
  de evaluación", "al uniformar nombres de estados", "revisar-base"). Entre más
  específica la descripción, mejor se activa en el momento correcto. NO lo
  actives para X (aclara los casos en que NO aplica).
---

# Nombre legible del skill

Una o dos frases que expliquen el propósito en lenguaje claro.

## Procedimiento (Procedure)

Resumen en una línea de lo que logra el procedimiento.

### Entradas (Inputs)

- Qué necesita para empezar (un archivo, una carpeta, ciertos campos).
- Supuestos sobre el formato de esas entradas.

### Pasos (Steps)

1. Primer paso, concreto y verificable.
2. Segundo paso.
3. Tercer paso.
   (Mantén los pasos en orden y específicos: "uniforma la columna `estado` a
   mayúsculas y sin acentos" es mejor que "limpia los datos".)

### Salida (Output)

- Qué entrega y en qué formato (una tabla en Markdown, un CSV nuevo, un
  resumen de media página).
- Dónde la deja (en pantalla, en un archivo, en qué carpeta).

### Resguardos (Guardrails)

- Qué NO debe hacer este skill.
- Cómo se respeta la dignidad de los datos (humano en el bucle, mantener local,
  no decidir sobre personas).
- Qué hacer ante datos faltantes, ambiguos o sospechosos: detenerse y
  preguntar, nunca inventar.
```

---

## Ejemplo mínimo

```markdown
---
name: uniformar-estados
description: >
  Normaliza la columna de estado/entidad en una base educativa para que todas
  las variantes ("CDMX", "Ciudad de México", "D.F.") queden igual. Actívalo
  cuando el usuario pida uniformar, estandarizar o limpiar nombres de estados o
  entidades federativas en un CSV. NO lo uses para limpiar otras columnas.
---

# Uniformar nombres de estados

Estandariza los nombres de las 32 entidades federativas a una forma canónica.

## Procedimiento

### Entradas
- Un archivo CSV con una columna de estado/entidad (el usuario indica cuál).

### Pasos
1. Detecta la columna de entidad.
2. Mapea cada variante a su nombre oficial (catálogo de 32 entidades).
3. Marca en una columna nueva `revisar` cualquier valor que no haya podido
   mapear con confianza.

### Salida
- Un CSV nuevo con la columna uniformada y la columna `revisar`.
- Un breve resumen de cuántas filas se normalizaron y cuántas quedaron por
  revisar.

### Resguardos
- No elimines filas: marca lo dudoso para revisión humana.
- Si más del 10% queda sin mapear, detente y avisa antes de continuar.
```
