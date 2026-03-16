---
name: gap-analysis
description: Analyze a PRD to identify knowledge gaps before committing to design or development. Classifies gaps by type and severity (CRITICAL/MAJOR/MINOR), separates what to resolve with internal stakeholders vs. user research, recommends Discover or Validate research mode, and surfaces unknown unknowns using pre-mortem, assumption inversion, and Roger Martin's "What would have to be true?" techniques. Use after /prd or before designing user interviews.
---

# Gap Analysis Skill

Analiza un PRD (borrador o final) para identificar qué no sabe el equipo antes de comprometer capacidad de entrega. Clasifica los gaps por tipo, severidad y quién puede resolverlos. Ayuda al PM a descubrir lo que no sabe que no sabe.

**Cuándo usar:**
- Justo después de generar un PRD con `/prd` — para validar qué research falta antes de avanzar a flow design
- Antes de diseñar entrevistas de usuario — para saber exactamente qué explorar
- Cuando el PM siente que "algo falta" pero no sabe qué

**Disparador:** cuando el usuario dice "analiza este PRD", "qué gaps tiene", "qué me falta investigar", "gap analysis", o quiere saber si el PRD está listo para avanzar.

---

## INSTRUCCIONES PARA EL ASISTENTE

### Contexto metodológico

Este skill implementa un gap analysis basado en:
- **14 familias de gaps** (gap-taxonomy.md): desde problem framing hasta perception gaps
- **Scoring de severidad** basado en UK GDS: `Risk = Impact (1-10) × (10 - Confidence)`
- **Clasificación de locus**: stakeholder interno vs. research con usuarios reales
- **Técnicas de unknown unknowns**: pre-mortem, "What would have to be true?", assumption inversion
- **Modo recomendado de research**: Discover vs. Validate según el volumen de gaps críticos

Lee `references/gap-taxonomy.md` antes de comenzar el análisis.

---

### Fase 0 — Obtener el PRD

Si el usuario no ha pegado el PRD, pide que lo haga o que indique la ruta del archivo. No comiences el análisis sin tener el texto del PRD.

Si hay un PRD en `AI_Output/` del proyecto actual, léelo automáticamente y confirma cuál vas a analizar.

---

### Fase 1 — Análisis de supuestos implícitos (unknown unknowns)

Antes de clasificar gaps en la taxonomía, aplica estas 4 técnicas para descubrir lo que el PRD no dice:

**1. "What would have to be true?"** (Roger Martin)
Lista todas las condiciones que tendrían que ser verdad para que este PRD tenga éxito. Para cada condición pregúntate: ¿hay evidencia de esto en el PRD? Si no la hay, es un gap candidato.

Ejemplos de condiciones a chequear:
- Los usuarios experimentan este problema con la frecuencia/intensidad que asume el PRD
- Los usuarios adoptarán el comportamiento nuevo que la solución requiere
- El equipo puede construir esto con la tecnología disponible
- El negocio puede sostener el coste operacional de esta feature
- No hay implicaciones legales o de privacidad sin explorar

**2. Pre-mortem del PRD**
Imagina que es 6 meses después del lanzamiento y la feature ha fracasado. ¿Cuáles son los 5 motivos más probables? Cada motivo revela un gap no articulado en el PRD.

**3. Assumption inversion**
Para cada supuesto central del PRD, invierte: "¿Qué pasa si lo opuesto es verdad?" Si el PRD no puede sobrevivir a la inversión, el supuesto necesita validación.

**4. Reverse Five Whys**
Parte de la solución propuesta. Pregunta "¿por qué?" recursivamente hasta llegar al problema de usuario. Si la cadena se rompe o llega a respuestas vagas ("porque la competencia lo tiene"), hay un problem framing gap.

---

### Fase 2 — Clasificación en las 14 familias

Para cada gap detectado (tanto los obvios como los descubiertos en Fase 1), clasifícalo según la taxonomía:

**Categoría A — Gaps de usuario (research externo):**
1. Problem Framing Gap
2. Desirability Gap
3. Usability/UX Gap
7. Process Functional (PF) Gap
8. Process Inventory (PI) Gap
9. User Context Gap
10. Segment/Persona Gap
14. Perception/Communication Gap

**Categoría B — Gaps internos (stakeholders):**
4. Feasibility/Technical Gap
5. Business Viability Gap
6. Ethical/Harm Gap
11. Outcome/Metric Gap
12. Requirement Coverage Gap
13. Organizational/Resource Gap

Para cada gap identificado, documenta:
- **Tipo:** familia de gap (1-14)
- **Descripción específica:** qué exactamente no sabemos en el contexto de este PRD
- **Evidencia de su existencia:** qué parte del PRD revela este gap (cita textual si es posible)
- **Locus:** quién puede resolverlo (stakeholder concreto vs. tipo de research con usuarios)

---

### Fase 3 — Scoring de severidad

Para cada gap, asigna:

**Impact (1-10):** ¿Cuánto afecta al outcome si esta incógnita resulta ser distinta de lo asumido?
- 9-10: invalida el value proposition completo o crea riesgo legal/ético
- 7-8: cambia significativamente el diseño de la solución
- 5-6: afecta el scope pero no el núcleo
- 3-4: afecta detalles de implementación
- 1-2: cosmético, no cambia el ROI

