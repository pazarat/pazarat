# V7.4 Project Folder Correction Report

Baseline: `Mind_Ai_v7_2.zip`.

Purpose: fix the misunderstanding that `02_MY_PROJECT/` is the project. It is not. It is only the project-instance container. The actual Pazarat project is `02_MY_PROJECT/pazarat/`.

Implemented topology:

```text
02_MY_PROJECT/
  pazarat/                 # actual project folder
    00_PROJECT_TUNNEL/     # Pazarat local tunnel/control plane
    docs/                  # Pazarat documentation root
    backend/               # backend codebase
    frontend/              # frontend workspace
    database/              # database artifacts
    infra/                 # infrastructure
    scripts/               # project scripts
    tools/                 # project validators
    tests/                 # cross-cutting tests
```

Key corrections:

- Added general topology-contract gate to orchestration layer.
- Strengthened `02_MY_PROJECT` seed and gates to clarify container vs actual project folder.
- Moved Pazarat local tunnel files into `02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/`.
- Moved `A_dashboards`, `B_web_frontend`, and `C_mobile_app` into `02_MY_PROJECT/pazarat/docs/`.
- Added routing manifests so the model knows where to document and where to code.
- Added backend/frontend/database/infra/scripts/tests inside the actual Pazarat project folder.
- Cleaned explicit Pazarat/stack terms from upper general layers.

Validation:

Run:

```bash
python tools/verify_tunnel_integrity.py
python 02_MY_PROJECT/pazarat/tools/verify_pazarat_project_topology.py
```
