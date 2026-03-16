# AI-assisted Gap Analysis for Product PRDs: Methodology, Taxonomy, and Research Workflows

## Executive overview

Published frameworks around product discovery, assumption mapping, and UX research do not converge on a single "14-gap" taxonomy for Product Requirements Documents (PRDs). Instead, they cluster around types of product risks, assumptions, and knowledge gaps (e.g., desirability, feasibility, viability, usability, ethical) and around process-level gaps in how teams understand user workflows and contexts. Drawing from these sources and from Mercadona Tech’s Quality Guard and Research Mom Test, a practical taxonomy for PRD gaps can be constructed that combines risk/assumption types with process and context gaps, and that explicitly encodes where each gap must be resolved (internal stakeholders vs. user research).[^1][^2][^3][^4]

Risk-based models such as Assumption Mapping, the Four Big Risks, and the Riskiest Assumption Test (RAT) provide proven ways to score gaps by severity using dimensions such as impact if wrong, current evidence/confidence, and effort/cost to learn, often expressed with simple 2×2 matrices or numeric risk scores. These models can be adapted into an ordinal scale (CRITICAL / MAJOR / MINOR / REFINEMENT) tailored to gap management.[^5][^6][^3][^7][^8][^9]

For unknown unknowns, there is a rich toolbox: pre-mortems, Roger Martin’s "What would have to be true?" reframing, assumption inversion, red-teaming, and JTBD-based opportunity finding all explicitly focus on surfacing hidden assumptions and blind spots before committing to a solution or a research plan. Recent work on AI in UX research and generative AI workflows shows that AI can support this by suggesting overlooked areas (e.g., accessibility), highlighting weakly evidenced assumptions in plans, and mining qualitative data for patterns that humans miss.[^9][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21]

Finally, there is growing practitioner guidance on translating assumptions into research instruments, distinguishing between discover (generative) and validate (evaluative) modes, and synthesizing Jobs-to-Be-Done (JTBD) from interview evidence in a structured, auditable way. This provides a strong methodological base for an AI-assisted gap-analysis stack where PRD gaps drive a pipeline from gap detection → severity scoring → mode selection (Discover vs. Validate) → interview/field protocols → JTBD enrichment.[^22][^23][^24][^25][^26][^27][^28][^29][^30]

***

## Q1 — A practical gap taxonomy for PRDs

### 1.1 What the literature actually offers

General gap-analysis literature talks about performance, resource, profitability, market, and perception gaps at an organizational level, rather than a fine-grained PRD taxonomy. Product-management literature instead focuses on *risk* and *assumption* types: value/desirability, usability, feasibility, and business viability risks, sometimes with ethical and adaptability risks added. Mercadona Tech’s Research Mom Test adds three process-oriented gap types focused on how work is actually done: Process Functional, Process Inventory, and User Context gaps.[^31][^32][^2][^33][^34][^3][^4][^35][^1]

Across these sources, a "complete enough" taxonomy for PRDs is best built by synthesizing: (a) risk/assumption types; (b) operational/process gaps; and (c) organizational/compliance gaps. This section proposes such a taxonomy, indicating whether each gap tends to require internal clarification, external research, or both.

### 1.2 Proposed taxonomy (14 gap families)

The table below groups 14 gap families. Names are synthesized, but each family is grounded in specific risk or gap concepts from the literature.

| # | Gap family | Definition and examples | Resolution locus |
|---|------------|-------------------------|------------------|
| 1 | **Problem framing gap** | Unclear articulation of the user problem, outcome, or opportunity; often visible when the PRD describes features rather than user outcomes or opportunities.[^17][^36][^37] Example: roadmap items described as "build SSO" without stating what user outcome or business metric it serves. | Primarily external (user research) to understand real problems; internal (product/strategy) to align on outcomes. |
| 2 | **Desirability gap** | Uncertainty about whether users actually want the proposed solution or care enough about the underlying problem, corresponding to value/desirability risk.[^3][^38][^33][^39] Example: assuming a flagship feature is compelling without evidence of demand.[^40] | External (customer discovery, JTBD, opportunity mapping). |
| 3 | **Usability / UX gap** | Missing or weak understanding of whether users can figure out how to use the solution, reflected in usability risk.[^3][^38][^25][^28] Example: PRD specifies complex flows without evidence that target users can complete them successfully. | External (usability tests, observational studies); some internal (design heuristics). |
| 4 | **Feasibility / technical gap** | Unknowns about whether the team can build or run the solution with available technology, skills, and infrastructure, corresponding to feasibility assumptions and feasibility risk.[^3][^34][^38][^41] Example: assuming a machine-learning model can achieve needed accuracy without prior experiments. | Internal (engineering, data, infra, security, legal/compliance). |
| 5 | **Business viability gap** | Unclear whether the solution will be good for the business (unit economics, sales channel fit, compliance, brand, etc.), i.e., business viability risk.[^3][^34][^33][^27] Example: no clarity on pricing or acquisition costs for a feature that significantly increases operational load. | Internal (finance, strategy, sales, legal, operations). |
| 6 | **Ethical / harm gap** | Unexamined potential for harm (privacy, fairness, manipulation, safety) in the solution, framed as ethical assumptions.[^1][^34] Example: collecting sensitive user data without explicit consent or clear safeguards. | Internal (legal, security, ethics) plus external (user trust perception research). |
| 7 | **Process Functional (PF) gap** | Missing details about how the current AS-IS process works: frequency, duration, constraints, exceptions, failure modes.[^31] Example: PRD notes "receivers process pallets" but omits pallets per shift, time per pallet, and what happens under peak load.[^31] | External (field observation, shadowing), sometimes supported by internal ops data. |
| 8 | **Process Inventory (PI) gap** | Incomplete map of which areas, steps, or systems are affected by the change, as described in Mercadona’s Process Inventory gaps.[^31] Example: PRD lists warehouse but omits transport provider processes that are also impacted. | Internal (ops, systems owners) and external (observing adjacent processes with partners). |
| 9 | **User Context gap** | Unknown user workarounds, frustrations, past attempts, and triggers that shape behavior, per Research Mom Test.[^31][^39] Example: not knowing what users do when the system is down, or what "last straw" triggers a cancellation. | External (contextual interviews, JTBD, diary studies). |
| 10 | **Segment / persona gap** | Confusion about *who* the primary user or buyer is; often seen when a feature is built for one persona but sold to another.[^40][^39][^42] Example: building compliance features for security teams while marketing to data analysts. | Primarily external (segmentation research), internal alignment on target audience. |
| 11 | **Outcome / metric gap** | Lack of clear success metrics or baseline/target for the problem, which Cagan and others highlight as a common product management failure.[^3][^42][^37] Example: "increase engagement" with no defined metric, baseline, or target. | Internal (product, analytics, finance) with some external benchmarking as needed. |
| 12 | **Requirement coverage gap (functional / non-functional)** | Incomplete definition of functional requirements and quality attributes (performance, security, reliability, accessibility), as distinct from solution UI specs.[^43][^43][^4] Example: specifying features but omitting reliability or accessibility constraints for critical workflows. | Internal (product, engineering, security, accessibility), sometimes external (accessibility or performance tests with users). |
| 13 | **Organizational / resource gap** | Gaps in resources, skills, or processes required to deliver or support the product, corresponding to resource and performance gaps in general gap-analysis literature.[^44][^4][^37] Example: launching self-service analytics without training or support capacity. | Internal (leadership, HR, ops, support). |
| 14 | **Perception / communication gap** | Misalignment between how the organization perceives the product and how users or the market perceive it, analogous to perception gaps in gap-analysis references.[^4][^40][^45] Example: marketing claims "simple" while users find the product complex and confusing. | External (brand and UX research) plus internal (marketing, product positioning).

