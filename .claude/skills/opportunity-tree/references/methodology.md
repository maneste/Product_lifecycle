# Opportunity Tree Methodology — Teresa Torres / Continuous Discovery Habits

## What belongs in the tree

Customer needs, pain points, gaps, and unmet desires — framed as:

- "The user/professional needs X"
- "The user cannot do Y today"
- "The user struggles with Z"

These are **opportunities**: situations where a product could create value by solving a real problem or fulfilling a real need.

## What does NOT belong

- Solutions, features, product ideas, implementation details
- "We should build X" or "Add a feature for Y"
- Technical specifications or design choices

These go in a separate solutions layer when the time comes. The tree is discovery-only.

## Pain/Gap labels

Pain points and gaps are useful as **evidence context** on a card (e.g., "Pain: workflow is interrupted"), but the node itself must represent the opportunity, not the solution. The label describes why this is a real problem — the node title frames it as a need.

## Depth guidance

Go as deep as needed to make the opportunity actionable. Stop when drilling further would require knowing the solution.

- Too shallow: "Users need better support" (not actionable)
- Too deep: "Users need a button in the top right of the screen" (requires knowing the solution)
- Right depth: "Users need to complete a task quickly without interrupting their workflow"

## Desired Outcome

One node only. The north star metric that validates the product loop. Not a user need itself — it is the outcome the product exists to create for the business.

Do not add sub-nodes to the Desired Outcome.

## Branching rules

- Opportunity areas should be **meaningfully distinct**. If two areas overlap heavily, consider merging before adding more sub-nodes.
- Each branch inherits a color from its area (see canvas-conventions.md). All sub-nodes under an area share its color.
- Maximum practical depth: 4 levels (area → specific → sub → detail). Beyond that, the opportunities are likely too granular or solution-adjacent.

## Hypotheses vs. validated needs

An opportunity without user research evidence is a hypothesis. In the markdown file (`opportunity_tree.md`), note unvalidated nodes as hypotheses. In the canvas, they can still appear — but the markdown should track evidence status.

Do not block adding a node because it is unvalidated. Block adding a node because it is a solution, not a need.

## Adding new nodes — checklist

Before adding a node, confirm:

1. Is it framed as a need/problem, not a solution/feature?
2. Is it distinct from existing sibling nodes?
3. Is it at the right depth — actionable without requiring a solution?
4. Does it belong under the correct area (correct color branch)?
5. Does it have a unique reference number that follows the existing sequence?
