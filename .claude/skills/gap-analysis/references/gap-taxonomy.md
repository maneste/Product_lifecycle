# Gap Taxonomy for PRD Analysis

14 gap families. Para cada gap: definición, ejemplos, locus de resolución (quién puede responderlo), y heurísticas de severidad.

Fuentes: Assumption Mapping (Strategyzer), Four Big Risks (Cagan/SVPG), RAT (Lean Startup), Research Mom Test (Mercadona Tech), Teresa Torres (OST), UK GDS riskiest assumptions model.

---

## Categoría A — Gaps de usuario (resolver con research externo)

### 1. Problem Framing Gap
**Definición:** El PRD describe features o soluciones sin articular qué problema de usuario resuelven ni qué outcome produce.
**Ejemplo:** "Construir SSO" sin especificar qué experiencia o métrica de usuario mejora.
**Locus:** Externo (user research para entender el problema real) + Interno (product/strategy para alinear en outcomes).
**Severidad crítica cuando:** El value proposition entero depende de esta claridad.

### 2. Desirability Gap
**Definición:** Incertidumbre sobre si los usuarios realmente quieren la solución o sienten suficientemente el problema subyacente.
**Ejemplo:** Asumir que una feature flagship es atractiva sin evidencia de demanda.
**Locus:** Externo (customer discovery, JTBD, opportunity mapping).
**Severidad crítica cuando:** No hay ninguna evidencia previa de que el problema existe o importa.

### 3. Usability / UX Gap
**Definición:** Falta de comprensión de si los usuarios pueden completar el flujo propuesto sin fricción.
**Ejemplo:** PRD especifica flujos complejos sin evidencia de que el perfil de usuario puede ejecutarlos.
**Locus:** Externo (usability tests, observación contextual) + Interno (heurísticas de diseño).
**Severidad crítica cuando:** El flujo implica comportamientos nuevos o poblaciones con baja alfabetización digital.

### 7. Process Functional (PF) Gap
**Definición:** Faltan detalles sobre cómo funciona el proceso AS-IS: frecuencia, duración, restricciones, excepciones, modos de fallo.
**Ejemplo:** "Los recepcionistas procesan palés" sin saber cuántos palés por turno, tiempo por palé, ni qué pasa en picos de carga.
**Locus:** Externo (field observation, shadowing) + datos internos de operaciones.
**Severidad crítica cuando:** El diseño de la solución cambia radicalmente según estos parámetros operacionales.

### 8. Process Inventory (PI) Gap
**Definición:** Mapa incompleto de qué áreas, pasos o sistemas se ven afectados por el cambio.
**Ejemplo:** PRD lista el almacén pero omite los procesos del proveedor de transporte que también impacta.
**Locus:** Interno (ops, system owners) + Externo (observar procesos adyacentes).
**Severidad crítica cuando:** Un sistema no mapeado puede bloquear o invalidar el diseño.

### 9. User Context Gap
**Definición:** Desconocimiento de los workarounds del usuario, frustraciones pasadas, intentos previos y triggers que activan la necesidad.
**Ejemplo:** No saber qué hace el usuario cuando el sistema está caído, o qué "última gota" provoca una cancelación.
**Locus:** Externo (entrevistas contextuales, JTBD, diary studies).
**Severidad crítica cuando:** El diseño asume un comportamiento de usuario que puede no existir.

### 10. Segment / Persona Gap
**Definición:** Confusión sobre quién es el usuario primario o quién toma la decisión de adopción.
**Ejemplo:** Feature construida para equipos de seguridad pero vendida a analistas de datos.
**Locus:** Externo (segmentation research) + Interno (alineación sobre target audience).
**Severidad crítica cuando:** El mensaje y el diseño son completamente distintos según el segmento real.

### 14. Perception / Communication Gap
**Definición:** Desalineación entre cómo la organización percibe el producto y cómo lo perciben usuarios o mercado.
**Ejemplo:** Marketing dice "simple", los usuarios experimentan complejidad.
**Locus:** Externo (brand research, UX research) + Interno (marketing, product positioning).
**Severidad menor/mayor** generalmente (raramente bloquea el inicio de construcción).

---

## Categoría B — Gaps internos (resolver con stakeholders)

### 4. Feasibility / Technical Gap
**Definición:** Incógnitas sobre si el equipo puede construir o operar la solución con la tecnología, skills e infraestructura disponibles.
**Ejemplo:** Asumir que un modelo ML alcanzará la precisión necesaria sin experimentos previos.
**Locus:** Interno (engineering, data, infra, security, legal/compliance).
**Severidad crítica cuando:** La viabilidad técnica no está demostrada y es condición necesaria para el valor.

