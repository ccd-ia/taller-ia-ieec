# Andamiaje CRAFT para prompts

Un buen prompt no es magia: es una instrucción bien estructurada. **CRAFT** es
una forma fácil de recordar las cinco piezas que casi siempre mejoran el
resultado.

| Letra | Pieza | Pregunta que responde |
|-------|-------|------------------------|
| **C** | Contexto | ¿Qué situación, datos o antecedentes necesita conocer la IA? |
| **R** | Rol | ¿Desde qué perspectiva o expertise debe responder? |
| **A** | Acción | ¿Qué quiero exactamente que haga? (un verbo claro) |
| **F** | Formato | ¿Cómo quiero el resultado? (tabla, viñetas, longitud) |
| **T** | Tono | ¿Con qué registro? (formal, divulgativo, para autoridades) |

No siempre necesitas las cinco, pero entre más completes, mejor sale.

---

## Plantilla en blanco

Copia esto y llena cada parte:

```
CONTEXTO:
(Describe la situación y los datos. Por ejemplo: qué archivo vas a usar, de qué
trata, qué periodo cubre, qué se hizo antes.)

ROL:
(Indica desde qué perspectiva debe trabajar la IA. Por ejemplo: "Actúa como
analista de datos educativos del IEEC".)

ACCIÓN:
(Di con un verbo claro qué quieres: limpia, resume, compara, redacta, grafica,
clasifica. Sé específico sobre el alcance.)

FORMATO:
(Cómo quieres la salida: una tabla con estas columnas, tres viñetas, un párrafo
de máximo 100 palabras, un archivo CSV.)

TONO:
(El registro: profesional y basado en evidencia, divulgativo para redes,
formal para un oficio dirigido a autoridades.)
```

---

## Ejemplo lleno (política educativa)

```
CONTEXTO:
Tengo el archivo demo-data/resultados-evaluacion.csv con los promedios de una
evaluación de matemáticas y español por estado, con el número de estudiantes
evaluados (n_estudiantes) en cada caso. Es un corte estatal de una sola
aplicación.

ROL:
Actúa como analista de evaluación educativa del IEEC, con cuidado de no
sobreinterpretar diferencias pequeñas entre estados.

ACCIÓN:
Identifica los tres estados con el promedio más bajo en matemáticas y los tres
más altos. Para cada uno, reporta también su promedio en español y su
n_estudiantes. Señala si alguno de esos estados tiene una muestra
especialmente pequeña que obligue a tomar el dato con cautela.

FORMATO:
Una tabla en Markdown con columnas: estado, promedio_matematicas,
promedio_espanol, n_estudiantes, nota. Debajo de la tabla, dos viñetas con los
hallazgos principales.

TONO:
Profesional y basado en evidencia. Distingue claramente el dato de la
interpretación, y no afirmes causas; solo describe lo que muestran los números.
```

---

## Consejos rápidos

- **Itera.** El primer resultado casi nunca es el final. Pide ajustes: "más
  corto", "agrega una columna con el porcentaje", "cámbialo a tono divulgativo".
- **Pide que pregunte.** Si tu tarea es ambigua, agrega: "antes de empezar,
  hazme las preguntas que necesites". Es justo lo que hace el meta-prompt de
  `meta-prompts/build-a-skill.md`.
- **Recuerda la dignidad de los datos.** Si la tarea toca datos sensibles
  (calificaciones, audio, expedientes), pide borradores para revisión humana,
  nunca decisiones automáticas.