### 1.3 Severity heuristics for each gap family

Across assumption-mapping and risk frameworks, severity is consistently linked to two key variables: *impact if the assumption is wrong* and *level of evidence/confidence*, sometimes augmented by feasibility/cost to learn. For PRD gaps, severity heuristics can be tailored per gap family:[^6][^3][^35][^7][^8][^5]

- **Critical (must resolve before committing)** when:
  - The gap sits in the "important + low evidence" quadrant of an assumptions map or risk matrix.[^35][^41][^5][^6]
  - Not resolving it could invalidate the overall value proposition or business viability (e.g., major desirability, viability, or feasibility gaps).[^33][^3][^27]
  - It affects safety, compliance, or ethical risk (ethical/harm gap; some process gaps in regulated domains).[^34][^1]
- **Major (address early in parallel)** when:
  - The gap significantly affects usability, UX, or operational performance but is unlikely to kill the initiative outright (e.g., UX gaps, some PF/PI gaps).[^3][^38][^24]
  - Evidence exists but is weak or indirect; further research materially reduces delivery and rework risk.[^41][^39]
- **Minor (can be refined later)** when:
  - The gap relates to secondary segments, edge-case flows, or cosmetic aspects (e.g., perception nuances, secondary persona details) that do not change core ROI or safety.[^25][^26]
- **Refinement (polish)** when:
  - The gap is about optimization (microcopy, fine-grained UX polish, or detailed performance tuning) after major risks are addressed.[^28][^25]

Severity categories in the skill can therefore be derived by combining generic risk scores (see Q2) with per-gap heuristics about how much they influence value, feasibility, and safety.

***

## Q2 — Scoring knowledge gaps by severity

### 2.1 Published models for scoring assumptions and risks

Several practitioner models explicitly score the criticality of assumptions along impact and evidence/confidence dimensions.

- **Assumption Mapping (Strategyzer / Testing Business Ideas)** maps desirability, viability, and feasibility hypotheses on a 2×2: importance (impact) vs. evidence, then focuses on the top-right quadrant: important + low-evidence assumptions.[^5][^6][^35]
- **Assumption mapping variants** in product blogs likewise classify assumptions into desirability, viability, feasibility, usability and plot them on evidence vs. risk or evidence vs. importance matrices, with "risky" assumptions being high-impact, low-evidence points.[^2][^38][^8][^46]
- **Riskiest Assumption Test (RAT)** emphasizes identifying assumptions whose failure would most affect success, using inversion and impact-based prioritization, and can be combined with probability × impact style thinking from classic risk management.[^47][^48][^49][^9]
- **UK Government Digital Service approach** to riskiest assumptions has each team member score assumptions from 0–10 on "impact if wrong" and "confidence" (evidence). Risk score is computed as impact × (10 − confidence), giving a 0–100 scale that explicitly penalizes high-impact, low-confidence assumptions.[^7]
- **Risk matrices** in project and product risk literature rate risks by impact and likelihood and place them into cells that correspond to categories like low/medium/high/critical risk. These can be adapted from generic risks to assumption-centric risks.[^50][^51]
- **Lean UX Hypothesis Prioritization Canvas** and similar tools by Jeff Gothelf use canvases and matrices to prioritize which hypotheses to test first based on the potential value of learning vs. cost of experimentation.[^52][^53][^54]

These models consistently treat *assumption criticality* as a function of:

- Impact on outcome if wrong.
- Current evidence / confidence.
- Sometimes likelihood / probability of being wrong.
- Practical factors like ease, cost, and time required to test.

### 2.2 Axes for a gap-severity model

The axes described in the question align well with existing models:

- **Impact on outcome:** mirrors "importance" or "impact if wrong" in assumption maps and RAT.[^49][^3][^7][^5]
- **Evidence / confidence:** corresponds to evidence level on assumption maps and to confidence scores in the UK GDS example.[^8][^6][^7][^5]
- **Cost to resolve:** present implicitly in discussion of experiment libraries and choosing tests that balance learning value vs. effort in Testing Business Ideas and Lean UX materials.[^53][^52][^5]
- **Dependency / blocking power:** whether other work can proceed while the gap remains; discovery-vs-delivery discussions explicitly tie high uncertainty on value/feasibility to the need for prior discovery before committing delivery capacity.[^42][^27][^37]

### 2.3 From numeric scores to CRITICAL / MAJOR / MINOR / REFINEMENT

Based on these sources, a pragmatic scoring scheme for the skill can be:

1. **Assign base scores to each gap** using:
   - Impact (1–5 or 1–10).
   - Confidence/evidence (1–5 or 1–10).
   - Optionally likelihood (if estimable).
