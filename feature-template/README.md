# Feature Template

A starter template for building new product features using the shared-agents library.

## Quick Start

1. **Clone this template**
   ```bash
   gh repo create your-org/feature-<your-name> --template your-org/feature-template
   cd feature-<your-name>
   ```

2. **Add shared-agents dependency**
   ```bash
   git submodule add -b v1.0.0 https://github.com/your-org/shared-agents.git
   npm install
   ```

3. **Define your idea**
   ```bash
   # Edit docs/context.md with your feature idea
   vim docs/context.md
   ```

4. **Run agent pipeline**
   ```bash
   npm run agent:pipeline
   # This runs: user-research → prd → design → architecture
   ```

5. **Build and deploy**
   ```bash
   npm run build
   npm run deploy
   ```

## What's Included

### Directory Structure

```
feature-template/
├── docs/              # Documentation and context
│   ├── context.md     # Feature context and requirements
│   └── README.md
├── data/              # Data and artifacts
│   ├── raw/           # Raw input data
│   ├── processed/     # Agent outputs (JSON)
│   ├── schemas/       # Database schemas, API specs
│   └── reference/     # Reference materials
├── prompts/           # Feature-specific prompts
│   ├── current/       # Active prompts
│   ├── templates/     # Prompt templates
│   ├── snippets/      # Reusable prompt fragments
│   └── versions/      # Historical prompt versions
├── src/               # Source code
│   ├── frontend/      # Frontend code
│   ├── backend/       # Backend code
│   └── infra/         # Infrastructure as code
├── tests/             # Test files
├── cloud.md           # Complete setup and usage guide
└── README.md          # This file
```

### Agent Workflow

This template uses the shared-agents library to generate:

1. **User Research** → `data/processed/user-research.json`
2. **PRD** → `data/processed/prd.json` + `docs/prd.md`
3. **Design Specs** → `data/processed/design-specs.json`
4. **Tech Architecture** → `data/processed/tech-architecture.json`

See [cloud.md](./cloud.md) for detailed workflow instructions.

## Key Files

- **cloud.md** - Complete guide for building features with Cloud Code
- **docs/context.md** - Your feature's problem statement and goals
- **data/processed/** - AI-generated artifacts from agents
- **src/** - Your implementation code

## Development

### Install Dependencies

```bash
npm install
```

### Run Agent Pipeline

```bash
# Run all agents in sequence
npm run agent:pipeline

# Or run individually
npm run agent:research
npm run agent:prd
npm run agent:design
npm run agent:architecture
```

### Build

```bash
npm run build
```

### Test

```bash
npm test                # All tests
npm run test:unit       # Unit tests only
npm run test:integration # Integration tests
npm run test:e2e        # End-to-end tests
```

### Deploy

```bash
npm run deploy:staging      # Deploy to staging
npm run deploy:production   # Deploy to production
```

## Environment Variables

Create a `.env` file:

```bash
# AI Provider
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Database (example)
DATABASE_URL=postgresql://...

# Cloud Provider (example)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

## Shared Agents Version

This template uses:
- **shared-agents**: v1.0.0

To update:
```bash
cd shared-agents
git fetch --tags
git checkout v1.1.0
cd ..
git add shared-agents
git commit -m "Update shared-agents to v1.1.0"
```

## Workflow

1. **Define** → Write `docs/context.md`
2. **Research** → Run user research agent
3. **Plan** → Run PRD agent
4. **Design** → Run product designer agent
5. **Architect** → Run tech architecture agent
6. **Implement** → Write code in `src/`
7. **Test** → Write tests, ensure coverage
8. **Deploy** → Ship to staging, then production
9. **Iterate** → Update based on feedback

## Examples

### Healthcare Appointment Reminders

```typescript
// docs/context.md
{
  "problemStatement": "Healthcare practices lose 15-30% revenue to no-shows",
  "targetUsers": "Small healthcare practice administrators",
  "businessGoals": ["Reduce no-shows by 40%", "Improve patient experience"],
  "constraints": {
    "timeline": "3 months to MVP",
    "budget": "$50K",
    "technical": "Must integrate with EMR systems, HIPAA compliant"
  }
}
```

Run agents:
```bash
npm run agent:pipeline
```

Outputs:
- User personas (Practice Admin, Front Desk Staff, Patients)
- PRD with features (SMS reminders, confirmation links, rescheduling)
- Design specs (user flows, screens, components)
- Tech architecture (Serverless AWS, DynamoDB, SNS for SMS)

## Versioning

### Prompt Versioning

When you update prompts:

```bash
# Version the current prompt
cp prompts/current/my-prompt.md prompts/versions/v1.0/my-prompt.md

# Update the prompt
vim prompts/current/my-prompt.md

# Commit
git add prompts/
git commit -m "Update my-prompt to v1.1"
```

### Agent Output Versioning

Agent outputs are automatically timestamped. Archive old outputs:

```bash
mkdir -p data/processed/archive/2025-10
mv data/processed/*.json data/processed/archive/2025-10/
```

## Troubleshooting

**Problem**: Agents produce generic outputs
**Solution**: Add more specific context in `docs/context.md`

**Problem**: Agent fails with error
**Solution**: Check API keys, rate limits, and agent version compatibility

**Problem**: Outputs don't match expectations
**Solution**: Customize prompts in `prompts/templates/` and re-run

## Contributing

See [shared-agents contribution guide](../shared-agents/docs/contribution.md)

## License

[Your License]

## Support

- [Cloud Code Guide](./cloud.md)
- [Shared Agents Docs](../shared-agents/README.md)
- [Agent Workflow](../shared-agents/docs/workflow.md)

## Next Steps

1. Read [cloud.md](./cloud.md) for complete setup instructions
2. Define your feature in `docs/context.md`
3. Run the agent pipeline
4. Start building!
