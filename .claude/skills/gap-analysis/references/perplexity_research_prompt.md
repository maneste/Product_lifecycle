# Perplexity Research Prompt — Gap Analysis Methodology

Usa este prompt en Perplexity antes de implementar el skill de gap analysis.
El objetivo es obtener la base metodológica más sólida posible para construir
una herramienta que ayude al PM a descubrir lo que no sabe antes de investigar.

---

## CONTEXTO PARA EL PROMPT

Este prompt asume conocimiento de los siguientes frameworks como punto de partida:

- **Mom Test** (Rob Fitzpatrick): las preguntas de research no pueden ser respondidas
  con falsedades. Foco en comportamiento pasado observable, no en opiniones ni hipótesis.
- **Quality Guard** (Mercadona Tech): validación del PRD en 3 dimensiones
  (completitud del problema, calidad del proceso AS-IS/TO-BE, contaminación de solución).
  Veredictos: PASS ≥7.0 / CONDITIONAL 5.0–6.99 / FAIL <5.0.
- **Research Mom Test** (Mercadona Tech): gap detection en 3 categorías
  (Process Functional gaps, Process Inventory gaps, User Context gaps),
  seguido de generación de guión de entrevista y JTBDs enriquecidos.
- **Teresa Torres** (Continuous Discovery Habits): opportunity mapping como
  framework estratégico para organizar el espacio de problemas del usuario.
- **JTBD enriquecido**: Job Performer + trigger + struggle (con citas) +
  outcome + dimensión funcional / emocional / social + ansiedades.

---

## PROMPT