2. **Compute a risk score** similar to UK GDS: Risk = Impact × (MaxConfidence − Confidence). This directly rewards high-impact, low-confidence gaps.[^7]
3. **Adjust for effort and blocking power** by tagging gaps as *blocking* vs. *parallelizable* and considering test cost from experiment libraries.[^52][^5]
4. **Map numeric risk to severity labels** using thresholds inspired by risk-matrix practice:
   - CRITICAL: top decile or above a defined cutoff (e.g., ≥70 on a 0–100 scale) and blocking key decisions.[^50][^7]
   - MAJOR: medium–high scores that merit early testing but may allow some parallel delivery.
   - MINOR: low scores where learning is nice-to-have.
   - REFINEMENT: assumptions and gaps with both low impact and high confidence.

Practitioner materials often emphasize that the *relative* ordering of assumptions matters more than absolute scores; assumption maps and prioritization canvases are designed to visually show which assumptions fall into "test now", "plan later", or "ignore" quadrants. The skill can therefore compute numeric scores but surface categories and sorting to the PM, rather than expose raw formulas.[^35][^41][^8]

***

## Q3 — Techniques to surface unknown unknowns (the PM as discovery assistant)

### 3.1 Pre-mortems applied to research plans

Pre-mortems, popularized by Gary Klein, ask teams to imagine that a project has failed in the future and then work backwards to list all the reasons it failed. Experimental and practitioner accounts report that pre-mortems can increase the number of potential problems identified by around 30 percent compared to standard risk analysis, because the "it already failed" framing gives people psychological permission to voice concerns and counteracts optimism bias and groupthink.[^11][^55][^14][^56]

Applying this to research plans rather than only to products means asking: "It is six months from now and our research plan failed to de-risk the product. Why did that happen?" Potential answers include: talking to the wrong segment, not probing workarounds, ignoring edge contexts, or asking leading questions. These answers directly suggest knowledge-gap categories and areas where unknown unknowns may lurk.

### 3.2 "What would have to be true?" (Roger Martin)

Roger Martin and subsequent commentators describe "What would have to be true for this to be a good idea?" as the most important strategy question, because it shifts discussion from debating current truths to enumerating future-enabling conditions. Instead of asking "Is this PRD correct?", the team lists what would have to be true about customers, competitors, technology, and the organization for the PRD’s solution to succeed, then examines each condition as a hypothesis.[^57][^58][^59][^16]

This technique naturally exposes unknown unknowns by forcing teams to articulate implicit assumptions that otherwise remain tacit—especially around customer behavior, channel viability, and competitive dynamics. These conditions can then feed directly into an assumptions map or gap list for further scoring.[^16][^53]

### 3.3 Assumption inversion, RAT, and red-teaming

- **Assumption inversion** ("what if the opposite were true?") is explicitly recommended as a way to unearth big assumptions for RAT and other risk techniques. Questions such as "What if our audience doesn’t actually feel this pain?" or "What if a competitor already solves this well enough?" prompt teams to consider failure modes they might otherwise ignore.[^47][^9]
- **Riskiest Assumption Test (RAT)** encourages teams to identify the single assumption whose failure would most jeopardize the initiative and test it with minimal effort. The RAT literature emphasises brainstorming potential fail points, then rating them by impact to isolate the true "keystone" unknown.[^48][^49][^9][^47]
- **Red-teaming / devil’s advocate** is less formalized in product practice but is often combined with pre-mortems or RAT: one group constructs a case for why the product or PRD is wrong or harmful, while another defends it, revealing blind spots and overconfidence. Recent AI tools that act as "cognitive bias detectors" or automated red teams apply similar logic by stress-testing reasoning and surfacing where it breaks, again tied to pre-mortem framing.[^55]

### 3.4 Reverse "Five Whys" from solution back to problem

Classic root-cause analysis uses the "Five Whys" to trace from an observed problem back to deeper causes. In product discovery, practitioners also use a reversed pattern: starting from a proposed solution and asking why it exists, recursively, until reaching a user outcome or business need. When this chain stalls at vague or circular justifications (e.g., "because competitors have it"), it reveals that the problem framing and opportunity definition are under-specified and that substantial problem/segment gaps remain.[^27][^42]

### 3.5 JTBD and opportunity mapping for unknown unknowns

Teresa Torres’ opportunity solution tree (OST) proposes starting from an outcome, mapping the opportunity space (unmet needs, pain points, desires), and then mapping solutions and assumption tests under specific opportunities. She explicitly recommends deriving opportunities from generative research and continuously refining them as teams learn more about customers. Jobs-to-Be-Done (JTBD) is described as one effective lens for uncovering these opportunities; in practice, jobs often become top-level opportunities on the OST that are then broken down into smaller, more actionable sub-opportunities.[^17][^36][^18][^60][^61][^20]

Because jobs and opportunities must be grounded in users’ actual progress-making stories (not in product ideas), OST + JTBD force teams to explore parts of the problem space that weren’t considered when the PRD was written (e.g., switching triggers, social anxieties, or post-onboarding struggles), thereby exposing unknown unknowns.

### 3.6 AI-assisted techniques for surfacing unknown unknowns (2022–2025)

Recent studies and practitioner reports highlight several ways in which AI can assist in uncovering unknown unknowns in product and UX contexts:

- **Gap analysis on research plans and protocols:** A 2024 Substack article on generative AI in UX research reports that AI tools, when given research plans or usability-study descriptions, often suggest overlooked areas such as accessibility, edge devices, or diverse user abilities that teams had not planned to investigate. This functions as an automated "gap detector" on research design.[^12]
- **Highlighting under-explored themes in data:** Academic work on AI in UX research notes that AI can help with interpreting and synthesizing large volumes of qualitative data, uncovering patterns that researchers might miss due to time constraints or cognitive overload. This can reveal recurring user struggles or contexts that were not part of the original PRD assumptions.[^10][^15]
- **JTBD + AI workflows:** Practitioners like Brian Rhea and Jose Bermejo demonstrate workflows where LLMs process interview transcripts to extract pain points, desired outcomes, forces of progress, and JTBD candidates, significantly accelerating the discovery of hidden motivations and anxieties. These workflows rely on structured prompts that ask the model to label text segments according to JTBD constructs, making it easier to spot non-obvious patterns across many interviews.[^19][^21]
- **AI-supported pre-mortems and red-teaming:** Tools built around pre-mortem and cognitive-bias detection concepts use AI to propose failure scenarios, cognitive biases, and counter-arguments to human reasoning, functioning as an always-on red-team that surfaces unlikely but high-impact failure modes.[^55]

