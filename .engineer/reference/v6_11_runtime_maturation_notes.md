# v6.11 Runtime Maturation Notes

## Purpose

This maturation pass strengthens the project engineer runtime without changing its visible role: the engineer remains focused on the active project, while the runtime stays silent unless explicitly inspected.

## Key changes

1. Distribution mode is explicit: `template` or `working_snapshot`.
2. Runtime cache is treated as volatile and non-authoritative.
3. Repository-static fingerprints exclude generated runtime state to avoid self-stale cache loops.
4. Semantic navigation now distinguishes runtime, external research, implementation translation, writing/content, research, write/modify, governance, comparison, project work, and project-surface requests.
5. Unknown intent falls back to bounded project work rather than project-surface identity mode.
6. Safe-write enforces scope containment before applying any write.
7. `.jsonl` ledgers are readable content.
8. Code files are classified as code by primary extension before content keyword signals.
9. Duplicate/impact scans filter generic scan terms to reduce false positives.
10. Tool registry now describes purpose, mutation behavior, scope, risk, and generated-output contracts.

## Non-breaking policy

Existing lifecycle behavior remains intact:

- `doctor` remains pass/fail compatible.
- `runtime-audit.status` stays `pass` when only nonfatal warnings exist, while `health` exposes `pass_with_warnings`.
- Project-facing answers still hide runtime internals.
- Current project files still outrank generated reports and external research.
