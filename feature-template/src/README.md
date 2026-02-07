# Source Code Directory

Implementation code for the feature.

## Subdirectories

### `frontend/`
Frontend application code.

**Typical Structure:**
```
frontend/
├── components/       # React/Vue/etc components
├── pages/           # Page components
├── hooks/           # Custom hooks
├── utils/           # Utility functions
├── styles/          # CSS/styling
├── assets/          # Images, fonts, icons
├── api/             # API client code
├── design-tokens.json  # From Product Designer Agent
└── App.tsx          # Main app component
```

**Framework Examples:**
- React: `npx create-react-app frontend --template typescript`
- Next.js: `npx create-next-app frontend --typescript`
- Vue: `npm create vue@latest frontend`

### `backend/`
Backend/API server code.

**Typical Structure:**
```
backend/
├── routes/          # API route handlers
├── controllers/     # Business logic controllers
├── models/          # Data models
├── services/        # Business logic services
├── middleware/      # Express middleware
├── utils/           # Utility functions
├── config/          # Configuration
├── db/              # Database connection/migrations
└── server.ts        # Main server file
```

**Framework Examples:**
- Express: `npm init` + `npm install express`
- NestJS: `npm i -g @nestjs/cli && nest new backend`
- Fastify: `npm install fastify`

### `infra/`
Infrastructure as Code (IaC).

**Typical Structure:**
```
infra/
├── terraform/       # Terraform configurations
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/
├── kubernetes/      # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── docker/          # Dockerfiles
│   ├── Dockerfile.frontend
│   └── Dockerfile.backend
└── scripts/         # Deployment scripts
```

## Getting Started

### Initialize Frontend

```bash
cd src/frontend
npm create vite@latest . -- --template react-ts
npm install
npm run dev
```

### Initialize Backend

```bash
cd src/backend
npm init -y
npm install express typescript @types/node @types/express
npx tsc --init
```

### Create Dockerfile

```bash
cd src/infra/docker
cat > Dockerfile.backend <<EOF
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
EOF
```

## Using Agent Outputs

### Design Tokens (Frontend)

The Product Designer Agent generates design tokens:

```typescript
// src/frontend/design-tokens.json (from agent)
import designTokens from './design-tokens.json';

// Use in your CSS-in-JS or Tailwind config
const theme = {
  colors: designTokens.colors,
  spacing: designTokens.spacing,
  typography: designTokens.typography
};
```

### Database Schema (Backend)

The Tech Architecture Agent generates schemas:

```sql
-- data/schemas/database-schema.sql (from agent)
-- Apply to your database
psql -U postgres -d mydb -f ../../data/schemas/database-schema.sql
```

### API Specification (Backend)

The Tech Architecture Agent generates API specs:

```yaml
# data/schemas/api-specification.yaml (from agent)
# Use for validation, codegen, documentation
```

## Development Workflow

1. **Run agents** → Get design specs and architecture
2. **Review outputs** → Understand what to build
3. **Initialize projects** → Set up frontend/backend/infra
4. **Implement features** → Build according to specs
5. **Test** → Write and run tests
6. **Deploy** → Use infra code to deploy

## Best Practices

- Follow agent-generated architecture decisions
- Use design tokens for consistency
- Implement features as defined in PRD
- Write tests for critical paths
- Document deviations from agent specs
