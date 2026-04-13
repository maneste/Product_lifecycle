# Product Lifecycle

A template repository for AI-assisted product management — from user research and discovery through PRD generation, flow design, UI specs, and backend specs. Built on [Amp](https://ampcode.com/) (Claude Code).

Clone and adapt it for any digital product.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **AI Agent** | [Amp](https://ampcode.com/) (Claude Code) | Skills, agents, slash commands — the orchestration engine for the entire lifecycle |
| **LLM (agent)** | Claude (Anthropic) | Powers all interactive skills, subagents, and code generation |
| **LLM (research)** | OpenAI API (`gpt-4o-mini`) | Processes and analyzes user interview transcriptions |
| **Scripting** | Python 3 | User Discovery pipeline (`process_interviews.py`, `aggregate_results.py`) |
| **Diagrams** | Mermaid | User journeys, flow diagrams, ER diagrams — all rendered inline by Amp |
| **Knowledge base** | Obsidian (Canvas + Markdown) | Opportunity tree visualization and editing |
| **Template engine** | [Copier](https://copier.readthedocs.io/) | Create derived projects, sync template updates across products |
| **Transcription source** | Google Drive (symlink) | Raw interview transcripts stored externally, linked via `Transcriptions/` |
| **Version control** | Git + GitHub | Repo hosting, template distribution via "Use this template" |

### Python Dependencies

```
openai>=1.0.0
python-dotenv>=1.0.0
```

---

## How It Works

The lifecycle runs through five stages, each powered by an Amp tool:

| Stage | Tool | Output |
|-------|------|--------|
| 1. PRD | `prd` skill | Discovery-phase product requirements doc |
| 2. Flow Design | `flow-designer` skill | Mermaid user journey diagram + step-by-step documentation |
| 3. UI Specs | `frontendUIAgent` subagent | UI specifications + Figma prompt |
| 4. Backend Specs | `backendAgent` subagent | API contracts, data models, logic |
| 5. ER Diagram | `er-diagram-generator` subagent | Entity-relationship diagram (optional) |

All outputs are saved to `AI_Output/doc_[Feature_Name]/`.

### Research Pipeline

Before (or in parallel with) the feature lifecycle, the research pipeline helps the PM prepare, execute, and analyze user research:

```
Gap Analysis → Interview Script → User Interviews → Interview Processing → Aggregated Insights
```

| Step | Tool | What it does |
|------|------|-------------|
| Gap Analysis | `gap-analysis` skill | Identifies knowledge gaps in a PRD; classifies by severity (CRITICAL/MAJOR/MINOR) and locus (stakeholder vs. user research); surfaces unknown unknowns via pre-mortem & assumption inversion |
| Interview Script | `interview-script` skill | Generates a Mom Test–compliant 5-phase interview guide adapted to the specific feature and its gaps; determines Discover vs. Validate mode |
| Interview Processing | `User_discovery/` pipeline | Processes transcripts with OpenAI, validates against opportunity tree, outputs JSON + Markdown per interview |
| Aggregation | `User_discovery/` pipeline | Consolidates all interview outputs into a single summary with evidence counts |
| Opportunity Tree | `opportunity-tree` skill | Manages the Teresa Torres opportunity tree in Obsidian Canvas format |

---

## Repository Structure

```
Product_lifecycle/
├── .claude/
│   ├── agents/                # Subagents (frontend, backend, ER diagram)
│   ├── commands/              # Slash commands (/update-*, /init-context, etc.)
│   └── skills/                # Interactive skills (prd, flow-designer, etc.)
├── docs/
│   ├── product/               # Roadmap, PRDs, PRD drafts, User Discovery
│   ├── architecture/          # Tech stack, DB schema, system design
│   ├── design/                # UI design system, colors, assets
│   └── deployment/            # Local setup, env vars, CI/CD
├── hq/
│   ├── Vision_[Product].md    # Product vision and positioning
│   ├── opportunity_tree.canvas # Opportunity tree (Obsidian Canvas)
│   ├── opportunity_tree.md    # Opportunity tree markdown sync
│   ├── research/              # Benchmark_[Product].json, *_interview_summary.json
│   ├── personas/              # User_persona.md
│   ├── decisions/             # Notifications_Touchpoints.json
│   ├── ideas/                 # Raw brainstorms
│   └── brand/                 # Brand assets
├── docs/product/
│   └── [Product]_App_Flow.md  # Complete user journey flowchart
├── User_discovery/            # Interview processing pipeline (Python + OpenAI)
├── Transcriptions/            # Raw transcripts (gitignored, Google Drive symlink)
├── feature-template/          # Implementation templates
├── RESEARCH_ROADMAP.md        # Planned improvements to the research module
└── CLAUDE.md                  # Source of truth for all paths & conventions
```

---

## Getting Started

### Prerequisites

- [Amp](https://ampcode.com/) (Claude Code) installed and authenticated
- OpenAI API key (for `User_discovery` pipeline only)
- Python 3 (for `User_discovery` pipeline only)
- [Copier](https://copier.readthedocs.io/) ≥ 9 (only if creating derived projects)

### 1. Initialize the knowledge base

On first setup, run the init command to create your knowledge base files interactively:

```
/init-context
```

This creates all files in order across `hq/`, `hq/personas/`, `hq/research/`, `hq/decisions/`, and `docs/product/`: product vision, user persona, app flow, opportunity tree, interview summary, benchmark analysis, and notification strategy.

### 2. Run user research (optional)

Process interview transcripts with OpenAI to validate opportunities:

```bash
cd User_discovery
bin/run
```

See [`User_discovery/README.md`](User_discovery/README.md) for full documentation.

### 3. Generate a PRD

```
/prd
```

The skill reads your knowledge base, asks clarifying questions, and generates a structured PRD saved to `AI_Output/`.

### 4. Analyze gaps (optional)

```
/gap-analysis
```

Identifies what you don't know before committing to design — classifies gaps by severity and recommends Discover vs. Validate research.

### 5. Prepare interview script (optional)

```
/interview-script
```

Generates a Mom Test–compliant interview guide adapted to the specific feature and its gaps.

### 6. Design the flow

```
/flow-designer
```

Interactive co-design session that produces a Mermaid flow diagram with step-by-step documentation.

### 7. Generate specs

Trigger subagents from the main conversation:

- **UI specs** — ask Amp to run the `frontendUIAgent`
- **Backend specs** — ask Amp to run the `backendAgent`
- **ER diagram** — ask Amp to run the `er-diagram-generator`

---

## Knowledge Base Commands

Keep context files up to date with individual update commands:

| Command | Updates |
|---------|---------|
| `/update-vision` | Product vision & positioning |
| `/update-persona` | User persona |
| `/update-app-flow` | App journey flowchart |
| `/update-opportunity-tree` | Opportunity framework (Obsidian Canvas) |
| `/update-interview-summary` | User evidence & quotes |
| `/update-benchmark` | Competitive analysis |
| `/update-notifications` | Notification strategy |

---

## Skills Reference

| Skill | Trigger | Description |
|-------|---------|-------------|
| `prd` | `/prd` | Interactive Discovery-phase PRD generation |
| `gap-analysis` | `/gap-analysis` | PRD gap analysis with severity scoring and unknown-unknown techniques |
| `interview-script` | `/interview-script` | Mom Test–compliant interview guide generation |
| `flow-designer` | `/flow-designer` | Interactive flow co-design with Mermaid diagrams |
| `opportunity-tree` | `/update-opportunity-tree` | Teresa Torres opportunity tree editor (Obsidian Canvas) |
| `repo-structure` | automatic | File naming & storage conventions |
| `release` | `/release` | Template versioning workflow (Product_lifecycle repo only) |

---

## Agents Reference

| Agent | Purpose | Output |
|-------|---------|--------|
| `frontendUIAgent` | UI specifications from PRD + flow | Screen-by-screen UI spec + Figma prompt |
| `backendAgent` | Backend architecture from PRD + flow | API contracts, data models, business logic |
| `er-diagram-generator` | Entity-relationship modeling | Mermaid ER diagram |

---

## Adapting This Template

1. Use GitHub's **"Use this template"** button to create a new repo
2. Run `/init-project` once to set up Copier tracking
3. Run `/init-context` to populate the knowledge base for your product
4. Update `CLAUDE.md` if you change any folder names or conventions
4. Add your transcript files to `Transcriptions/transcription_source/`

### Syncing Template Updates

This repo uses [Copier](https://copier.readthedocs.io/) for template management. Derived projects can pull in improvements:

```bash
copier update   # run from inside the derived project
```

---

## Methodologies Embedded

This template encodes several product management methodologies into its skills:

- **Teresa Torres — Opportunity Solution Trees** → `opportunity-tree` skill
- **Rob Fitzpatrick — The Mom Test** → `interview-script` skill
- **UK GDS Severity Scoring** → `gap-analysis` skill (Risk = Impact × (10 − Confidence))
- **Pre-mortem & Assumption Inversion** → `gap-analysis` skill (unknown unknowns)
- **Roger Martin — "What would have to be true?"** → `gap-analysis` skill
- **Jobs-to-be-Done (JTBD)** → PRD structure and research pipeline

---

## License

MIT
