# PAZARAT PROJECT TUNNEL ENTRY

This folder is the dedicated local tunnel/control plane for the Pazarat project.

Important boundary rule:

- `02_MY_PROJECT/` is the project-instance container.
- `02_MY_PROJECT/pazarat/` is the actual Pazarat project folder.
- `02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/` is the Pazarat project-local tunnel and routing/control plane.
- `02_MY_PROJECT/pazarat/docs/` is product/developer documentation.
- `02_MY_PROJECT/pazarat/backend/`, `frontend/`, `database/`, `infra/`, `scripts/`, and `tests/` are implementation/execution areas.

Models must enter this folder before editing Pazarat docs, code, database, infrastructure, or tests.

## Mandatory task execution layer

For non-trivial work, the model must not treat these tunnel files as reading material only.

Before changing Pazarat docs, backend, frontend, database, infrastructure, scripts, tests, routing, registries, or tunnel standards, the model must activate:

```text
19_PAZARAT_TASK_EXECUTION_AND_DELIVERY_CONFORMANCE_STANDARD.md
00_PROJECT_TUNNEL/_execution/
```

The required execution loop is:

```text
Task plan -> affected surface map -> execution -> validation -> delivery conformance -> final response
```

A task is not complete because files exist. It is complete only when planned outputs, actual outputs, routing/traceability, and validation evidence agree.
