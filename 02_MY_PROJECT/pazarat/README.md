# Pazarat Project Folder

`02_MY_PROJECT/pazarat/` is the actual Pazarat project boundary.

Inside this project:

- `00_PROJECT_TUNNEL/` is the Pazarat local tunnel/control plane.
- `docs/` is product/developer documentation.
- `backend/` is the backend codebase.
- `frontend/` is the frontend workspace.
- `database/` is database schemas, migrations, seeds, and read models.
- `infra/` is deployment/operations infrastructure.
- `scripts/` and `tools/` are repeatable project commands and validation utilities.
- `tests/` is for cross-cutting project tests.

Do not treat `02_MY_PROJECT/` as the Pazarat project. It is only the project-instance container.

## Execution enforcement

All non-trivial Pazarat work must pass through the local tunnel execution cycle:

```text
00_PROJECT_TUNNEL/19_PAZARAT_TASK_EXECUTION_AND_DELIVERY_CONFORMANCE_STANDARD.md
00_PROJECT_TUNNEL/_execution/
```

This turns documentation and code generation into planned, validated tasks rather than free-form output.
