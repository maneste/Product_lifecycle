# Product Lifecycle

A template repository for AI-assisted product management — from user research and discovery through PRD generation, flow design, UI specs, and backend specs. Built on [Claude Code](https://claude.ai/code).

## What This Is

This repo provides a structured workflow and a set of Claude Code skills, agents, and commands to take a digital product feature from raw user research to implementation-ready documentation.

Clone and adapt it for any product.

## How It Works

The lifecycle runs through five stages, each powered by a Claude Code tool:

| Stage | Tool | Output |
|-------|------|--------|
| 1. PRD | `prd` skill | Discovery-phase product requirements doc |
| 2. Flow Design | `flow-designer` skill | Mermaid user journey diagram |
| 3. UI Specs | `frontendUIAgent` subagent | UI specifications + Figma prompt |
| 4. Backend Specs | `backendAgent` subagent | API contracts, data models, logic |
| 5. ER Diagram | `er-diagram-generator` subagent | Entity-relationship diagram (optional) |

All outputs are saved to `AI_Output/doc_[Feature_Name]/`.

## Repository Structure

```
Product_lifecycle/
├── .claude/
│   ├── agents/            # Subagents (frontend, backend, ER diagram)
│   ├── commands/          # Slash commands (/update-*, /init-context, etc.)
│   └── skills/            # Interactive skills (prd, flow-designer, etc.)
├── AI_Output/             # Agent-generated docs (version controlled)
│   └── doc_[Feature]/
├── context_knowledge/     # Private knowledge base (gitignored)
├── User_discovery/        # Interview processing scripts (OpenAI pipeline)
├── feature-template/      # Implementation templates
├── Transcriptions/        # Raw transcripts (gitignored, Drive symlink)
└── CLAUDE.md              # Source of truth for all paths & conventions
```

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) installed and authenticated
- OpenAI API key (for `User_discovery` pipeline only)

### 1. Initialize the knowledge base

On first setup, run the init command to create your `context_knowledge/` files interactively:

```
/init-context
```

This creates all knowledge base files in order: product vision, user persona, app flow, opportunity tree, interview summary, benchmark analysis, and notification strategy.

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

### 4. Design the flow

```
/flow-designer
```

Interactive co-design session that produces a Mermaid flow diagram with step-by-step documentation.

### 5. Generate specs

Trigger subagents from the main conversation:

- **UI specs** — ask Claude to run the `frontendUIAgent`
- **Backend specs** — ask Claude to run the `backendAgent`
- **ER diagram** — ask Claude to run the `er-diagram-generator`

## Knowledge Base Commands

Keep context files up to date with individual update commands:

| Command | Updates |
|---------|---------|
| `/update-vision` | Product vision & positioning |
| `/update-persona` | User persona |
| `/update-app-flow` | App journey flowchart |
| `/update-opportunity-tree` | Opportunity framework |
| `/update-interview-summary` | User evidence & quotes |
| `/update-benchmark` | Competitive analysis |
| `/update-notifications` | Notification strategy |

## Skills Reference

| Skill | Trigger | Description |
|-------|---------|-------------|
| `prd` | `/prd` | Interactive PRD generation |
| `flow-designer` | `/flow-designer` | Interactive flow co-design |
| `repo-structure` | automatic | File naming & storage conventions |
| `skill-creator` | `/skill-creator` | Create or update skills |

## Adapting This Template

1. Clone the repo
2. Run `/init-context` to populate `context_knowledge/` for your product
3. Update `CLAUDE.md` if you change any folder names or conventions
4. Add your transcript files to `Transcriptions/transcription_source/`

## License

MIT
