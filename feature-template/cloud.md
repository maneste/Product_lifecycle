# Cloud Code Guide: Building New Features

This guide explains how to use this feature template repository in conjunction with the shared-agents library to build new product features from idea to deployment.

## Architecture Overview

This project uses a two-repository architecture:

1. **shared-agents** - Centralized repository of reusable AI agent modules
2. **feature-<name>** - Individual feature repositories (this repo)

```
┌─────────────────────┐
│   shared-agents     │
│  (Agent Modules)    │
│  - user-research    │
│  - prd              │
│  - product-designer │
│  - tech-architecture│
└──────────┬──────────┘
           │ referenced by
           ▼
┌─────────────────────┐
│  feature-<name>     │
│  (Your Feature)     │
│  - Uses agents      │
│  - Implements code  │
│  - Deploys product  │
└─────────────────────┘
```

## Prerequisites

1. **Shared Agents Library**: Ensure you have access to the shared-agents repository
2. **AI API Key**: Anthropic Claude or OpenAI API key
3. **Development Environment**: Node.js 16+, Git, your preferred IDE
4. **Cloud Access**: AWS/GCP/Azure credentials (for deployment)

## Step-by-Step Process for Adding New Functionality

### Step 1: Clone or Fork This Template

```bash
# Option A: Create new repo from template (recommended)
gh repo create your-org/feature-<your-feature-name> --template your-org/feature-template

# Option B: Clone and rename
git clone https://github.com/your-org/feature-template.git feature-<your-feature-name>
cd feature-<your-feature-name>
```

### Step 2: Add Shared Agents as Dependency

**Option A: Git Submodule** (recommended for versioning)
```bash
git submodule add -b v1.0.0 https://github.com/your-org/shared-agents.git shared-agents
git submodule update --init --recursive
```

**Option B: NPM Package** (if published)
```bash
npm install @your-org/shared-agents@1.0.0
```

**Option C: Direct Git Dependency** (package.json)
```json
{
  "dependencies": {
    "@your-org/shared-agents": "git+https://github.com/your-org/shared-agents.git#v1.0.0"
  }
}
```

### Step 3: Define Your Idea in `docs/context.md`

Create a comprehensive context document:

```markdown
# Feature Context

## Problem Statement
[Clear description of the problem you're solving]

## Target Users
[Who will use this feature? Include demographics, behaviors, needs]

## Business Goals
[What does the business hope to achieve?]
- Goal 1
- Goal 2

## Success Metrics
[How will you measure success?]
- Metric 1: Baseline → Target
- Metric 2: Baseline → Target

## Constraints
- Timeline: [e.g., 3 months to MVP]
- Budget: [e.g., $50K development budget]
- Technical: [e.g., Must integrate with X, use Y technology]

## Assumptions
[What are you assuming to be true?]

## Open Questions
[What needs to be answered?]
```

### Step 4: Run Agent Workflow

Execute agents in sequence to generate artifacts:

#### 4.1 User Research Agent

```typescript
// scripts/01-run-user-research.ts
import { UserResearchAgent } from '@your-org/shared-agents/agents/user-research';
import { saveAgentOutput } from '@your-org/shared-agents/utils/commonHelpers';
import context from '../docs/context.json';

const agent = new UserResearchAgent({
  problemStatement: context.problemStatement,
  targetAudience: context.targetUsers,
  businessGoals: context.businessGoals,
  existingResearch: context.existingResearch || ''
});

const result = await agent.run();

// Save outputs
saveAgentOutput(result, 'data/processed/user-research.json');

console.log('User Research Complete!');
console.log('Personas:', result.outputs.personas.length);
console.log('Opportunities:', result.outputs.opportunities.length);
```

Run it:
```bash
npm run agent:research
```

**Review the outputs** in `data/processed/user-research.json` before proceeding.

#### 4.2 PRD Agent

