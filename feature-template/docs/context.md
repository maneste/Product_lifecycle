# Feature Context

This document defines the context and requirements for this feature. Fill this out before running the agent pipeline.

## Problem Statement

**What problem are we solving?**

[Clear, concise description of the problem or opportunity. Include:
- Who experiences this problem?
- How severe is it?
- What's the current situation?
- Why does this problem exist?]

Example:
> Small healthcare practices lose 15-30% of potential revenue due to patient no-shows. Practice administrators spend 2+ hours daily making manual reminder calls, which is inefficient and often ineffective. Patients forget appointments because they lack convenient reminder systems, and rescheduling is difficult.

## Target Users

**Who will use this feature?**

### Primary Users
- [User type 1]: [Description, demographics, behaviors]
- [User type 2]: [Description, demographics, behaviors]

### Secondary Users
- [User type 3]: [Description, role]

Example:
> **Primary Users:**
> - Practice Administrators: Age 30-50, manage scheduling for 1-10 doctor practices, tech-comfortable but not technical, value efficiency
> - Front Desk Staff: Age 25-45, handle patient interactions, need simple tools
>
> **Secondary Users:**
> - Patients: All ages, varying tech comfort, want convenience

## Business Goals

**What does the business hope to achieve?**

1. [Goal 1 - be specific and measurable]
2. [Goal 2 - include timeframe if relevant]
3. [Goal 3 - tie to business metrics]

Example:
> 1. Reduce patient no-show rates from 20% to 12% within 6 months
> 2. Reduce administrative time spent on reminders by 80%
> 3. Improve patient satisfaction scores by 15 points
> 4. Increase practice revenue by $50K annually per practice

## Success Metrics

**How will we measure success?**

| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|-------------------|
| [Metric 1] | [Current value] | [Target value] | [How to measure] |
| [Metric 2] | [Current value] | [Target value] | [How to measure] |

Example:
| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|-------------------|
| No-show rate | 20% | 12% | (No-shows / Total appointments) × 100 |
| Admin time on reminders | 2 hrs/day | 15 min/day | Time tracking logs |
| Patient satisfaction | 3.5/5 | 4.2/5 | Post-appointment surveys |

## Constraints

**What limitations or requirements do we have?**

### Timeline
- [Timeframe for MVP]
- [Timeframe for full launch]

### Budget
- [Development budget]
- [Ongoing operational costs]

### Technical Constraints
- [Required technologies]
- [Must integrate with X]
- [Performance requirements]
- [Compliance requirements]

### Resource Constraints
- [Team size and skills]
- [Available time]

Example:
> **Timeline:**
> - MVP in 3 months
> - Full launch in 6 months
>
> **Budget:**
> - $50K development budget
> - Max $500/month operational costs initially
>
> **Technical:**
> - Must integrate with existing EMR systems (eClinicalWorks, Epic) via REST APIs
> - HIPAA compliance required
> - Must support 10K appointments/month initially
> - API response time < 200ms
>
> **Resources:**
> - 2 full-stack developers
> - 1 designer (part-time)
> - Existing AWS infrastructure

## Product Vision

**What's the long-term vision?**

[1-2 paragraph description of where this product should be in 2-3 years]

Example:
> Become the default appointment management solution for small healthcare practices. Every appointment is either kept, rescheduled, or cancelled—never missed. Patients love the convenience, practices love the revenue recovery. Eventually expand to other industries (beauty, professional services, etc.).

## Existing Research

**What do we already know?**

- [Existing data point 1]
- [Existing research finding 2]
- [Competitive insight 3]

Example:
> - Industry reports show 15-30% no-show rates are common in small practices
> - SMS reminders reduce no-shows by 25-40% according to studies
> - Competitors (Solutionreach, Weave) exist but are expensive ($300-500/month)
> - Our target practices can't afford enterprise solutions

## Assumptions

**What are we assuming to be true?**

1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

Example:
> 1. Patients have mobile phones and check SMS regularly
> 2. Practices have budget for a low-cost solution ($50-100/month)
> 3. EMR systems have APIs we can integrate with
> 4. Practices are willing to change their reminder process

## Open Questions

**What needs to be answered?**

1. [Question 1]
2. [Question 2]
3. [Question 3]

Example:
> 1. What percentage of target practices use which EMR systems?
> 2. How much are practices currently spending on no-shows?
> 3. What's the patient demographic breakdown (age, tech comfort)?
> 4. Are there regulatory concerns beyond HIPAA?

## Risks

**What could go wrong?**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [How to mitigate] |

Example:
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| EMR integration is harder than expected | Medium | High | Start with 1-2 popular EMRs, build adapters |
| Patients don't respond to SMS | Low | High | Test with pilot practices, offer multiple reminder channels |
| HIPAA compliance delays launch | Medium | Medium | Engage compliance expert early, use compliant infrastructure |

## Competitive Landscape

**Who else is solving this?**

- [Competitor 1]: [Their approach, strengths, weaknesses]
- [Competitor 2]: [Their approach, strengths, weaknesses]

Example:
> - **Solutionreach**: Comprehensive patient engagement platform. Strength: Feature-rich. Weakness: Expensive ($300-500/month), complex setup
> - **Weave**: All-in-one practice management. Strength: Strong brand. Weakness: Expensive, requires hardware
> - **SimplePractice**: Practice management software. Strength: Affordable. Weakness: Limited to mental health practices

## Out of Scope (for MVP)

**What are we explicitly NOT doing in the first version?**

- [Feature or capability 1]
- [Feature or capability 2]

Example:
> - Multi-language support (English only initially)
> - Patient portal or app
> - Billing or payments
> - Integration with more than 2 EMR systems
> - White-labeling for practices

---

## Filled Out? Ready for Agents!

Once this document is complete, run:

```bash
npm run agent:pipeline
```

This will generate:
1. User research insights and personas
2. Detailed PRD with features and requirements
3. Design specifications and user flows
4. Technical architecture and implementation plan