### 5. Business Viability Gap
**Definición:** Falta de claridad sobre si la solución es buena para el negocio: unit economics, canal de ventas, compliance, marca.
**Ejemplo:** Sin claridad sobre pricing o costes de adquisición para una feature que aumenta carga operacional.
**Locus:** Interno (finance, strategy, sales, legal, operations).
**Severidad crítica cuando:** La feature puede ser deseable para usuarios pero insostenible para el negocio.

### 6. Ethical / Harm Gap
**Definición:** Potencial de daño no examinado: privacidad, equidad, manipulación, seguridad.
**Ejemplo:** Recoger datos sensibles sin consentimiento explícito ni salvaguardas claras.
**Locus:** Interno (legal, security, ethics) + Externo (investigación de percepción de confianza).
**Severidad crítica siempre** en entornos regulados o cuando afecta datos sensibles.

### 11. Outcome / Metric Gap
**Definición:** Ausencia de métricas de éxito claras o de baseline/target para el problema.
**Ejemplo:** "Aumentar engagement" sin métrica definida, baseline ni objetivo.
**Locus:** Interno (product, analytics, finance) + benchmarking externo si necesario.
**Severidad crítica cuando:** Sin métrica no hay forma de saber si la solución funcionó.

### 12. Requirement Coverage Gap
**Definición:** Definición incompleta de requisitos funcionales y atributos de calidad (performance, security, reliability, accessibility).
**Ejemplo:** Features especificadas pero sin restricciones de fiabilidad ni accesibilidad para flujos críticos.
**Locus:** Interno (product, engineering, security, accessibility).
**Severidad varía** según el atributo de calidad omitido.

### 13. Organizational / Resource Gap
**Definición:** Gaps en recursos, skills o procesos necesarios para entregar o dar soporte al producto.
**Ejemplo:** Lanzar self-service analytics sin capacidad de formación ni soporte.
**Locus:** Interno (leadership, HR, ops, support).
**Severidad mayor** cuando el gap bloquea la adopción post-lanzamiento.

---

## Resumen rápido

| # | Gap | Locus | Severidad típica |
|---|-----|-------|------------------|
| 1 | Problem Framing | Externo + Interno | CRÍTICO |
| 2 | Desirability | Externo | CRÍTICO |
| 3 | Usability/UX | Externo | MAYOR |
| 4 | Feasibility/Technical | Interno | CRÍTICO |
| 5 | Business Viability | Interno | CRÍTICO |
| 6 | Ethical/Harm | Interno | CRÍTICO |
| 7 | Process Functional | Externo | CRÍTICO/MAYOR |
| 8 | Process Inventory | Interno + Externo | MAYOR |
| 9 | User Context | Externo | CRÍTICO/MAYOR |
| 10 | Segment/Persona | Externo | MAYOR |
| 11 | Outcome/Metric | Interno | CRÍTICO |
| 12 | Requirement Coverage | Interno | VARÍA |
| 13 | Organizational/Resource | Interno | MAYOR |
| 14 | Perception/Communication | Externo + Interno | MENOR/MAYOR |

---

## Sistema de scoring de severidad

Basado en el modelo UK Government Digital Service:

```
Risk Score = Impact (1-10) × (10 - Confidence) (1-10)
Rango: 0-100
```

**Umbrales:**
- **CRÍTICO** (≥70): debe resolverse antes de comprometer capacidad de entrega. Bloquea decisiones clave.
- **MAYOR** (40-69): abordar en paralelo al inicio. No bloquea totalmente pero eleva riesgo de retrabajo.
- **MENOR** (15-39): resolver cuando sea posible. No cambia el ROI ni la seguridad.
- **REFINAMIENTO** (<15): optimización post-lanzamiento. Impact bajo + Confidence alta.

**Ajustes:**
- +10 si el gap es **blocking** (no puede resolverse en paralelo con el desarrollo)
- +5 si afecta safety, compliance o ética
- -10 si hay evidencia indirecta razonablemente sólida

---

## Regla de clasificación: ¿stakeholder o usuario?

**Habla con stakeholders internos cuando:**
- El gap es técnico, financiero, legal u organizacional
- La respuesta existe dentro de la organización (datos de ops, decisiones de negocio)
- El gap es sobre procesos internos que el usuario no puede describir mejor que ops

**Habla con usuarios reales cuando:**
- El gap es sobre comportamiento, motivación, contexto o percepción
- La pregunta es "¿lo quieren?" / "¿lo usarían?" / "¿cómo lo hacen hoy?"
- El gap requiere observar comportamiento in situ (PF gaps complejos)

**Ambos cuando:**
- El gap tiene dimensión operacional Y de experiencia de usuario (PI gaps, algunos PF gaps)
- El problema tiene implicaciones de confianza o ética (Ethical gap)
