# Figma Make Instructions - PRD Schema Template

This document provides the complete schema and instructions for creating Product Requirement Documents (PRDs) using Atomic Design principles and structured JSON output.

## Feature Context (WHY & WHO)

Define feature context with the following structure:

```json
"feature_context": {
  "feature_name": "<Feature name>",
  "problem": "<What user / business pain does this solve?>",
  "goal": "<High-level outcome or job-to-be-done>",
  "personas": [
    { "id": "<persona_id>", "role": "<role>", "needs": "<primary need>" }
  ],
  "user_journey": [ "<step 1>", "<step 2>", "…" ],
  "in_scope": [ "<capability A>", "<capability B>" ],
  "out_of_scope": [ "<excluded A>", "<excluded B>" ],
  "success_metrics": {
    "<metric_key>": "<target>",  // e.g. "conversion_rate": "↑10%"
    "…": "…"
  },
  "constraints": [ "<design / legal / tech constraint>", "…" ],
  "acceptance_test_ids": [ "<AT-ID-01>", "<AT-ID-02>", "…" ]
}
```

## UI Component Hierarchy & Naming (Atomic Design)

Define all UI pieces in a 5-level hierarchy using **lowercase_snake_case** IDs.

### Level 1: Atoms (Indivisible Elements)

- `button_<action>` - Example: `button_search`
- `textbox_<purpose>` - Example: `textbox_search_input`
- `dropdown_<purpose>` - Example: `dropdown_category_filter`
- `label_<text>` - Example: `label_no_results`
- `image_<purpose>` - Example: `image_brand_logo`

### Level 2: Molecules (Groups of Atoms)

- `molecule_<name>` - Example: `molecule_search_bar`
  - Contains: `[textbox_search_input, button_search]`
- `molecule_filter_bar`
  - Contains: `[dropdown_category_filter, button_apply_filter]`

### Level 3: Organisms (Groups of Molecules/Atoms)

- `organism_header`
  - Contains: molecules `[molecule_search_bar]`, atoms `[image_brand_logo]`
- `organism_results_list`
  - Contains: molecules `[molecule_result_card]`

### Level 4: Templates (Wireframes Combining Organisms)

- `template_search_page`
  - Contains: organisms `[organism_header, organism_results_list]`

### Level 5: Pages (Final Screens)

- `page_search`
  - Based on: `template_search_page`

## PRD Schema Template Structure

