# Engineer Runtime v6.18 — Workshop Neural Gate and Neutral Runtime Repair

## Purpose

This release repairs the project-specific coupling introduced in the surface lens and promotes `02_WORKSHOP/_WORKSHOP_SYSTEM` into a silent universal method gate inside the engineer operating cycle.

## Key Fixes

- Removed project-specific file/module priority from runtime logic.
- Added a runtime audit check for active-project-specific coupling inside static runtime files.
- Added `workshop-lens` as a first-class command.
- Added workshop universal method files: truth hierarchy, incomplete truth, 360 method, maturity assessment, local standards generation, execution gates.
- Added software universal canon and core software discipline canons.
- Updated plug/neural/project-lens to include the workshop lens as a silent maturity gate.
- Changed project-surface first step behavior: surface lens may identify owner truth and incomplete children, but it must not choose a specific child repair target until owner routing and direct children are read.
- Added tests for workshop gate and runtime neutrality.

## Boundaries

- Workshop canons are maturity lenses and local-standard generators.
- Workshop canons do not override active project truth.
- Active project facts may appear in project-lens output when discovered from files, but not in static runtime logic.

## Verification

- `runtime-audit`: pass
- `doctor`: pass
- `tool registry`: 44/44
- `tests/test_v618_workshop_neutral_runtime.py`: passed

## Packaging Note

Generated indexes and ledgers should be cleaned before distribution.