```typescript
// scripts/02-run-prd.ts
import { PRDAgent } from '@your-org/shared-agents/agents/prd';
import { loadAgentOutput, saveAgentOutput } from '@your-org/shared-agents/utils/commonHelpers';
import context from '../docs/context.json';

const userResearch = loadAgentOutput('data/processed/user-research.json');

const agent = new PRDAgent({
  userResearchOutputs: userResearch.outputs,
  productVision: context.productVision,
  businessConstraints: context.constraints.join(', '),
  technicalConstraints: context.technicalConstraints
});

const result = await agent.run();

// Save outputs
saveAgentOutput(result, 'data/processed/prd.json');

// Generate markdown PRD
fs.writeFileSync('docs/prd.md', generatePRDMarkdown(result.outputs));

console.log('PRD Complete!');
console.log('Features:', result.outputs.features.length);
```

Run it:
```bash
npm run agent:prd
```

**Review `docs/prd.md`** and refine if needed.

#### 4.3 Product Designer Agent

```typescript
// scripts/03-run-product-designer.ts
import { ProductDesignerAgent } from '@your-org/shared-agents/agents/product-designer';
import { loadAgentOutput, saveAgentOutput } from '@your-org/shared-agents/utils/commonHelpers';

const prd = loadAgentOutput('data/processed/prd.json');
const userResearch = loadAgentOutput('data/processed/user-research.json');

const agent = new ProductDesignerAgent({
  prdOutputs: prd.outputs,
  userPersonas: userResearch.outputs.personas,
  brandGuidelines: {
    colors: ['#007AFF', '#5856D6'],
    typography: 'Inter, SF Pro'
  },
  designConstraints: 'Mobile-first, WCAG AA compliant, Material Design 3'
});

const result = await agent.run();

// Save outputs
saveAgentOutput(result, 'data/processed/design-specs.json');

// Generate design system tokens
fs.writeFileSync(
  'src/frontend/design-tokens.json',
  JSON.stringify(result.outputs.designSystem, null, 2)
);

console.log('Design Complete!');
console.log('User Flows:', result.outputs.userFlows.length);
console.log('Screens:', result.outputs.screens.length);
```

Run it:
```bash
npm run agent:design
```

**Review design specifications** in `data/processed/design-specs.json`.

#### 4.4 Tech Architecture Agent

```typescript
// scripts/04-run-tech-architecture.ts
import { TechArchitectureAgent } from '@your-org/shared-agents/agents/tech-architecture';
import { loadAgentOutput, saveAgentOutput } from '@your-org/shared-agents/utils/commonHelpers';

const prd = loadAgentOutput('data/processed/prd.json');
const design = loadAgentOutput('data/processed/design-specs.json');

const agent = new TechArchitectureAgent({
  prdOutputs: prd.outputs,
  designOutputs: design.outputs,
  technicalConstraints: 'AWS, Node.js/TypeScript, React, PostgreSQL, integrate with existing API',
  scalabilityRequirements: 'Start with 1K users, scale to 50K in 12 months'
});

const result = await agent.run();

// Save outputs
saveAgentOutput(result, 'data/processed/tech-architecture.json');

// Generate database schema
generateDatabaseSchema(result.outputs.dataModel, 'data/schemas/database-schema.sql');

// Generate API spec
generateOpenAPISpec(result.outputs.apiSpecification, 'docs/api-specification.yaml');

console.log('Architecture Complete!');
console.log('Stack:', result.outputs.technologyStack);
console.log('Estimated Cost:', result.outputs.costs.estimate.total);
```

Run it:
```bash
npm run agent:architecture
```

**Review architecture** in `data/processed/tech-architecture.json`.

### Step 5: Add Feature-Specific Prompts (Optional)

If you need to customize or extend prompts for this feature:

```bash
# Copy template from shared-agents
cp shared-agents/prompts/templates/generic-prd.md prompts/templates/custom-prd.md

# Edit and customize
vim prompts/templates/custom-prd.md
```

Version your prompts:
```bash
# When you update a prompt, copy to versions folder
cp prompts/templates/custom-prd.md prompts/versions/v1.0/custom-prd.md
```

