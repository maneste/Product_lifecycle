# Frontend UI Template — PWA (Progressive Web App)

## Platform Context

- **Platform:** PWA — runs in browser, installable, offline-capable
- **Framework:** Next.js / Vue / React (detect from docs/architecture/)
- **Navigation:** File-based or client-side router + service worker
- **Key constraints:** offline support, installability, push notifications, app-shell model

## Component Naming Conventions

Same as Web App template (`web-app.md`) — use `PascalCase` for components, `lowercase_snake_case` for spec IDs.

## Output Structure for `[Feature_Name]_UI_Specs.md`

Same base structure as `web-app.md`, plus PWA-specific sections below.

```
# [Feature Name] — UI Specifications (PWA)

## 1. Feature Context
[same as web-app]

## 2. Component Hierarchy
[same as web-app]

## 3. Page Specifications
[same as web-app, add PWA-specific notes per page]

For each page, add:
#### Offline Behavior
- **Available offline:** Yes / No / Partial
- **Offline fallback:** [what the user sees when offline]
- **Data sync:** [how data syncs when connection restores]

## 4. PWA-Specific Specifications

### Install Experience
- **Install prompt trigger:** [when/how the install prompt appears]
- **Home screen icon:** [requirements, refer to hq/brand/]
- **Splash screen:** [colors, logo usage]

### Offline Strategy
| Page / Feature | Offline available | Cache strategy |
|---|---|---|
| [SCN_*] | Yes / No | Cache-first / Network-first / Stale-while-revalidate |

### Push Notifications
- **Triggers:** [when notifications are sent for this feature]
- **Permission request:** [when/how to ask for permission]
- **Notification content:** [title, body, action]

### App Shell
- **Shell components:** [what is always cached — nav, layout]
- **Dynamic content:** [what is fetched fresh]

## 5. URL / Routing Map
[same as web-app]

## 6. Edge Cases
[same as web-app, plus offline edge cases]

## 7. Design Tokens Used
[same as web-app]
```

## PWA-Specific Notes

- Specify which pages are available offline
- Note service worker caching strategy per route
- Specify manifest.json additions needed (name, icons, theme_color)
- Note any Web Push API usage
- Specify background sync requirements if data must persist offline
- Minimum installability requirements: HTTPS, manifest, service worker
