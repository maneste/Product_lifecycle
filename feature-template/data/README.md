# Data Directory

This directory contains all data related to the feature.

## Subdirectories

### `raw/`
Raw, unprocessed data inputs.
- User survey results
- Interview transcripts
- Market research data
- Reference documents
- Any other source data

### `processed/`
Processed outputs from AI agents.

**Agent Outputs:**
- `user-research.json` - From User Research Agent
- `prd.json` - From PRD Agent
- `design-specs.json` - From Product Designer Agent
- `tech-architecture.json` - From Tech Architecture Agent

### `schemas/`
Data models and schemas.
- Database schemas (SQL, NoSQL)
- API specifications (OpenAPI/Swagger)
- Data validation schemas
- Type definitions

**Example:**
```
database-schema.sql
api-specification.yaml
data-models.ts
```

### `reference/`
Reference materials and documentation.
- Competitive analysis documents
- Market research reports
- Technical specifications
- Industry standards
- Existing system documentation

## Usage

1. **Input Phase**: Add raw data to `raw/`
2. **Processing**: Agents save outputs to `processed/`
3. **Schema Definition**: Create schemas in `schemas/`
4. **Reference**: Keep external docs in `reference/`

## .gitignore

Consider which data files should be committed:
- ✅ Commit: Schemas, processed agent outputs
- ❌ Don't commit: Large raw files, sensitive data, temporary files
