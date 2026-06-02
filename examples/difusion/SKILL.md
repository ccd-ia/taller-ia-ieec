---
name: extraer-mensajes-difusion
description: >
  Lee un estudio del IEEC y redacta borradores de mensajes de difusión a partir
  de sus hallazgos: un hilo para Twitter/X, un bloque para boletín (newsletter)
  y un mensaje para tomadores de decisiones (stakeholders). Actívalo cuando el
  usuario pida sacar mensajes de difusión, comunicar un estudio, hacer un hilo o
  un boletín a partir de un documento de hallazgos, o cuando llegue un estudio
  nuevo a la carpeta estudios/. NO lo uses para escribir el estudio mismo ni
  para análisis estadístico; parte de un estudio que YA existe.
---

# Extraer mensajes de difusión

Convierte un estudio del IEEC en borradores de comunicación para tres públicos,
listos para que el equipo de difusión los revise y publique.

## Procedimiento

### Entradas

- Un estudio en formato Markdown o texto (por defecto, el archivo más reciente
  en `examples/difusion/estudios/` o el que indique el usuario).
- Se asume que el estudio tiene una sección de hallazgos y datos con sus cifras.

### Pasos

1. Lee el estudio completo e identifica: título, línea de investigación, periodo,
   muestra/fuente y los 3 hallazgos principales.
2. Para cada hallazgo, extrae la **cifra clave** y su **contexto** (a qué se
   compara, de qué periodo es). Anota la fuente exacta tal como aparece en el
   estudio.
3. Redacta tres borradores, todos en español de México:
   - **Hilo de Twitter/X**: 4 a 6 tuits cortos. El primero engancha con el
     hallazgo más fuerte; los siguientes desarrollan los otros dos hallazgos;
     el último cierra con la recomendación principal y menciona al IEEC. Sin
     exagerar las cifras.
   - **Boletín (newsletter)**: un bloque de 120–180 palabras con un titular,
     dos o tres párrafos y una frase de cierre con la implicación de política.
   - **Mensaje para tomadores de decisiones**: 4 a 6 viñetas sobrias con el dato,
     su fuente y la acción sugerida. Tono institucional.
4. Debajo de cada borrador, agrega una línea **"Fuente:"** con la referencia del
   estudio, para que quien publique no pierda la trazabilidad.

### Salida

- Los tres borradores (hilo, boletín, mensaje a decisores), en Markdown, en
  pantalla, claramente separados con encabezados.
- Cada cifra acompañada de su fuente.
- Una nota final: "Borradores para revisión humana antes de publicar."

### Resguardos

- **La IA redacta, una persona del equipo de difusión aprueba y publica.** Nunca
  publiques automáticamente.
- **Cita fuente y dato.** No uses ninguna cifra que no esté en el estudio.
- **No exageres ni inventes.** Si un hallazgo es preliminar o el estudio marca
  una limitación (p. ej. "no implica causalidad"), respétalo en el mensaje: no
  conviertas una asociación en una relación causal.
- **Distingue dato de interpretación** en el texto.
- Si el estudio no trae cifras claras o falta la fuente, detente y avisa; no
  rellenes con números aproximados.