In aggregate, these approaches suggest that an AI assistant for PRD gap analysis can:

- Parse PRDs to propose implicit assumptions and "what would have to be true" conditions.
- Run a virtual pre-mortem on the PRD or research plan and list plausible failure reasons.
- Cross-check the PRD against known risk categories (desirability, feasibility, viability, usability, ethical) and against Research Mom Test’s PF/PI/User Context gaps.
- Suggest under-explored user segments, contexts, or constraints based on comparable products and themes in prior research data.

***

## Q4 — From gaps to Mom Test–style research instruments

### 4.1 From assumptions/gaps to research questions

Several guides recommend an explicit step of turning assumptions into research questions before designing interviews or tests.

- The UK New South Wales digital service provides a template where teams list their riskiest assumptions in one column and, in a later step, "turn assumptions into research questions" designed to help validate those assumptions with users.[^23]
- UX research guides likewise advocate listing behavioral hypotheses first (e.g., "Users drop out of tutorials because of confusing instructions"), then rewriting them as open-ended, neutral questions about users’ past behavior (e.g., "Tell me about the last time you struggled to follow a tutorial").[^22]
- OpinionX’s critique of assumption mapping notes that many teams directly design questions to "validate or eliminate" each assumption, often without explicitly checking for bias; it recommends greater care in how these questions are framed.[^62]

These sources converge on a pattern:

1. Make assumptions explicit.
2. For each, draft one or more research questions that target user behavior or context, not the solution.
3. Review and refine questions to avoid leading language, hypotheticals, and solution talk.

### 4.2 Applying Mom Test principles

Rob Fitzpatrick’s Mom Test and derivative summaries emphasize three core interviewing principles: talk about the customer’s life, ask about specific past behavior, and avoid hypotheticals or leading questions. Good questions ask about the last time the interviewee did something, what they did, what they used, and what went wrong, rather than whether they like an idea or would buy a feature.[^63][^64][^65][^66]

Systematic translation from gap to Mom Test–compliant question can therefore follow templates such as:

- **User Context gap → interview questions**
  - Gap example: unknown triggers that cause users to seek a workaround.
  - Question templates (from Mom Test–style guidance): "Tell me about the last time you [tried to accomplish X]. What happened?"; "What made you start looking for a different way to do it?"[^64][^65][^29]
- **Desirability gap → interview questions**
  - Gap: uncertain whether the problem is painful enough.
  - Question templates: "Walk me through the last time this was a problem"; "What did you do instead? How often does that happen?"[^67][^64]
- **Segment/persona gap → interview questions**
  - Gap: unclear who actually uses or decides.
  - Question templates: "Who else was involved when you decided to [switch tools / choose this solution]?"; "Who is most affected when this goes wrong?"[^29]

Automating this mapping is largely a matter of:

- Classifying the gap type.
- Selecting a question template family (e.g., "last time story", "workflow walkthrough", "decision journey").
- Filling in domain-specific variables (job, task, artifact) from the PRD.

### 4.3 Process Functional gaps → field observation protocols

Generative-research and ethnographic guidance stresses that process questions are best answered through direct observation and contextual inquiry. For example, EthOS and other UX research platforms describe generative research as exploratory, qualitative, and focused on observing people in their natural context to understand behaviors, workflows, and pain points.[^24][^25][^28]

To translate **Process Functional gaps** into observation protocols, teams can:

- Derive **observation goals** from PF gaps (e.g., "understand what happens when three trucks arrive simultaneously at the dock").[^31]
- Specify **what to watch and capture**: frequency, duration, hand-offs, tools used, error-recovery behavior, and workarounds, as recommended by generative research method descriptions.[^24][^25]
- Add **probe questions** aligned with Mom Test principles, triggered by events rather than asked in the abstract (e.g., "I noticed you did X when that happened—can you walk me through what you were thinking?").[^65][^68]

While there is no single named framework that maps PF gaps to observation protocols, these elements are all present in generative UX research best practices.

### 4.4 Anti-patterns in interview design and confirmation bias

Interview-design anti-patterns strongly associated with confirmation bias include:

- Asking about opinions or hypotheticals instead of past behavior, which Fitzpatrick and others highlight as a central trap in customer discovery.[^63][^64][^65]
- Leading questions that embed the desired answer or frame one option as obviously better, such as "Do you prefer interactive tutorials instead of boring PDFs?", contrasted with neutral alternatives like "How do you like to consume instructions when you need to learn something new?"[^22]
- Talking more about the product idea than about the user’s life, which turns interviews into pitch sessions rather than research, a mistake repeatedly noted in Mom Test summaries and user-research guides.[^39][^65]
- Anchoring on assumptions from prior assumption-mapping sessions without questioning them, which OpinionX argues can "doom" discovery by constraining exploration to pre-selected topics.[^62]

These anti-patterns provide clear negative rules that an AI assistant can enforce when turning gaps into interview questions (e.g., flagging hypothetical language, solution references, and leading adjectives).

***

## Q5 — Discover Mode vs. Validate Mode

### 5.1 Generative vs. evaluative modes in UX and product research

UX and product-research literature commonly distinguishes **generative (exploratory)** research from **evaluative (validatory)** research.[^26][^69][^25][^28][^24]

- Generative research is used early to uncover user needs, behaviors, and motivations, employing methods such as open-ended interviews, ethnographic observation, and diary studies.[^25][^28][^24]
- Evaluative research tests whether solutions work as intended, using methods like usability testing, A/B tests, surveys with closed questions, and analytics analysis.[^26][^28][^25]

These correspond closely to **Discover** (open exploration, user shapes the inquiry) and **Validate** (hypothesis testing) modes in the Mercadona framework.

### 5.2 When practitioners recommend each mode

Several sources provide decision guidance:

- Generative research is recommended when there is high uncertainty about user needs, when entering new domains, or when problem framing is weak; evaluative research is recommended once a concept or design exists and specific hypotheses can be tested.[^28][^24][^25][^26]
- Mind the Product’s discussion of discovery vs. delivery emphasizes that the *degree of uncertainty* along the four big risk types (value, usability, feasibility, business viability) should determine whether to do discovery; high uncertainty on any of these risks indicates the need for discovery work.[^27]
- Marty Cagan’s writings, summarized by commentators, frame **discovery** as answering "Are there real users who want this, and can we design a solution that is valuable, usable, feasible, and viable?", and **delivery** as building the solution after those questions are resolved. This logic maps directly to selecting Discover vs. Validate mode.[^37][^3][^42]

A practical decision rubric for the skill, grounded in these sources, can be:

- Use **Discover mode** when:
  - Problem framing, segment definition, or opportunity space is unclear (problem framing, segment, or User Context gaps).[^36][^17][^27]
  - Desirability or usability risks are high and evidence is weak.[^38][^3][^27]
  - The team is exploring new markets or outcomes, or existing data is anecdotal.
- Use **Validate mode** when:
  - The opportunity and target segment are well-understood, and the PRD encodes a clear hypothesis about a specific solution or behavior change.
  - The goal is to measure whether a chosen solution works (e.g., usability, performance, conversion) within an already-mapped opportunity.[^25][^26][^28]

### 5.3 Failure modes when Validate mode is misapplied

Commonly documented failure modes when teams jump to validation prematurely or apply it incorrectly include:

- **Confirmatory interviewing:** Asking questions that implicitly seek agreement with the proposed solution, a trap highlighted by Fitzpatrick and multiple Mom Test summaries. This results in polite enthusiasm and false positives rather than real evidence.[^64][^65][^63]
- **Testing UI/UX without understanding needs:** Running usability tests or A/B tests on features whose underlying problem or desirability is unvalidated, leading to local optimization around the wrong opportunity.[^42][^28][^25]
- **Over-focusing on delivery metrics:** Cagan and others note that teams often measure outputs (velocity, feature count) instead of outcomes (customer value, business impact) when discovery is under-invested and validation is misapplied as a checkbox exercise.[^3][^37][^42]
- **Sampling the wrong users:** Evaluative tests with non-target users or biased samples can generate misleading "validation"; segmentation and opportunity mapping sources emphasize the importance of aligning research participants with clearly defined target opportunities and segments.[^20][^39][^17]

An AI-assisted tool can mitigate these failure modes by detecting when PRD gaps (e.g., problem framing, desirability, segment gaps) remain large and recommending Discover mode and generative methods instead of Validate mode.

***

## Q6 — JTBD enrichment from qualitative evidence

### 6.1 Methodologies for constructing JTBD from interviews

JTBD research guides and case studies describe a broadly consistent methodology:

1. **Conduct in-depth, story-focused interviews.** JTBD interviews reconstruct a "decision journey" and ask participants to walk through what happened before, during, and after key events (e.g., switching solutions), focusing on triggers, actions, and outcomes rather than preferences.[^70][^71][^29]
2. **Look for key moments and forces of progress.** Analysts review transcripts to identify triggers, frustrations, emotional cues, and decision points, as well as the four forces of progress: push of the situation, pull of a new solution, habits holding back, and anxieties of the new solution.[^72][^30][^29]
3. **Cluster moments across interviews into jobs.** By mapping multiple stories, common jobs emerge (e.g., "get financial clarity at the end of the month"), often grouped by goal, context, or trigger.[^30][^29]
4. **Decompose jobs into functional, emotional, and social dimensions.** Practitioners emphasize capturing what users are trying to accomplish, how they want to feel, and how they want to be perceived.[^73][^30]

This flow directly supports the enriched JTBD structure specified (performer, trigger, struggle with quotes, desired outcome, functional/emotional/social motivations, anxieties and barriers).

### 6.2 Distinguishing real JTBD from researcher interpretation

JTBD practitioners warn against over-interpreting or inferring jobs without sufficient grounding in actual user stories. Guidance includes:

- Treat jobs as **stable progress statements** describing movement from a current to a desired state, derived from repeated patterns in user narratives rather than isolated comments.[^29][^30]
- Use **verbatim quotes and detailed timelines** as evidence, capturing exact phrases and emotional cues, and avoid rewriting them into marketing language.[^70][^72][^29]
- Validate job statements by checking whether they accurately summarize multiple stories and whether participants would recognize them as true to their experience.[^30][^29]

In practice, a "real" JTBD is one that can be traced back to multiple, rich stories with concrete events and quotes—not just a researcher’s conceptual abstraction.

### 6.3 Evidence levels for validating a JTBD

There is no single numeric standard for how many quotes or interviews are required to validate a JTBD, but methodological guidance points to:

- **Pattern repetition across interviews**: JTBD interview guides advocate looking for recurring triggers, anxieties, and desired outcomes across multiple participants and recommend visual mapping to identify clusters.[^29][^30]
- **Saturation-style thinking**: qualitative research practice in JTBD contexts encourages continuing interviews until no substantially new jobs or forces of progress appear, analogous to theoretical saturation in qualitative research.[^71][^29]

A pragmatic rule for the skill, aligned with these sources, is to treat JTBD as *tentative* when based on only one or two stories and as *supported* when the pattern appears across several interviews and multiple, distinct verbatims.

### 6.4 Handling conflicting evidence

When different interviews conflict (e.g., some users seek control while others seek automation), JTBD guidance suggests:

- **Segmenting by context or job performer**: clustering jobs by context (e.g., "small team leaders" vs. "enterprise compliance officers") or trigger can reveal that apparently conflicting desires correspond to different jobs or segments, not noise.[^30][^29]
- **Using the forces-of-progress lens**: what appears as conflict may reflect different forces dominating in different situations (e.g., habits vs. anxieties vs. pull), which should be captured explicitly rather than averaged away.[^72][^29]

An AI-assisted workflow can support this by clustering excerpts by context, performer role, and forces of progress and tagging tensions as alternative jobs or opportunity branches rather than forcing a single narrative.

### 6.5 Relationship between opportunity nodes and JTBD

Teresa Torres notes that Jobs-to-Be-Done is an effective framework for uncovering customer needs, pain points, and desires and that, in organizations using JTBD, jobs often correspond to top-level opportunities in an opportunity solution tree that must later be broken down into more specific sub-opportunities. She also emphasizes that opportunities should emerge from generative research and experience mapping, not from solution brainstorming.[^18][^61][^17][^20]

