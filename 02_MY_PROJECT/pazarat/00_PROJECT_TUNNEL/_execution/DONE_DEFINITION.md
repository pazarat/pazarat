# PAZARAT DEFINITION OF DONE

A Pazarat task is complete only when all applicable items pass.

## Mandatory for every non-trivial task

- The actual project folder is respected: `02_MY_PROJECT/pazarat/`.
- A task plan exists or the final delivery clearly summarizes one.
- Required outputs are listed and checked.
- Affected paths are listed and checked.
- Forbidden paths and behaviors are checked.
- Governing standards are applied.
- Validation was run, or the reason it could not be run is disclosed.
- Delivery conformance is reported.

## Additional for documentation tasks

- Documentation path is under `docs/` unless it is project-tunnel control logic.
- Implementation implications are classified when relevant.
- Routing and traceability are updated when documentation affects code/data/API ownership.

## Additional for code/database tasks

- Code lives under `backend/`, `frontend/`, `database/`, or another accepted implementation path inside Pazarat.
- Business behavior has a feature packet or implementation contract.
- Tests, migrations, API contracts, and traceability are considered.

## Additional for structural tasks

- Topology contract exists.
- Migration manifest exists when paths move.
- No duplicated source-of-truth roots remain.
- Validators pass.
