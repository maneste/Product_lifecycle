# Backend Spec Template — Firebase

## Stack Context

- **API paradigm:** Firebase SDK (Firestore + Auth + Cloud Functions)
- **Database:** Firestore (NoSQL, document-collection model)
- **Auth:** Firebase Auth (JWT, Firestore security rules enforce access)
- **Realtime:** Firestore onSnapshot listeners
- **Storage:** Firebase Storage (if file uploads needed)
- **ID format:** Firestore auto-generated document IDs (or custom string IDs)

---

## File 1: `[Feature_Name]_API_Contracts.md`

```markdown
# [Feature Name] — API Contracts (Firebase)

## Authentication
All Firestore operations use Firebase Auth. Security rules enforce that users can only access their own documents.
Auth token is handled automatically by the Firebase SDK.

## Data Operations

### [N]. [Operation Name]
**Purpose:** [Why the frontend needs this]

**Operation type:** Read | Write | Query | Realtime listener | Cloud Function call

**Firebase call:**
```typescript
// Example read:
const docRef = doc(db, 'collection', documentId)
const docSnap = await getDoc(docRef)

// Example query:
const q = query(
  collection(db, 'collection'),
  where('userId', '==', userId),
  orderBy('createdAt', 'desc')
)
const querySnapshot = await getDocs(q)
```

**Frontend Sends:**
- [Parameter]: [type] — [description]

**Data Shape Returned:**
```typescript
{
  id: string        // Firestore document ID
  field: type       // description
  createdAt: Timestamp
  updatedAt: Timestamp
}
```

**Frontend Uses This For:**
- [How the data is used in the UI]

**Security Rule Required:**
- [Describe the Firestore security rule needed]

---

## Realtime Listeners (if applicable)

### [N]. [Listener Name]
**Purpose:** [Why real-time updates are needed]

**Firebase listener:**
```typescript
const unsubscribe = onSnapshot(
  query(collection(db, 'collection'), where('userId', '==', userId)),
  (snapshot) => {
    snapshot.docChanges().forEach((change) => {
      // handle added/modified/removed
    })
  }
)
```

---

## Cloud Functions (complex logic only)

### [N]. [Function Name]
**Purpose:** [Why this can't be a simple Firestore operation]
**Trigger:** HTTP call | Firestore trigger | Auth trigger | Scheduled
**Input:** [schema]
**Output:** [schema]
```

---

## File 2: `[Feature_Name]_DB_Schema.md`

*(Firestore is schemaless — document structure instead of SQL)*

```markdown
# [Feature Name] — Firestore Structure

## Collections

### `[collection_name]`
**Path:** `/[collection_name]/{documentId}`
**Document ID:** Auto-generated | [field]-based

**Document shape:**
```typescript
{
  userId: string          // Firebase Auth UID — always present for RLS
  field: type             // description
  nestedObject: {
    field: type
  }
  createdAt: Timestamp    // serverTimestamp()
  updatedAt: Timestamp    // serverTimestamp()
}
```

**Indexes required:**
- Composite index: `userId ASC, [field] DESC` — needed for [query description]

**Subcollections (if any):**
- `[collection_name]/{id}/[subcollection]` — [purpose]

---

## Security Rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /[collection_name]/{documentId} {
      allow read: if request.auth != null && request.auth.uid == resource.data.userId;
      allow create: if request.auth != null && request.auth.uid == request.resource.data.userId;
      allow update: if request.auth != null && request.auth.uid == resource.data.userId;
      allow delete: if request.auth != null && request.auth.uid == resource.data.userId;
    }
  }
}
```
```

---

## File 3: `[Feature_Name]_Backend_Logic.md`

```markdown
# [Feature Name] — Backend Logic (Firebase)

## Business Rules
[Rules enforced via Cloud Functions, security rules, or client-side validation]

## Cloud Functions
| Function | Trigger | Purpose |
|----------|---------|---------|

## Scheduled Jobs (Cloud Scheduler)
| Job | Schedule | Purpose |
|-----|----------|---------|

## Storage Buckets (if applicable)
| Path | Purpose | Access rule |
|------|---------|------------|

## Realtime Listeners
| Collection | Event | Purpose |
|------------|-------|---------|

## Data Denormalization
[Document any intentional data duplication for query performance]
```
