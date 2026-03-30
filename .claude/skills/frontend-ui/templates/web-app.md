# Frontend UI Template — Web App

## Platform Context

- **Platform:** Web (desktop-first or responsive)
- **Framework:** Next.js / Vue / React / other (detect from docs/architecture/)
- **Navigation:** File-based routing (Next.js) or client-side router
- **Component style:** CSS Modules / Tailwind / styled-components (detect from docs/architecture/)
- **State management:** detect from docs/architecture/

## Component Naming Conventions

Use `PascalCase` for component files and `lowercase_snake_case` for component IDs in specs.

| Level | Naming | Example |
|-------|--------|---------|
| Atom | `[Name]` | `Button`, `Label`, `Input` |
| Molecule | `[Name]` | `SearchBar`, `CardHeader` |
| Organism | `[Name]` | `EventList`, `NavigationBar` |
| Page | `[Name]Page` | `HomePage`, `DetailPage` |
| Modal / Dialog | `[Name]Dialog` | `ConfirmationDialog` |

## Output Structure for `[Feature_Name]_UI_Specs.md`

```
# [Feature Name] — UI Specifications (Web App)

## 1. Feature Context
- Problem
- Goal
- Personas
- Scope (in / out)

## 2. Component Hierarchy
### Atoms
### Molecules
### Organisms
### Pages
### Dialogs / Modals

## 3. Page Specifications
For each screen:
### [SCN_ID] — [Page Name]
**Route:** `/path/to/page`
**Entry from:** [list of pages/actions that navigate here]
**Exit to:** [list of pages this navigates to]

#### Layout
[Description — grid, sidebar, full-width, max-width container, etc.]

#### Components
| Component ID | Type | Purpose |
|---|---|---|

#### States
- **Default:** [description]
- **Loading:** [skeleton / spinner approach]
- **Error:** [error handling UI]
- **Empty:** [empty state UI]

#### Interactions
| Event | Component | Result |
|---|---|---|

#### Responsive Behavior
| Breakpoint | Layout changes |
|---|---|
| Mobile (<768px) | |
| Tablet (768–1024px) | |
| Desktop (>1024px) | |

#### Accessibility
- ARIA roles / labels: [key elements]
- Keyboard navigation: [tab order, keyboard shortcuts]
- Screen reader: [key announcements]

## 4. URL / Routing Map
[List all routes introduced by this feature]

## 5. Edge Cases
[List edge cases not covered in individual page specs]

## 6. Design Tokens Used
[List colors, typography, spacing values applied from the design system]
```

## Web-Specific Notes

- Specify SEO-relevant pages (meta title, description, OG tags)
- Note any server-side vs client-side rendering requirements
- Specify form validation (client-side only vs server-validated)
- Note any URL params or query string usage
- Specify browser support constraints if known
- Note any print styles if relevant