### Root Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "<feature_name_PRD>",
  "type": "object",
  "required": ["screens", "backendSchemas"],
  "properties": {
    "screens": {
      "type": "array",
      "items": { "$ref": "#/definitions/Screen" },
      "description": "All user-facing or admin views."
    },
    "backendSchemas": {
      "type": "array",
      "items": { "$ref": "#/definitions/BackendEntity" },
      "description": "Data models, events, or APIs powering the UI."
    }
  }
}
```

### Screen Definition

```json
"Screen": {
  "type": "object",
  "required": ["id", "description", "kind", "elements", "navigation"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^(button|textbox|dropdown|label|image|molecule|organism|template|page)_[a-z0-9_]+$",
      "description": "Element ID following naming conventions."
    },
    "description": {
      "type": "string",
      "description": "Short purpose statement."
    },
    "kind": {
      "enum": ["screen", "page", "modal"],
      "description": "UI container type."
    },
    "elements": {
      "type": "array",
      "description": "Ordered list of UI components.",
      "items": {
        "type": "object",
        "required": ["id", "role"],
        "properties": {
          "id": { "type": "string", "description": "Element ID (see components)." },
          "role": {
            "enum": ["button", "textbox", "label", "image", "list", "card"],
            "description": "ARIA-style role."
          },
          "label": { "type": "string", "description": "User-visible text." }
        }
      }
    },
    "navigation": {
      "type": "array",
      "description": "Screen-flow edges.",
      "items": {
        "type": "object",
        "required": ["event", "source", "target"],
        "properties": {
          "event": {
            "enum": ["click", "submit", "swipe", "auto"],
            "description": "Gesture or trigger."
          },
          "source": { "type": "string", "description": "Element ID (from components)." },
          "target": { "type": "string", "description": "Destination screen ID." }
        }
      }
    }
  }
}
```

### Backend Entity Definition

```json
"BackendEntity": {
  "type": "object",
  "required": ["id", "title", "description", "fields"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9_]*$",
      "description": "Unique snake-case key."
    },
    "title": { "type": "string", "description": "Human-readable name." },
    "description": { "type": "string", "description": "Why this entity exists." },
    "lifecycle": {
      "type": "object",
      "properties": {
        "createdBy": { "type": "string", "description": "Producer of the entity." },
        "consumedBy": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Downstream consumers."
        }
      }
    },
    "fields": {
      "type": "array",
      "description": "Attributes of the entity.",
      "items": {
        "type": "object",
        "required": ["name", "type"],
        "properties": {
          "name": { "type": "string", "description": "Field name." },
          "type": { "type": "string", "description": "Primitive / composite type." },
          "isRequired": { "type": "boolean", "description": "Whether field is mandatory." },
          "description": { "type": "string", "description": "Field meaning." }
        }
      }
    }
  }
}
```

## Complete Example: "Mark Task as Done" Feature

### Feature Context

```json
{
  "feature_context": {
    "feature_name": "Mark Task as Done on Homepage",
    "problem": "Users lose track of completed tasks and the homepage looks cluttered.",
    "goal": "Let users mark one or many tasks as done directly from the home feed, declutter the list, and surface a completion-feedback banner.",
    "personas": [
      {
        "id": "busy_professional",
        "role": "End-user",
        "needs": "Quickly triage daily tasks between meetings"
      },
      {
        "id": "product_manager",
        "role": "Stakeholder",
        "needs": "Higher daily active completions (DAC) to prove engagement"
      }
    ],
    "user_journey": [
      "User opens the app and lands on /home",
      "Visually scans tasks; toggles one or selects many",
      "Clicks bulk **Mark Done**",
      "Sees success banner; tasks collapse into the archive"
    ],
    "in_scope": [
      "Toggle single task via checkbox-style button",
      "Bulk select and mark multiple tasks",
      "Real-time UI update without page reload",
      "Backend event `task_update_event` for analytics"
    ],
    "out_of_scope": [
      "Editing task details",
      "Creating new tasks",
      "Changing task order"
    ],
    "success_metrics": {
      "daily_active_completions": "↑ 15% within 30 days of launch",
      "latency_ms": "UI updates < 150 ms P95",
      "error_rate": "< 0.5% failed task-update API calls"
    },
    "constraints": [
      "Must work offline-first with local cache",
      "WCAG AA contrast for all buttons and labels",
      "Follow existing atomic-design ID prefixes exactly"
    ],
    "acceptance_test_ids": [
      "AT-DONE-01_single_toggle",
      "AT-DONE-02_bulk_mark",
      "AT-DONE-03_event_emitted"
    ]
  }
}
```

### Component Hierarchy

```json
{
  "components": {
    "atoms": [
      "button_task_done",
      "button_mark_done",
      "label_task_title",
      "label_task_deadline",
      "label_feature_title",
      "label_done_feedback"
    ],
    "molecules": [
      {
        "id": "molecule_tasks_header",
        "contains": ["label_feature_title", "button_mark_done"]
      },
      {
        "id": "molecule_task_row",
        "contains": ["button_task_done", "label_task_title", "label_task_deadline"]
      }
    ],
    "organisms": [
      {
        "id": "organism_tasks_section",
        "contains": { "molecules": ["molecule_tasks_header", "molecule_task_row"] }
      }
    ],
    "templates": [
      {
        "id": "template_home_tasks_section",
        "contains": { "organisms": ["organism_tasks_section"] }
      }
    ],
    "pages": [
      { "id": "page_home", "template": "template_home_tasks_section" }
    ]
  }
}
```

### Output Schema with Implementation

```json
{
  "output-1": {
    "screens": [
      {
        "id": "page_home",
        "description": "Homepage with task list and mark-done controls",
        "kind": "page",
        "elements": [
          { "id": "molecule_tasks_header", "role": "card", "label": "" },
          { "id": "molecule_task_row", "role": "card", "label": "" },
          { "id": "label_done_feedback", "role": "label", "label": "" }
        ],
        "navigation": [
          { "event": "click", "source": "button_task_done", "target": "page_home" },
          { "event": "click", "source": "button_mark_done", "target": "page_home" }
        ]
      }
    ],
    "backendSchemas": [
      {
        "id": "task",
        "title": "Task",
        "description": "Represents a to-do item",
        "fields": [
          { "name": "task_id", "type": "string", "isRequired": true },
          { "name": "title", "type": "string", "isRequired": true },
          { "name": "deadline", "type": "string", "isRequired": false },
          { "name": "is_done", "type": "boolean", "isRequired": true }
        ]
      },
      {
        "id": "task_update_event",
        "title": "Task Update Event",
        "description": "Emitted when a task is marked as done",
        "fields": [
          { "name": "task_id", "type": "string", "isRequired": true },
          { "name": "user_id", "type": "string", "isRequired": true },
          { "name": "timestamp", "type": "string", "isRequired": true }
        ]
      }
    ]
  }
}
```

## Instructions for LLM

1. Under `"components"`, emit an object with these five keys (atoms, molecules, organisms, templates, pages)
2. For `molecules`, `organisms`, and `templates`, use objects that list their `contains` arrays
3. Then generate `"output-1"` where all `elements[].id` and navigation `source`/`target` must reference these IDs verbatim
4. Use the Atomic-design components defined in "components" to name every UI element
5. Exactly reuse those IDs in output-1

## Key Requirements

- **Always use lowercase_snake_case** for all IDs
- **Explicitly list containment** at molecule, organism, and template levels
- **Reference IDs verbatim** in navigation and elements arrays
- **Follow the pattern hierarchy**: atoms → molecules → organisms → templates → pages
- **Include both screens and backendSchemas** in the final output
- **Define lifecycle for backend entities** (createdBy, consumedBy)
- **Specify required fields** for all entities
