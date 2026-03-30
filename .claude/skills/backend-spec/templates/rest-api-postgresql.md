# Backend Spec Template — REST API + PostgreSQL

## Stack Context

- **API paradigm:** REST (HTTP verbs + JSON)
- **Database:** PostgreSQL
- **Auth:** JWT bearer token (unless docs/architecture/ specifies otherwise)
- **ID format:** UUID (gen_random_uuid())
- **Timestamps:** `TIMESTAMP WITH TIME ZONE`, always include `created_at` + `updated_at`

---

## File 1: `[Feature_Name]_API_Contracts.md`

```markdown
# [Feature Name] — API Contracts

## Authentication
[Describe auth requirement — e.g. "All endpoints require JWT bearer token in Authorization header"]

## Endpoints

### [N]. [Action Name]
**Purpose:** [Why the frontend needs this endpoint]

**Endpoint:** `[METHOD] /[resource]/[path]`

**Frontend Sends:**
- [Parameter/field]: [type] — [description]

**Backend Returns:**
```json
{
  "field": "type — description"
}
```

**Frontend Uses This For:**
- [How the response is used in the UI]

**Errors:**
| Status | Meaning | Frontend Action |
|--------|---------|----------------|
| 400 | [reason] | [what UI should do] |
| 401 | Unauthorized | Redirect to login |
| 404 | Not found | Show not found state |
| 500 | Server error | Show retry option |

---

## Data Models

### [EntityName] (frontend view)
```json
{
  "id": "UUID",
  "field": "type — description"
}
```

---

## Real-Time / Async Patterns
[Describe polling, webhooks, or push notification patterns if needed]
```

---

## File 2: `[Feature_Name]_DB_Schema.sql`

```sql
-- =============================================
-- [Feature Name] Schema
-- =============================================

CREATE TABLE [table_name] (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    -- [fields]
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_[table]_[field] ON [table_name]([field]);

-- updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_[table]_updated_at
    BEFORE UPDATE ON [table_name]
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

**Schema rules:**
- Always UUID primary keys
- Always `created_at` + `updated_at`
- Status fields: use `VARCHAR(50)` with `CHECK` constraint listing valid values
- JSON/flexible data: use `JSONB`
- Foreign keys: always with explicit `ON DELETE` behavior
- Add indexes for: foreign keys, status fields, frequently filtered fields

---

## File 3: `[Feature_Name]_Backend_Logic.md`

```markdown
# [Feature Name] — Backend Logic

## Business Rules
[List rules extracted from PRD — conditions, validations, constraints]

## State Machines
### [Entity] States
| State | Description | Transitions to |
|-------|-------------|----------------|

## Background Jobs
| Job | Schedule | Purpose |
|-----|----------|---------|

## Event Handlers
| Trigger | Handler | Effect |
|---------|---------|--------|

## External Integrations
| Service | Purpose | Integration point |
|---------|---------|------------------|

## Error Handling
[Describe retry logic, fallback behavior, logging strategy]
```
