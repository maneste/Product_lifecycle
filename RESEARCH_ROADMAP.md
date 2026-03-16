# Research Module Roadmap

Mejoras para convertir el módulo de research en un asistente activo del PM — no solo procesa entrevistas ya hechas, sino que ayuda a preparar mejor la investigación, evita sesgos y estructura los hallazgos de forma accionable.

Inspiración: análisis comparativo con el AI Mercadona User Story Framework (marzo 2026).

---

## Mejoras planificadas

### 1. Gap Analysis pre-research ← EN PROGRESO
**Qué es:** Antes de generar el PRD (o justo después de un primer draft), analizar qué no sabemos y clasificarlo en dos categorías: gaps que se resuelven con stakeholders internos vs. gaps que requieren hablar con usuarios reales.

**Por qué importa:** Evita hacer research innecesario. Peor aún, evita construir un PRD sobre suposiciones sin haber identificado las incógnitas críticas.

**Artefactos a crear:**
- Skill `/gap-analysis` — análisis interactivo del PRD con taxonomía de gaps
- Taxonomía de 14+ tipos de gaps (operaciones/negocio vs. producto/usuario)
- Sistema de puntuación de severidad (crítico, mayor, menor, refinamiento)
- Gap Score que recomienda cuánta investigación hace falta y de qué tipo

**Archivos a crear/modificar:**
- `.claude/skills/gap-analysis/SKILL.md`
- `.claude/skills/gap-analysis/references/gap-taxonomy.md`
- Integración en el flujo PRD → gap analysis → research

---

### 2. Generación dinámica de guión de entrevista
**Qué es:** En lugar del prompt estático de 8 categorías en `interview_analysis.promptl`, generar el guión a partir del PRD concreto: qué métricas asume, qué flujo describe, qué JTBDs hipotiza.

**Por qué importa:** El guión actual es genérico. Un guión adaptado a la feature ayuda al PM a explorar exactamente las incógnitas identificadas en el gap analysis.

**Artefactos a crear:**
- Skill `/interview-script` — genera guión de 5 fases (Mom Test) a partir del PRD
- Integración con los gaps identificados en paso 1
- Output: guión listo para usar por el PM

**Referencias metodológicas:**
- Mom Test (Rob Fitzpatrick): habla de su vida, pregunta por el pasado concreto, habla menos
- 5 fases: warm-up → vida del usuario → comportamiento actual → deep dive en gaps → cierre

---

### 3. Modos Discover / Validate
**Qué es:** Dos modos operativos para el research según el nivel de hipótesis previas.

- **Discover:** cuando el árbol de oportunidades no tiene hipótesis fuertes. Exploración abierta, sin anclas.
- **Validate:** cuando el PRD ya incluye JTBDs hipotéticos. Regla anti-sesgo estricta: nunca mencionar, sugerir ni insinuar los JTBDs durante la entrevista.

**Por qué importa:** En modo Validate, si el usuario no confirma los JTBDs espontáneamente, eso es un hallazgo valioso — no un fracaso.

**Artefactos a crear:**
- Parámetro `--mode discover|validate` en el guión generado
- Instrucciones anti-sesgo explícitas para modo Validate
- Integración con el árbol de oportunidades para determinar el modo recomendado

---

### 4. Filtro de datos malos en el análisis
**Qué es:** Una capa de filtrado en el análisis post-entrevista que descarta datos no accionables antes de extraer insights.

**Datos a filtrar:**
- Cumplidos: "me encanta la app", "todo está muy bien"
- Opiniones sobre el futuro: "creo que estaría bien si...", "me gustaría que..."
- Vaguedades: "a veces", "más o menos", "depende"

**Datos a conservar:** solo comportamientos pasados observables y hechos concretos.

**Artefactos a crear:**
- Nueva sección en `interview_analysis.promptl`: filtro pre-extracción
- Criterios explícitos de qué cuenta como evidencia válida

---

### 5. JTBD como output estructurado del análisis
**Qué es:** Añadir una fase final al pipeline que, a partir de los quotes consolidados, genere JTBDs estructurados listos para alimentar el PRD.

**Estructura de cada JTBD:**
- Job Performer (quién, con qué contexto específico)
- Trigger (qué situación activa la necesidad)
- Struggle (qué le cuesta hacer, con citas literales)
- Outcome deseado (qué quiere lograr)
- Motivación funcional / emocional / social
- Ansiedades y barreras

**Por qué importa:** Hoy el output es `validated_opportunities[]`. Los JTBDs son una capa táctica más cercana a las user stories — la síntesis de oportunidades → JTBDs hoy queda implícita y la hace el PM manualmente.

**Artefactos a crear:**
- Nueva fase en `aggregate_results.py` o skill separado
- Schema JSON para JTBDs estructurados
- Integración: JTBDs quedan disponibles para el skill `prd`

---

## Secuencia de implementación

```
[1] Gap Analysis     →  [2] Guión dinámico  →  [3] Discover/Validate
        ↓
[4] Filtro datos malos  →  [5] JTBD output
```

Los ítems 1, 2 y 3 son pre-entrevista. Los ítems 4 y 5 son post-entrevista.
El ítem 1 es el desbloqueante: si el PM sabe qué no sabe, todo lo demás mejora.

---

## Estado

| # | Mejora | Estado |
|---|--------|--------|
| 1 | Gap Analysis pre-research | Completado |
| 2 | Generación dinámica de guión | Completado |
| 3 | Modos Discover / Validate | Pendiente |
| 4 | Filtro de datos malos | Pendiente |
| 5 | JTBD como output estructurado | Pendiente |
