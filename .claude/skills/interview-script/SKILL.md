---
name: interview-script
description: Generate a Mom Test–compliant 5-phase interview guide from a PRD. Always starts by asking what the PM has (PRD, gap analysis, research mode). Adapts questions to the specific feature — never uses generic templates. Determines Discover vs. Validate mode and includes an anti-bias checklist for the interviewer. Use before conducting user interviews.
---

# Interview Script Skill

Genera un guión de entrevista de usuario adaptado a una feature concreta, siguiendo la metodología Mom Test (Rob Fitzpatrick). No usa templates genéricos — cada guión se construye a partir del PRD y los gaps específicos de esa feature.

**Cuándo usar:** antes de salir a hacer entrevistas de usuario. Después de `/prd` y opcionalmente después de `/gap-analysis`.

**Disparador:** "genera el guión de entrevista", "prepara las preguntas para usuarios", "interview script", "cómo entrevisto sobre [feature]".

---

## INSTRUCCIONES PARA EL ASISTENTE

### Arranque — siempre preguntar, nunca asumir

Al inicio de cada sesión, pregunta exactamente esto:

> "Para generar el guión necesito saber con qué partimos. Dime:
> 1. ¿Tienes el PRD de la feature? Pégalo aquí o indícame dónde está.
> 2. ¿Has hecho un gap analysis previo? Si tienes el output, pégalo también.
> 3. ¿Sabes ya si es investigación exploratoria (Discover) o de validación (Validate)? Si no estás seguro, lo determinamos juntos."

No intentes inferir rutas ni buscar archivos. El PM trae el contexto — tú lo procesas.

Si el PM no tiene gap analysis, no lo hagas completo — extrae los gaps relevantes para el guión de forma inline (10 minutos de análisis, no un gap report completo).

---

### Fase 1 — Entender el contexto del PRD

Con el PRD delante, extrae:

**Para la cabecera del entrevistador (contexto interno, nunca se verbaliza al usuario):**
- El problema que el PRD asume que existe
- Las métricas de éxito que el PRD propone
- El perfil de usuario al que va dirigido
- Los JTBDs o hipótesis de comportamiento que el PRD asume (explícitos o implícitos)
- Los gaps o incógnitas más relevantes para la entrevista

**Para determinar el modo:**
- Si hay gap analysis previo: usa el Gap Score para decidir
  - Gap Score ≥80 o gaps CRÍTICOS de tipo Problem Framing / Desirability / User Context → **DISCOVER**
  - Gap Score <40 con JTBDs documentados → **VALIDATE**
- Si no hay gap analysis: evalúa el PRD — ¿tiene JTBDs con evidencia o son hipótesis sin respaldo?
  - Sin evidencia → **DISCOVER**
  - Con evidencia sólida → **VALIDATE**
  - Dudas → pregunta al PM

---

### Fase 2 — Determinar las preguntas de deep dive

Identifica las 3-5 incógnitas más importantes que esta entrevista debe responder. Estas serán la columna vertebral de la fase 4 del guión.

Para cada incógnita:
- Clasifícala en el tipo de gap (User Context, Desirability, PF, Segment, etc.)
- Elige el template de pregunta correspondiente de `references/mom-test-question-templates.md`
- Adapta el template al dominio y vocabulario específico del PRD
- Verifica que no sea leading, hipotética ni mencione la solución

---

### Fase 3 — Construir el guión de 5 fases

#### FASE 1: Warm-up (5 min)
Objetivo: crear rapport, entender el contexto del usuario sin contaminar la entrevista.

Incluir siempre:
- Presentación y agradecimiento (sin mencionar qué se va a preguntar)
- 1-2 preguntas de contexto general del usuario (rol, cuánto tiempo lleva, contexto de uso)
- NO mencionar el producto, la feature ni el problema que el PRD asume

#### FASE 2: Vida del usuario (10 min)
Objetivo: entender cómo es su día a día en el dominio relevante, sin anclas.

Construir 3-4 preguntas abiertas sobre su rutina en el área del PRD.
En modo DISCOVER: completamente abierto, que el usuario lleve la narrativa.
En modo VALIDATE: ligeramente más dirigido al dominio, pero sin mencionar hipótesis.