### Step 6: Define Data Schemas

Based on tech architecture outputs, create data schemas:

```sql
-- data/schemas/database-schema.sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE appointments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  scheduled_at TIMESTAMP NOT NULL,
  status VARCHAR(50) DEFAULT 'scheduled',
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Step 7: Implement Code

Now implement the actual feature based on agent outputs:

#### Frontend (`src/frontend/`)
```
src/frontend/
├── components/
├── pages/
├── hooks/
├── utils/
├── design-tokens.json  (from Product Designer Agent)
└── App.tsx
```

#### Backend (`src/backend/`)
```
src/backend/
├── routes/
├── controllers/
├── models/
├── services/
└── server.ts
```

#### Infrastructure (`src/infra/`)
```
src/infra/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── kubernetes/
    └── deployment.yaml
```

### Step 8: Write Tests

```
tests/
├── unit/
│   ├── frontend/
│   └── backend/
├── integration/
└── e2e/
```

### Step 9: Deploy

#### Set up CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy Feature

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Tests
        run: npm test
      - name: Deploy to AWS
        run: npm run deploy
```

#### Deploy Infrastructure

```bash
cd src/infra/terraform
terraform init
terraform plan
terraform apply
```

#### Deploy Application

```bash
npm run build
npm run deploy:staging  # Deploy to staging first
npm run deploy:production  # After validation
```

### Step 10: Maintenance & Updates

#### Upgrading Shared Agents

When a new version of shared-agents is released:

1. **Review Changelog**
   ```bash
   git submodule foreach git fetch --tags
   git submodule foreach git tag -l
   ```

2. **Update to New Version**
   ```bash
   cd shared-agents
   git checkout v1.1.0
   cd ..
   git add shared-agents
   git commit -m "Update shared-agents to v1.1.0"
   ```

3. **Test Compatibility**
   ```bash
   npm test
   npm run agent:pipeline  # Re-run agent workflow
   ```

4. **Deploy Updates**
   ```bash
   npm run deploy:staging
   # Validate
   npm run deploy:production
   ```

#### Updating Prompts

When you update prompt templates:

1. Version the old prompt
2. Update the current prompt
3. Re-run affected agents
4. Test changes
5. Commit with clear message

```bash
cp prompts/current/my-prompt.md prompts/versions/v1.0/my-prompt.md
# Edit prompts/current/my-prompt.md
npm run agent:prd  # Re-run agent
git add prompts/
git commit -m "Update PRD prompt template to v1.1"
```

## Common Workflows

### Quick Prototype (Skip Research)
```bash
npm run agent:prd      # Start with PRD
npm run agent:design
npm run agent:architecture
```

### Research-Only (Validation)
```bash
npm run agent:research
npm run agent:prd
# Stop here, validate before building
```

### Update Existing Feature
```bash
npm run agent:design    # Re-run design with new requirements
npm run agent:architecture
```

## Troubleshooting

### Agent Outputs Are Generic
- **Solution**: Provide more specific context in `docs/context.md`
- Add examples, data, or reference materials

### Agents Fail or Timeout
- **Solution**: Check API keys, rate limits, network
- Reduce complexity or split into smaller tasks

### Outputs Don't Chain Well
- **Solution**: Verify you're using compatible agent versions
- Check that previous agent completed successfully

## Best Practices

1. **Version Everything**: Agents, prompts, outputs
2. **Review Before Proceeding**: Don't auto-run all agents without review
3. **Document Decisions**: Use `docs/` folder extensively
4. **Test Incrementally**: Don't wait until the end to test
5. **Iterate**: Re-run agents as you learn more
6. **Track Costs**: Monitor AI API usage and cloud costs

## Resources

- [Shared Agents Documentation](../shared-agents/README.md)
- [Agent Workflow Guide](../shared-agents/docs/workflow.md)
- [Contribution Guide](../shared-agents/docs/contribution.md)

## Questions?

Open an issue in the shared-agents repository or contact the platform team.

---

**Ready to build?** Start with Step 1 and follow the process!
