# Backend Spec Template — Supabase

## Stack Context

- **API paradigm:** Supabase client (auto-REST via PostgREST) + Edge Functions for complex logic
- **Database:** PostgreSQL (managed by Supabase)
- **Auth:** Supabase Auth (JWT, RLS policies enforce row-level access)
- **Realtime:** Supabase Realtime (Postgres changes subscription)
- **Storage:** Supabase Storage (if file uploads needed)
- **ID format:** UUID (gen_random_uuid())

---

## File 1: `[Feature_Name]_API_Contracts.md`

```markdown
# [Feature Name] — API Contracts (Supabase)

## Authentication
All queries use Supabase Auth. RLS policies enforce that users can only access their own data.
Auth token is handled automatically by the Supabase client — no manual JWT handling needed.

## Data Operations

### [N]. [Operation Name]
**Purpose:** [Why the frontend needs this]

**Operation type:** Query | Mutation | Realtime subscription | Edge Function

**Supabase call:**
```typescript
// Example:
const { data, error } = await supabase
  .from('table_name')
  .select('field1, field2, related_table(field)')
  .eq('user_id', userId)
```

**Frontend Sends:**
- [Parameter]: [type] — [description]

**Backend Returns:**
```typescript
// Data shape:
{
  field: type // description
}
```

**Frontend Uses This For:**
- [How the response is used in the UI]

**RLS Policy Required:**
- [Describe the row-level security rule needed]

**Errors:**
| Code | Meaning | Frontend Action |
|------|---------|----------------|
| PGRST116 | No rows found | Show empty state |
| 42501 | RLS violation | Show permission error |

---

## Realtime Subscriptions (if applicable)

### [N]. [Subscription Name]
**Purpose:** [Why real-time updates are needed]

**Supabase subscription:**
```typescript
const channel = supabase
  .channel('channel_name')
  .on('postgres_changes',
    { event: '*', schema: 'public', table: 'table_name', filter: 'user_id=eq.{userId}' },
    (payload) => { /* handle */ }
  )
  .subscribe()
```

---

## Edge Functions (complex logic only)

### [N]. [Function Name]
**Purpose:** [Why this can't be a simple query]
**Endpoint:** `POST /functions/v1/[function-name]`
**Input:** [schema]
**Output:** [schema]
```

---

## File 2: `[Feature_Name]_DB_Schema.sql`

```sql
-- =============================================
-- [Feature Name] Schema (Supabase / PostgreSQL)
-- =============================================

CREATE TABLE [table_name] (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    -- [fields]
    created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- RLS
ALTER TABLE [table_name] ENABLE ROW LEVEL SECURITY;

CREATE POLICY "[table_name]_select_own" ON [table_name]
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "[table_name]_insert_own" ON [table_name]
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "[table_name]_update_own" ON [table_name]
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "[table_name]_delete_own" ON [table_name]
    FOR DELETE USING (auth.uid() = user_id);

-- Indexes
CREATE INDEX idx_[table]_user_id ON [table_name](user_id);

-- updated_at trigger (Supabase has moddatetime extension available)
CREATE TRIGGER handle_updated_at BEFORE UPDATE ON [table_name]
    FOR EACH ROW EXECUTE PROCEDURE moddatetime(updated_at);
```

**Supabase-specific rules:**
- Always reference `auth.users(id)` for user foreign keys (not a custom users table)
- Always enable RLS on every table
- Define policies for each operation (SELECT, INSERT, UPDATE, DELETE)
- Use `auth.uid()` in RLS policies for current user
- Prefer PostgREST queries over Edge Functions unless business logic is complex

---

## File 3: `[Feature_Name]_Backend_Logic.md`

```markdown
# [Feature Name] — Backend Logic (Supabase)

## Business Rules
[Rules enforced via RLS policies, CHECK constraints, or Edge Functions]

## State Machines
[If states exist — document transitions and which trigger updates them]

## Database Functions / Triggers
[Any PostgreSQL functions or triggers needed beyond RLS]

## Edge Functions
[Only document if complex logic requires server-side processing beyond queries]

## Storage Buckets (if applicable)
| Bucket | Purpose | Access policy |
|--------|---------|--------------|

## Realtime Channels
| Channel | Table | Events | Purpose |
|---------|-------|--------|---------|
```