```
I'm designing an AI-assisted Gap Analysis tool for Product Managers. The tool
analyzes a PRD (Product Requirements Document) and surfaces what the team
doesn't know yet — so the PM can decide what to investigate before (or after)
writing the PRD, and with whom (internal stakeholders vs. real users).

I already have two reference frameworks in mind:

1. The Mercadona Tech "Quality Guard" module, which evaluates PRDs across:
   - Problem completeness (quantitative metrics + field observations + impact articulation)
   - Process quality (AS-IS mapping, TO-BE mapping, actor identification)
   - Solution contamination (5 antipatterns: embedded JTBDs, technical prescriptions,
     UI/UX specs, solution language, hypothesis-based requirements)

2. The Mercadona Tech "Research Mom Test" module, which detects gaps across:
   - Process Functional (PF) gaps: missing current operation details
     (frequency, duration, constraints, failure modes)
   - Process Inventory (PI) gaps: incomplete understanding of affected areas/sections
   - User Context gaps: unknown workarounds, frustrations, previous attempts, triggers

I want to go deeper and build the most rigorous and practical version of this.
Please research and answer the following:

---

**QUESTION 1 — Complete gap taxonomy for product PRDs**

The Mercadona framework identifies 3 gap categories. I've seen references to
"14 types of gaps" in some PM frameworks. What is the most complete and
well-sourced taxonomy of knowledge gaps that can exist in a PRD?

I need:
- Each gap type with a clear name, definition, and 1-2 examples
- Classification: does this gap require internal stakeholder resolution
  (legal, ops, engineering, finance) OR external user research?
- Severity heuristics: when is each gap type critical vs. refinement?

Reference frameworks to consider beyond Mercadona:
- Assumption Mapping (Jeff Patton / David Bland — "Testing Business Ideas")
- Hypothesis-driven development (Lean UX, Gothelf & Seiden)
- The "Riskiest Assumption Test" (RAT) concept
- Discovery vs. delivery uncertainty (Marty Cagan / Shreyas Doshi)
- Desirability / Feasibility / Viability triangle (IDEO/d.school)

---

**QUESTION 2 — Scoring knowledge gaps by severity**

The Mercadona Quality Guard uses a 0–10 scale per dimension with
PASS/CONDITIONAL/FAIL thresholds. I want to design a severity scoring
model specifically for gaps (not for overall PRD quality).

What are the best published models for scoring the criticality of a
specific unknown assumption? I'm thinking along these axes:
- How much does not knowing this affect the outcome if wrong?
- How confident are we right now (evidence level)?
- How hard/expensive is it to resolve?
- Does resolving it require blocking work, or can it run in parallel?

Are there scoring rubrics or matrices from product research that combine
these dimensions into a simple rating like: CRITICAL / MAJOR / MINOR / REFINEMENT?

---

**QUESTION 3 — The PM as knowledge discovery assistant**

This is the most important design question. The tool should not just list gaps
— it should help the PM discover what they don't know they don't know
(unknown unknowns).

What techniques exist for surfacing unknown unknowns in product development
before user interviews are designed? I'm interested in:

- Pre-mortem applied to research plans (not just to products)
- "What would have to be true?" technique (Roger Martin / strategy consulting)
- Assumption inversion: deliberately listing what the PRD assumes to be true,
  then asking what happens if each assumption is false
- Red teaming / devil's advocate applied to product hypotheses
- "Five Whys" reverse: starting from the proposed solution and tracing back to
  the assumed problem
- Jobs-to-be-Done lens: what job is the PRD assuming users have? Is that stated
  explicitly or implicitly?

What does current AI-assisted research show about systematically uncovering
unknown unknowns in product and UX contexts (2022–2025)?

---

**QUESTION 4 — Connecting gap detection to interview design (Mom Test)**

Once gaps are identified and scored, the next step is translating each gap
into a non-leading, behaviorally-focused interview question following
Rob Fitzpatrick's Mom Test principles:
- Talk about their life, not your PRD
- Ask about the past (specific events), not opinions
- Listen more, talk less — never confirm your own hypothesis

What published work exists on the systematic translation from "knowledge gap"
to "research instrument"? Specifically:
- How do you convert a User Context gap into a Mom Test question?
- How do you convert a Process Functional gap into a field observation protocol?
- Are there templates or decision trees for this translation?
- What anti-patterns in interview design are most correlated with confirmation
  bias in product research?

---

**QUESTION 5 — Discover Mode vs. Validate Mode**

The Mercadona framework distinguishes two research modes:
- Discover: open exploration, no prior hypotheses, user shapes the inquiry
- Validate: hypothesis testing, with strict anti-bias rules (never mention,
  suggest, or hint at the hypotheses during the interview)

What is the published research or practitioner consensus on when to use each
mode? How do practitioners decide which mode to apply based on the existing
evidence in a PRD? Is there a decision framework or rubric?

Also: what are the documented failure modes when Validate mode is applied
incorrectly (i.e., the researcher inadvertently confirms rather than tests)?

---

**QUESTION 6 — JTBD enrichment from research evidence**

The final output I want to produce is enriched JTBDs with this structure:
- Job Performer (specific who, with specific context)
- Trigger (what situation activates the need)
- Struggle (what's hard, with literal user quotes)
- Desired outcome
- Functional motivation (what task they want to complete)
- Emotional motivation (how they want to feel)
- Social motivation (how they want to be perceived)
- Anxieties and barriers

What is the most rigorous methodology for constructing JTBDs from qualitative
interview evidence? Specifically:
- How do you distinguish a real JTBD from a researcher's interpretation?
- What level of evidence (number of quotes, number of interviews) validates a JTBD?
- How do you handle conflicting evidence across interviews?
- What's the connection between Teresa Torres' opportunity nodes and JTBDs?
  (Are they the same abstraction level, or is JTBD more tactical?)

Please provide concrete examples, practitioner sources (2020–2025), and
any AI-assisted workflows that exist for JTBD synthesis from interview data.
```

---

## Qué hacer con las respuestas

Una vez tengas los resultados de Perplexity, úsalos para alimentar estos artefactos:

| Respuesta a pregunta | Alimenta |
|---------------------|----------|
| Q1 — Taxonomía completa | `gap-taxonomy.md` — la clasificación core del skill |
| Q2 — Scoring de severidad | Lógica de puntuación del skill `gap-analysis` |
| Q3 — Descubrimiento de unknown unknowns | El prompt del asistente interactivo (la pieza más valiosa) |
| Q4 — Gap → pregunta de entrevista | Skill futuro `interview-script` (#2 del roadmap) |
| Q5 — Discover vs. Validate | Skill futuro `interview-script` + modos operativos (#3 del roadmap) |
| Q6 — JTBDs desde evidencia | Pipeline de análisis post-entrevista (#5 del roadmap) |

El más crítico para este repositorio es **Q3** — el PM como asistente de descubrimiento.
El valor diferencial no está en listar gaps conocidos, sino en destapar lo que
el PM no sabe que no sabe.
