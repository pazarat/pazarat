# Engineer Runtime v6.15 Surgical Maturation Report

This release is a conservative maturation patch over the neural/truth-canon runtime. It addresses context pressure, generated-cache self-confirmation, and matrix navigation depth without breaking the lifecycle or replacing the existing central plug model.

## Repairs applied

1. **Compact plug by default**
   - `plug` now defaults to compact steering output.
   - `plug --mode full` remains available for forensic/deep inspection.

2. **Relationship graph navigation**
   - Added `relationship-graph` command.
   - Matrix/plug now include relationship graph output or summary.
   - The graph maps likely owner candidates, parent/sibling candidates, and state/event/permission/API/test linkages.

3. **Generated cache discipline**
   - Added `cache-clean` command.
   - Added generated cache governance.
   - `best-fit` excludes `.engineer/indexes`, `.engineer/ledgers`, and `.engineer/state` by default.

4. **Version and registry alignment**
   - Runtime version aligned to `6.15.0`.
   - Registry now includes 42/42 commands.
   - Runtime audit now checks version drift and compact/relationship capabilities.

5. **Surgical restraint**
   - Did not bulk-split `engineer.py` to avoid introducing broad breakage.
   - Added a handoff file and protocols that define staged modularization as a future safe step.

## Verification

- `runtime-audit`: pass
- `doctor`: pass
- registry / parser command count: 42 / 42
- `tests/test_v615_surgical_maturation.py`: 5 passed
- v6.10-v6.14 targeted tests were run as independent tests/sets; the broad full suite can be slow because several tests run subprocesses that rebuild generated evidence.

## Remaining intentional debt

- `engineer.py` remains monolithic pending a staged extraction.
- Relationship graph is heuristic and should be reinforced later with explicit owner metadata.
- Compact output should continue to be tuned as project scale grows.
