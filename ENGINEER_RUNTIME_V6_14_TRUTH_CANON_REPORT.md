# Engineer Runtime v6.14 — Incomplete Truth And Code Practice Canon Report

## Purpose

v6.14 applies a new methodology across the engineer architecture and the active project extension:

1. **Incomplete Truth Maturity** — an authoritative file can exist and still be too thin for execution.
2. **Discovery / Execution Separation** — the engineer may discover and propose repairs, but cannot execute production-oriented work over unaccepted repairs.
3. **Code Practice Canon** — stack selection is not enough; production code must obey implementation-practice rules.
4. **Best-Fit Reality Comparison** — best practice is mapped to current project truth and lifecycle risk, not copied generically.

## Runtime Additions

New governance/protocol files:

- `.engineer/governance/incomplete_truth_maturity.yaml`
- `.engineer/protocols/incomplete_truth_maturity_cycle.md`
- `.engineer/protocols/best_fit_reality_comparison.yaml`
- `.engineer/protocols/code_practice_canon_gate.yaml`
- `.engineer/reference/v6_14_incomplete_truth_and_code_canon_notes.md`

New commands:

- `truth-maturity`
- `canon-check`

Updated commands and behavior:

- `plug` now includes `truth_maturity_summary` and `canon_check_summary` when relevant.
- `neural` includes `incomplete_truth_reflex` and `code_practice_reflex`.
- `best-fit` now treats incomplete truth and code-practice canon as excellence patterns.
- `runtime-audit` verifies the new commands and governance files.

## Active Project Extension

New project-local standard:

- `18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md`

Updated project-local files:

- `02_PROJECT_TRUTH_INDEX.yaml`
- `12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml`
- `13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md`
- `14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md`
- `06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md`
- `11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md`
- `99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md`

## Core Rule

```txt
A local file can be binding truth, but if it does not satisfy higher project truth,
platform reality, downstream execution, or required implementation practice, classify
it as incomplete truth and repair the owner before production-oriented execution.
```

## Verification

Observed verification after the upgrade:

- `python .engineer/commands/engineer.py runtime-audit` → pass
- `python .engineer/commands/engineer.py doctor` → pass
- registry/CLI commands → 40 / 40
- `tests/test_v614_incomplete_truth_code_canon.py` → 5 passed
- v6.13, v6.12, v6.11, v6.10, and older core tests were run as individual files and passed.

## Important Note

The active project extension is project-local. The runtime methodology is generic and remains project-neutral. The active project now demonstrates the methodology through its own code-practice canon and runtime gates.