From this, the relationship can be characterized as:

- JTBD statements often operate **at the same or slightly higher level** as top-level opportunities (e.g., "get peace of mind about cash flow" as an opportunity node).
- Opportunity nodes in an OST can be seen as **JTBD fragments or sub-jobs**, especially when broken down by context or journey phase (e.g., "understand upcoming expenses" as a sub-job).[^17][^18]

The enriched JTBD structure proposed fits neatly as a *rich annotation* for opportunity nodes: performer and trigger specify scope, struggle quotes and anxieties provide evidence, and functional/emotional/social motivations articulate why addressing the opportunity matters.

### 6.6 AI-assisted JTBD synthesis workflows (2022–2025)

Several practitioners and studies describe concrete AI-assisted workflows for JTBD synthesis:

- **AI-powered extraction of JTBD elements from transcripts:** Brian Rhea demonstrates a Colab notebook using OpenAI APIs to process interview transcripts and automatically extract pain points, desired outcomes, forces of progress, and JTBD candidates, driven by a prompt template that instructs the model what to look for.[^19]
- **Notion AI–based JTBD extraction:** Jose Bermejo shows how Notion AI can be configured with custom prompts to auto-fill database properties such as job to be done, pain, and outcome from interview summaries, using syntax rules (e.g., outcomes starting with "maximizing" or "minimizing").[^21]
- **AI in UX research more broadly:** Reports and studies on AI in UX research document increased use of AI for transcription, coding, theme extraction, and mapping user needs into design concepts, noting that AI can significantly reduce the time required to interpret and synthesize qualitative data.[^13][^15][^10][^12]

These workflows typically retain humans in the loop for:

- Reviewing and editing extracted JTBD statements.
- Resolving conflicts and segmenting by context.
- Selecting which jobs become opportunity nodes or PRD-level requirements.

For the skill, this suggests a pipeline where the AI:

1. Tags transcript excerpts with JTBD elements (trigger, struggle, outcome, functional/emotional/social motivations, anxieties).[^21][^19]
2. Clusters these tagged excerpts into candidate jobs and opportunities.[^29][^30]
3. Surfaces enriched JTBD records with evidence links (quotes, interview IDs) and explicit confidence levels based on how many interviews and quotes support each job.[^15][^10]

This pipeline aligns current AI practice with rigorous qualitative methods, making enriched JTBD outputs auditable and directly traceable back to the underlying research.

---

## References

