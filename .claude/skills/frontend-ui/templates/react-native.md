# Frontend UI Template — React Native

## Platform Context

- **Platform:** Mobile native (iOS + Android)
- **Framework:** React Native
- **Navigation:** React Navigation (Stack, Tab, Modal)
- **Component style:** StyleSheet or styled-components / NativeWind
- **State management:** detect from docs/architecture/ (Redux, Zustand, React Query, etc.)

## Component Naming Conventions

Use `PascalCase` for component files and `lowercase_snake_case` for component IDs in specs.

| Level | Naming | Example |
|-------|--------|---------|
| Atom | `Atom[Name]` | `AtomButton`, `AtomLabel` |
| Molecule | `Molecule[Name]` | `MoleculeCard`, `MoleculeHeader` |
| Organism | `Organism[Name]` | `OrganismEventList` |
| Screen | `Screen[Name]` | `ScreenHome`, `ScreenDetail` |
| Modal | `Modal[Name]` | `ModalConfirmation` |

## Output Structure for `[Feature_Name]_UI_Specs.md`

```
# [Feature Name] — UI Specifications (React Native)

## 1. Feature Context
- Problem
- Goal
- Personas
- Scope (in / out)

## 2. Component Hierarchy
### Atoms
### Molecules
### Organisms
### Screens
### Modals

## 3. Screen Specifications
For each screen:
### [SCN_ID] — [Screen Name]
**Component:** `Screen[Name]`
**Navigation type:** Stack | Tab | Modal
**Entry from:** [list of SCN_ nodes that navigate here]
**Exit to:** [list of SCN_ nodes this screen navigates to]

#### Layout
[Description of visual layout — list structure, scroll behavior, safe area usage]

#### Components
| Component ID | Type | Purpose |
|---|---|---|

#### States
- **Default:** [description]
- **Loading:** [skeleton / spinner approach]
- **Error:** [error handling UI]
- **Empty:** [empty state UI]

#### Interactions
| Gesture/Event | Component | Result |
|---|---|---|

#### Platform Notes
- **iOS:** [any iOS-specific behavior]
- **Android:** [any Android-specific behavior]

#### Accessibility
- Focus order: [list]
- Screen reader: [key announcements]

## 4. Navigation Map
[Describe the navigation stack/tab structure and how screens relate]

## 5. Edge Cases
[List edge cases not covered in individual screen specs]

## 6. Design Tokens Used
[List colors, typography, spacing values applied from the design system]
```

## React Native-Specific Notes

- All touch targets minimum 44×44pt
- Use `ScrollView` or `FlatList` for lists — specify which
- Note `KeyboardAvoidingView` needs for forms
- Specify `statusBarStyle` per screen (light/dark)
- Note any gestures (swipe back, pull-to-refresh, long-press)
- Deep linking: note if any screen needs a deep link URL
