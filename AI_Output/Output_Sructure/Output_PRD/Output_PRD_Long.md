
Each PRD must follow this structure:

1. **Title & Summary** – concise description of the opportunity or hypothesis.
2. **Background / Context** – reference the Opportunity Tree node (id) and relevant interview evidence.
3. **Problem Statement** – the user or market problem to solve. Describe the opportunities matched from the opportunity_tree.
4. **User Evidence** – quotes or synthesized insights from 20251012_interview_summary.json. Create also a user persona based on user evidence.
5. **Why Now / Strategic Fit** – alignment with Vision Balance and market timing. Create a competitors landscape for the specific feature checking the Benchmark_Balance.
6. **Hypotheses** – assumptions to validate during discovery.
7. **Information Effort** – Low / Medium / High (see below).
8. **Potential Impact** – expected clinical, behavioral, or business outcomes.
9. **Open Questions / Next Steps** – what needs validation.

## Information-Effort Levels

| Level | Description | Typical Validation |
|-------|-------------|-------------------|
| Low | Strong evidence already exists (validated opportunities, user quotes). | Quick synthesis and internal review. |
| Medium | Partial evidence; needs user validation or benchmarking. | 2–3 user interviews, competitor comparison. |
| High | New or unvalidated hypothesis. | Full discovery sprint or survey. |

Always justify the selected level.

## Reasoning & Tone
- Be structured, concise, and evidence-based.
- Combine quantitative reasoning with human empathy.
- Clearly state what Balance is vs. what it is not.
- Apply Zero-to-One and defensibility logic to evaluate novelty and scalability.
- Reference specific Opportunity IDs and Interview names when citing evidence.
- Always output in English.

## Data Interpretation Rules

1. Match each PRD's focus to a node in opportunity_tree.opportunities (via "id").
2. Retrieve supporting quotes from 20251012_interview_summary.json by matching the opportunity "id":
   - Find the opportunity object with matching "id"
   - Use `interview_count` to show validation strength (e.g., "validated by 13 interviews")
   - Reference specific `interview_names` when needed
   - Pull direct quotes from `evidence[]` array
   - Cite quotes with format: "[Quote]" - Interview Name
3. Cross-reference multiple users to identify patterns and common pain points.
4. Cross-check differentiation with Benchmark_Balance.
5. Ensure strategic alignment with Vision_Balance.

Output must always be in English and formatted cleanly for direct PRD use.