1. [Assumption Testing: Everything You Need to Know to Get Started](https://www.producttalk.org/assumption-testing/) - A regular cadence of assumption testing helps product teams quickly determine which ideas will work ...

2. [What is assumption mapping? Complete guide with examples](https://blog.logrocket.com/product-management/assumption-mapping-guide-examples/) - Assumption mapping enables you to test and validate your assumptions, which helps you de-risk your p...

3. [The Four Big Risks - Silicon Valley Product Group](https://www.svpg.com/four-big-risks/) - In the first edition of my book, INSPIRED, I discussed how successful products are valuable, usable ...

4. [Types Of Gaps In Gap...](https://www.launchnotes.com/glossary/gap-analysis-in-product-management-and-operations) - Learn about Gap Analysis in product management. Explore its methods and how it identifies business p...

5. [Testing Business Ideas](https://catalogimages.wiley.com/images/db/pdf/9781119551447.excerpt.pdf) - Reduce risk and uncertainty of new ideas across your organization. Discover an extensive experiment ...

6. [Breaking Product Discovery into First Principles](https://www.antmurphy.me/newsletter/introduction-to-product-discovery) - For those who aren't faimiliar with assumptions mapping. It's a technique by David J Bland from his ...

7. [Prioritise the riskiest assumptions in big problem spaces](https://services.blog.gov.uk/2022/11/03/prioritise-the-riskiest-assumptions-in-big-problem-spaces/) - The first of two blog posts about how teams can use riskiest assumptions to focus on learning the th...

8. [Assumption mapping: Identifying risks before building your product](https://yourproductmanagement.com/assumption-mapping-identifying-risks-before-building-your-product/) - Discover how assumption mapping helps product teams prioritize risky assumptions, ensuring critical ...

9. [Riskiest Assumption Test - ModelThinkers](https://www.modelthinkers.com/mental-model/riskiest-assumption-test) - Before you launch that product, build that thing, or invest in that idea, you need to think ‘RAT’. A...

10. [ASCILITE 2024](https://open-publishing.org/publications/index.php/APUB/article/download/1341/1520/8614)

11. [The Pre-Mortem: Preventing Product Failure Before It Strikes](https://www.scrum.org/resources/blog/pre-mortem-preventing-product-failure-it-strikes) - This article explains why pre-mortems are a brilliant tool for risk mitigation, improving your team’...

12. [Generative AI in UX Research: Navigating the Promise and ...](https://uxpsychology.substack.com/p/generative-ai-in-ux-research-navigating) - Integrating AI with Traditional UX Research Methods

13. [How AI in UX research is quietly transforming how teams work](https://standardbeagle.com/ai-in-ux-research-transformation/) - Discover how AI in UX research is speeding up transcription, synthesis, and insight discovery, givin...

14. [The Premortem: Your Product's Autopsy Before Launch](https://eleganthack.com/the-premortem-your-products-autopsy-before-launch/) - Most product teams plan for success, which makes sense until you realize that planning only for succ...

15. [[PDF] Embracing AI tools in UX research - Bold Insight](https://boldinsight.com/wp-content/uploads/2024/02/Bold-Insight-Global-AI-Study.pdf)

16. [What Is A Better Model For Formulating Strategy? A Conversation With Roger Martin](https://www.forbes.com/sites/benjaminkomlos/2022/05/02/what-is-a-better-model-for-formulating-strategy-a-conversation-with-roger-martin/) - What’s a better model for formulating strategy? Have a specific problem you want to solve. Make sure...

17. [Summary: Build better products with continuous product discovery | Teresa Torres](https://www.lennyspodcast.com/blog/summary-build-better-products-with-continuous-product-discovery-teresa-torres/) - Build better products with continuous product discovery | Teresa Torres

18. [Mapping - An introductory guide for product teams by Teresa Torres](https://miro.com/blog/mapping-product-teams-teresa-torres/) - Teresa Torres, a product discovery coach, on why visual thinking is one of the most valuable parts o...

19. [JTBD + AI 🤖️ How I use OpenAI to Streamline JTBD Research](https://www.youtube.com/watch?v=eTE4oLLKrlU) - This is how I use AI to pull insights from customer interview transcripts in just a few seconds.

If...

20. [Teresa Torres Answers Your Product Discovery Questions](https://www.mindtheproduct.com/teresa-torres-answers-your-product-discovery-questions/) - Teresa Torres covers how to keep track of your team's discovery efforts, why the process of discover...

21. [Save 10s of hours of Jobs To Be Done Analysis With This AI Prompts](https://www.youtube.com/watch?v=C2dsxXMVv7I) - Have a coffee with me to see if I can help with your JTBD needs 👉 https://cal.com/josebcoach/25-min-...

22. [From hypotheses to actionable insights, a guide to user interviews](https://www.guindo.com/blog/en/ux-insights-user-interviews/) - Learn how to master user interviews for UX design with this complete guide: from hypothesis formulat...

23. [Activity steps](https://www.digital.nsw.gov.au/sites/default/files/2022-11/Template-Generating-research-questions.pdf)

24. [Drawing the line between generative and evaluative research - EthOS](https://ethosapp.com/blog/drawing-the-line-between-generative-and-evaluative-research/) - Generative research is about exploration and understanding, laying the groundwork for new ideas and ...

25. [Generative vs Evaluative Research](https://www.lyssna.com/blog/generative-vs-evaluative-research/) - Understand the key differences between generative and evaluative UX research. Learn when to use each...

26. [Generative vs evaluative research: Choosing the right approach](https://cleverx.com/blog/generative-vs-evaluative-research-choosing-the-right-approach/) - Generative research uncovers user needs early on, guiding design decisions. Evaluative research test...

27. [Product Discovery or Product Delivery: How do you Decide?](https://www.mindtheproduct.com/product-discovery-or-product-delivery-how-do-you-decide/) - What’s the fundamental difference between product discovery and delivery or execution? The degree of...

28. [Generative Vs. Evaluation Research | Research Test Methods](https://www.usertesting.com/blog/generative-vs-evaluation-research) - Generative research delves into understanding user needs and motivations to inspire innovation, eval...

29. [How To Use Jobs To Be Done (JTBD) Interviews To Unlock ...](https://uxarmy.com/blog/jobs-to-be-done-interviews/) - Jobs to be done (JTBD) interviews are a powerful method for uncovering customer needs and driving pr...

30. [How to Investigate Interviews Without Getting Confused? ...](https://www.dashly.io/blog/jtbd/) - Today, we’ll share our experience of how we investigate JTBD interviews and bring insights to the pr...

31. [Research Mom Test: Validación de Problemas contra la Realidad ...](https://www.gemba.es/p/research-mom-test-validacion-de-problemas) - Serie Gemba: AI Mercadona User Story Framework — De PRDs validados a JTBDs con evidencia real

32. [What is Gap Analysis? Steps, Template, Examples](https://www.appinio.com/en/blog/market-research/gap-analysis) - Gap Analysis is a strategic planning tool used to assess the difference, or “gap,” between the curre...

33. [The 4 Types Every Product Manager Must Master - Kaizenko](https://www.kaizenko.com/product-risk-management-the-4-types-every-product-manager-must-master/)

34. [The 5 Types of Assumptions that Underlie Our Ideas - Product Talk](https://www.producttalk.org/five-types-of-assumptions/) - Assumption testing is at the heart of what good continuous discovery teams do week over week. It’s h...

35. [How Assumptions Mapping Can Focus Your Teams On ...](https://www.strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter) - Assumptions Mapping is a team exercise where desirability, viability, and feasibility hypotheses are...

36. [Teresa Torres's Opportunity Solution Tree for Product Discovery](https://www.shortform.com/blog/teresa-torres-opportunity-solution-tree/) - Teresa Torres's Opportunity Solution Tree helps teams maintain laser focus on customer value. Learn ...

37. [Product Discovery in Roadmaps: Why Your Invisible Discovery Work ...](https://blog.roadmap.one/posts/blog9-product-discovery-in-roadmaps/) - Discovery work is invisible in most roadmaps—which is why it gets cut first and costs you most. Here...

38. [4 types of product assumptions and how to test them - LogRocket Blogblog.logrocket.com › product-management › 4-types-of-product-assumpti...](https://blog.logrocket.com/product-management/4-types-of-product-assumptions-how-to-test/) - Understanding, identifying, and testing product assumptions is a cornerstone of product development.

39. [User research product management: Essential guide for PMs](https://cleverx.com/blog/user-research-product-management-essential-guide-for-pms) - Define clear research questions together. Product managers know what decisions need evidence. Resear...

40. [How to Find the Product Gaps that are Killing Your Strategy](https://www.productplan.com/learn/how-to-find-product-gaps-that-are-killing-your-strategy/) - Are you ignoring product gaps that might be derailing your strategy? Learn how to develop a process ...

41. [How to use risk and assumption mapping in product discovery](https://dualoop.com/en-be/blog/how-to-risk-assumption-mapping-product-discovery) - We help product organisations transform the way they work through coaching and seasonal experts staf...

42. [Inspired by Marty Cagan: Summary & Notes - Graham Mann](https://grahammann.net/book-notes/inspired-marty-cagan) - The best product teams discover products worth building through continuous experimentation, deep cus...

43. [Product requirements and gap analysis](https://flagshipfintech.com/knowledge-base/product-requirements-and-gap-analysis/) - The gap analysis stage allows you to evaluate the compatibility between your product requirements an...

44. [Conducting requirements and gap analysis in projects](https://blog.sysco.no/business/analysis/Conducting-requirements-and-gap-analysis-in-projects/) - Gaps can be of various kinds, such as compliance gaps, legal gaps, performance gaps, communication g...

45. [AI Sales Teammate for B2B Sellers - Vivun](https://www.vivun.com/se-glossary/product-gap)

46. [Assumption Matrix: Definition, Examples, and Applicationswww.launchnotes.com › glossary › assumption-matrix-in-product-manage...](https://www.launchnotes.com/glossary/assumption-matrix-in-product-management-and-operations) - Learn about Assumption Matrix in product management. Understand its importance and how it supports s...

47. [Riskiest Assumption Test](https://modelthinkers.com/mental-model/riskiest-assumption-test) - Before you launch that product, build that thing, or invest in that idea, you need to think ‘RAT’. A...

48. [Riskiest Assumption Test - Duodeka Venture Builder](https://duodeka.com/venture-building-blog/riskiest-assumption-test-rat/) - The Riskiest Assumption Test (RAT) is a method used by companies or startups to validate the idea fo...

49. [Unveiling the Riskiest Assumption Test (RAT) in Product ...](https://jet.style/articles/review-of-rat) - Discover how the Riskiest Assumption Test (RAT) method can revolutionize your prioritization workflo...

50. [Project risk assessment: example with a risk matrix template](https://bigpicture.one/blog/project-risk-assessment-examples/) - Risk assessment involves measuring the probability and impact of a risk. At this stage, you can use ...

51. [How to Use a Risk Matrix in Project Management](https://projectmanagementacademy.net/resources/blog/risk-matrix/) - The risk matrix tool communicates the overall project risks and supplies information, increasing the...

52. [The Hypothesis Prioritization Canvas - Jeff Gothelf](https://jeffgothelf.com/blog/the-hypothesis-prioritization-canvas/) - If you have several hypotheses, how do you decide where to spend your discovery hours? Which should ...

53. [Innovation at Scale, #9: Testing Your Assumptions](https://innovationatscale.substack.com/p/innovation-at-scale-9-testing-your) - How hypothesis-driven design can accelerate your progress

54. [How to use the Lean UX Canvas - Jeff Gothelf](https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/) - This short video explains how to use the Lean UX canvas.

55. [The Pre-Mortem: Why Imagining Failure Before You ... - OverThinQ](https://overthinq.ai/blog/the-premortem-why-imagining-failure-prevents-it) - AI that detects your cognitive biases, stress-tests your reasoning, and shows you exactly where your...

56. [Use a Pre-Mortem to Identify Project Risks Before They Occur](https://www.mountaingoatsoftware.com/blog/use-a-pre-mortem-to-identify-project-risks-before-they-occur) - Help your team avoid project failures by identifying preventable roadblocks, and the ways you’ll get...

57. [What Would Have to Be True? - Tiffani Bova - Substack](https://tiffanibova1.substack.com/p/what-would-have-to-be-true) - The Most Important Question in Strategy

58. [MarkHowellLive.com | Great Questions: What Would Have to Be True?](https://www.markhowelllive.com/great-questions-what-would-have-to-be-true/) - I love a great question. In fact, I'm kind of a collector of great questions. In a way, great questi...

59. [What Would Have to be True? - Roger L. Martin - Substack](https://rogerlmartin.substack.com/p/2022-08-22_what-would-have-to-be-true-83dac5bd2189html) - The Most Valuable Question in Strategy

60. [Build better products with continuous product discovery | Teresa Torres](https://www.youtube.com/watch?v=9RFaz9ZBXpk) - Teresa Torres is an internationally acclaimed author, speaker, and coach. She teaches a structured a...

61. [Talking Methods: Driving better outcomes with Teresa Torres’ OST](https://www.youtube.com/watch?v=hHzsau3t_zY) - In this episode of "Talking Methods", learn how Teresa Torres' Opportunity Solution Tree (OST) can h...

62. [Assumptions Are Killing Your User Research - OpinionX](https://www.opinionx.co/blog/assumption-mapping) - 75% of new businesses fail and 80% of product features are rarely or never used. The number one reas...

63. [The Mom Test book review](https://www.globalorange.nl/en/knowledge/book-recommendation-the-mom-test/) - In The Mom Test, find out what questions to ask to validate your business plan. By tech entrepreneur...

64. [The Mom Test: How to Conduct Effective User Research? - TianPan.co](https://tianpan.co/notes/2025-04-29-the-mom-test) - The Mom Test provides practical user research techniques, teaching entrepreneurs how to gather genui...

65. [What Is the Mom Test? How to Talk to Customers and Avoid Bias | UXtweak](https://blog.uxtweak.com/the-mom-test/) - The Mom Test exists for a reason: because most of us have been lied to by people who love us. Say yo...

66. [The Mom Test: How to Conduct Effective User Research? - TianPan.co](https://tianpan.co/blog/2025-04-29-the-mom-test) - The Mom Test provides practical user research techniques, teaching entrepreneurs how to gather genui...

67. [Using the Mom Test for idea validation](https://www.reddit.com/r/Entrepreneur/comments/1j5kk3z/using_the_mom_test_for_idea_validation/) - Using the Mom Test for idea validation

68. [50 User Interview Questions: Guide and Examples - Articos](https://www.articos.com/blog/user-interview-questions/) - Discover 50+ proven user interview questions organized by research goal. Includes real question exam...

69. [Generative vs Evaluative UX Research - Ethnio](https://ethn.io/blog/generative_vs_evaluative_research_methods) - For example, a generative research study might identify a new user need, while an evaluative researc...

70. [Customer Interviews: How to Use the Jobs-to-Be-Done Framework](https://cxl.com/blog/customer-interviews/) - Want to get more out of customer interviews? You need a framework to guide the conversation. Find ou...

71. [How to Do Jobs to Be Done Research (JTBD) – Step-by-Step Guide](https://mrx.sivoinsights.com/blog/how-to-conduct-jobs-to-be-done-jtbd-research-a-beginner-s-step-by-step-guide) - Learn how to do Jobs to Be Done research with this simple step-by-step JTBD guide. From interviews t...

72. [Jobs to be Done 101: Your Interviewing Style Primer](https://dscout.com/people-nerds/the-jobs-to-be-done-interviewing-style-understanding-who-users-are-trying-to-become) - Implementing a Jobs to be Done approach helps get to the heart of who your users are—and who they wa...

73. [Revolutionizing B2B: How JTBD and Generative AI Unlock ...](https://emmanuelobadia.com/2025/01/25/revolutionizing-b2b-how-jtbd-and-generative-ai-unlock-customer-success/) - The JTBD framework is more than just theory—it's a tool you can apply today to gain a competitive ed...