#### FASE 3: Comportamiento actual (10 min)
Objetivo: entender cómo resuelven hoy lo que el PRD asume como problema.

Preguntas centradas en comportamiento pasado concreto:
- "La última vez que [situación del PRD]... ¿qué hiciste?"
- "¿Cómo lo resuelves actualmente?"
- "¿Qué herramientas/procesos usas?"

Nunca mencionar la solución propuesta en el PRD.

#### FASE 4: Deep dive en gaps (15 min)
Objetivo: responder las incógnitas críticas identificadas en Fase 2.

Para cada incógnita: 1-2 preguntas Mom Test–compliant, ordenadas de más abierta a más específica.

**Regla en modo VALIDATE:** si los JTBDs hipotéticos del PRD no emergen espontáneamente en las fases anteriores, no los introduzcas aquí. Anota su ausencia como hallazgo.

#### FASE 5: Cierre (5 min)
Incluir siempre:
- "¿Hay algo de lo que hemos hablado que quieras añadir o matizar?"
- "¿Conoces a alguien más que se enfrente a esto y con quien debería hablar?"
- Agradecimiento

---

### Fase 4 — Construir la cabecera del entrevistador

Sección que va al inicio del documento, marcada claramente como **SOLO PARA EL ENTREVISTADOR — NO VERBALIZAR**.

Incluye:
- Qué asume el PRD (lista de supuestos)
- Qué queremos validar o descubrir con esta entrevista (las incógnitas de Fase 2)
- Qué JTBDs hipotiza el PRD (si existen) — recordatorio de que NO se mencionan
- Señales a escuchar: comportamientos, frases o situaciones que confirmarían o refutarían los supuestos
- Señales de datos malos a descartar: cumplidos, hipotéticos, vaguedades

---

### Fase 5 — Checklist anti-sesgo

Al final del documento, una lista de verificación para antes de empezar la entrevista:

```
ANTES DE LA ENTREVISTA
[ ] He leído la cabecera del entrevistador
[ ] Sé qué JTBDs NO voy a mencionar
[ ] Tengo las preguntas memorizadas (no leer del guión como un robot)

DURANTE LA ENTREVISTA
[ ] ¿Estoy hablando de su vida o de mi PRD?
[ ] ¿Mis preguntas son sobre el pasado o sobre hipótesis futuras?
[ ] ¿Estoy escuchando o estoy validando lo que quiero oír?
[ ] Si el usuario da un cumplido, ¿pregunto por un ejemplo concreto?
[ ] Si el usuario dice "creo que usaría X", ¿pregunto por la última vez que lo necesitó?

SEÑALES DE ALARMA (parar y redirigir)
[ ] Me he puesto a explicar la feature
[ ] He usado las palabras del PRD
[ ] He preguntado "¿te gustaría que...?"
[ ] El usuario solo está siendo amable
```

---

### Output final

Presenta el guión completo en la conversación y pregunta si quiere guardarlo. Si confirma, guárdalo donde el PM indique (ruta libre — no asumir estructura de carpetas).

Formato del archivo: `[Feature]_Interview_Guide.md`

Estructura del documento:
```
# Guión de Entrevista — [Nombre de la Feature]

## SOLO PARA EL ENTREVISTADOR (no verbalizar)
[Cabecera con supuestos, JTBDs, señales a escuchar]

---

## Modo: DISCOVER / VALIDATE

## Perfil de entrevistado objetivo
[Quién buscar, criterios de selección]

---

## FASE 1: Warm-up (5 min)
[Preguntas]

## FASE 2: Vida del usuario (10 min)
[Preguntas]

## FASE 3: Comportamiento actual (10 min)
[Preguntas]

## FASE 4: Deep dive (15 min)
[Preguntas por incógnita]

## FASE 5: Cierre (5 min)
[Preguntas]

---

## Checklist anti-sesgo
[Lista de verificación]
```

---

## Archivos de referencia

- `references/mom-test-question-templates.md` — patrones de pregunta por tipo de gap y anti-patrones
