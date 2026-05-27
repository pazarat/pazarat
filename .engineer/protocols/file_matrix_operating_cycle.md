# File Matrix Operating Cycle v8.1

Purpose: give the model a fast, whole-project nervous-system surface before file work, while preserving the rule that current files are the source of truth.

## Cycle

1. **Entry**: classify intent through `plug` / `operation-mode`.
2. **Touch**: run `file-matrix-touch` for orientation when the model needs project awareness.
3. **Query**: run `file-matrix-query` for multi-lens retrieval.
4. **Context**: run `file-matrix-context` when a response, design, comparison, or implementation needs owner evidence.
5. **Read**: read selected owner files before strong claims or writes.
6. **Write gates**: duplicate-scan, impact-scan, write-plan, safe-write.
7. **Validation**: doctor, file-matrix-doctor, and project-specific build/test/lint/typecheck when available.
8. **Receipt**: record what was indexed, selected, read, changed, and validated.

## Non-negotiable boundaries

- The index is acceleration state, not source of truth.
- The active project lives under `02_WORKSHOP/ACTIVE_PROJECT`.
- Workshop/runtime files govern method and behavior.
- A missing or empty active project is valid and must trigger project-formation behavior, not failure.
