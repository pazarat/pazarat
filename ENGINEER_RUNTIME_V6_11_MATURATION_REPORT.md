# Engineer Runtime v6.11 Maturation Report

## Scope

This pass repaired and matured the engineering runtime itself, not the active project content.

## Applied repairs

- Declared distribution mode as `working_snapshot` so a real active project can coexist with a project-neutral runtime.
- Replaced the old “must ship empty” assumption with distribution-mode-aware policy.
- Strengthened semantic navigation for runtime inspection, external research, implementation translation, write/modify work, research projects, and content projects.
- Changed unknown-intent fallback from `project_surface` to `project_work` to prevent identity/status answers from swallowing real work requests.
- Added Arabic normalization for routing so terms with diacritics still match.
- Added write-scope containment in `safe-write`.
- Added repository-static fingerprinting that excludes generated runtime outputs.
- Required generated JSON indexes to carry `cache_meta` where produced by runtime commands.
- Added `.jsonl` as readable text so ledgers are not misclassified as empty binary-like files.
- Made code-extension classification primary to prevent source files from being mislabeled as truth files because they contain words like “truth” or “contract”.
- Reduced duplicate/impact false positives by filtering generic scan terms.
- Enriched the internal tool registry with purpose, mutation behavior, scope, risk, generated-output expectations, and safe-write prerequisites.
- Added v6.11 regression tests for routing, safe-write containment, runtime audit health, and write-guard tool planning.

## Verification performed

- `python .engineer/commands/engineer.py runtime-audit` returns `status: pass` and `health: pass` after cache refresh.
- `python .engineer/commands/engineer.py doctor` returns `status: pass`.
- Targeted v6.11 tests pass.
- Existing test modules were run individually; observed passes are preserved.

## Known operational note

A full single-shot `pytest tests -q` run can exceed the interactive execution timeout because many tests spawn subprocesses that rebuild project evidence over a non-empty working snapshot. Individual test modules complete successfully.