**Confidence (1-10):** ¿Cuánta evidencia existe ya en el PRD o en el knowledge base (context_knowledge/) para esta afirmación?
- 9-10: evidencia directa, múltiples fuentes, quotes de usuarios
- 7-8: evidencia indirecta pero sólida
- 5-6: evidencia anecdótica o de una sola fuente
- 3-4: intuición del PM, sin datos
- 1-2: supuesto sin ningún respaldo

**Risk Score = Impact × (10 - Confidence)**

Ajustes:
- +10 si el gap es blocking (bloquea el avance del diseño o desarrollo)
- +5 si afecta safety, compliance o ética
- -10 si hay evidencia indirecta razonablemente sólida no reflejada en el PRD

**Categorías:**
- CRÍTICO: ≥70 → resolver antes de comprometer capacidad
- MAYOR: 40-69 → resolver en paralelo al inicio del diseño
- MENOR: 15-39 → resolver cuando sea posible
- REFINAMIENTO: <15 → optimizar post-lanzamiento

---

### Fase 4 — Gap Score y recomendación de research

Calcula el **Gap Score** del PRD:

```
Gap Score = Suma de todos los Risk Scores / Número de gaps
+ Penalización: +20 por cada gap CRÍTICO de Categoría A (requiere usuarios reales)
```

**Interpretación:**
- **Gap Score ≥ 80 o ≥2 gaps CRÍTICOS de Categoría A:** El PRD necesita research antes de avanzar a flow design. Recomienda modo **DISCOVER** si los gaps son de problem framing, desirability o user context. Recomienda modo **VALIDATE** si los gaps son de usability o segment con hipótesis claras.
- **Gap Score 40-79 o 1 gap CRÍTICO:** Research paralelo al diseño. Identifica cuál es el gap más urgente y diseña una investigación focalizada.
- **Gap Score <40:** PRD listo para avanzar. Gaps menores se pueden resolver con stakeholders durante el diseño.

**Modos de research:**
- **DISCOVER** cuando: problem framing, desirability, o user context gaps son críticos. No hay JTBDs validados. El equipo entra en territorio nuevo.
- **VALIDATE** cuando: las oportunidades están mapeadas en el árbol, hay hipótesis claras de JTBDs, y solo falta confirmar usability o comportamiento específico. **Regla anti-sesgo estricta en modo Validate:** nunca mencionar, sugerir ni insinuar los JTBDs del PRD durante la entrevista. Si el usuario no los confirma espontáneamente, eso es un hallazgo — no un fracaso.

---

### Fase 5 — Output: Gap Report

Presenta el análisis en este formato:

```
## Gap Analysis — [Nombre de la Feature]

### Gap Score: [número] → [CRÍTICO/MAYOR/MENOR/REFINAMIENTO]
### Research recomendado: [DISCOVER/VALIDATE/STAKEHOLDER/NINGUNO]

---

### Gaps CRÍTICOS (resolver antes de avanzar)

**[Tipo de Gap]** — [Nombre descriptivo del gap]
Descripción: [qué exactamente no sabemos]
Evidencia en PRD: "[cita del PRD que revela el gap]"
Locus: [quién puede resolverlo]
Impact: X/10 | Confidence: Y/10 | Risk Score: Z
Acción: [qué hacer concretamente — quién entrevistar, qué observar, qué preguntar]

[Repetir para cada gap CRÍTICO]

---

### Gaps MAYORES (resolver en paralelo)
[Lista condensada con acción recomendada]

### Gaps MENORES / REFINAMIENTO
[Lista condensada — no bloquean]

---

### Unknown Unknowns detectados
[Los gaps descubiertos en Fase 1 que no estaban articulados en el PRD]

---

### Próximos pasos recomendados

1. [Acción más urgente con responsable]
2. [Segunda acción]
3. [...]
```

---

### Comportamiento del asistente

**Sé un descubridor activo, no un validador pasivo.**

Tu trabajo no es confirmar que el PRD está bien — es descubrir lo que el PM no sabe que no sabe. Usa las técnicas de Fase 1 con genuina curiosidad investigadora. Cuando apliques el pre-mortem, propón escenarios de fracaso concretos y creíbles. Cuando apliques "What would have to be true?", articula las condiciones con precisión — no con vaguedades.

**Nunca suavices los gaps CRÍTICOS.** Si el PRD asume que los usuarios tienen un problema que no está documentado con evidencia real, dilo directamente. Un gap crítico sin resolver es una deuda de conocimiento que se paga con retrabajo.

**Conecta los gaps con evidencia existente.** Antes de marcar un gap como "sin evidencia", busca en `context_knowledge/` del proyecto — interview_summary, persona, opportunity_tree. Si hay evidencia que el PRD no cita, señálalo como gap de documentación, no de knowledge.

**Propón acciones concretas.** Cada gap CRÍTICO debe tener una acción específica: no "investigar más" sino "hacer 3 entrevistas contextuales con [perfil específico] para observar [comportamiento específico] y responder [pregunta concreta]".

---

## Archivos de referencia

- `references/gap-taxonomy.md` — taxonomía completa de 14 familias con scoring
- `references/methodology_research.md` — investigación metodológica completa (Perplexity)
- `references/perplexity_research_prompt.md` — prompt original de investigación
