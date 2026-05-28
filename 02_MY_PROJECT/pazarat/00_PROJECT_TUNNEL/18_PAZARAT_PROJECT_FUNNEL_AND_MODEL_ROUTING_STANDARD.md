# PAZARAT PROJECT FUNNEL AND MODEL ROUTING STANDARD

# Purpose

This standard defines the Pazarat project funnel, the phase-based path for complex task execution, and the rule that any model reaching the third funnel phase must preserve the same architecture and decision philosophy.

It is meant to make the repository robust enough to handle complex project requests without losing structure, repeatability, or implementation readiness.

---

# Core Principle

Pazarat must process complex requests through a staged funnel, not as a single flat generation task.

Each funnel stage must clarify purpose, route outputs, and preserve the active codebase shape.

A model may only reach funnel stage 3 after stage 1 and stage 2 have confirmed:

- the target architecture
- the documentation routing
- the backend/frontend/database/infra split
- the Pazarat control-plane boundaries

If a model reaches stage 3, it must continue within the same structural philosophy.

---

# Funnel Stages

## Stage 1: Discovery

- Capture and normalize user intent.
- Identify whether the request targets a software project, documentation update, or mixed solution.
- Detect the active project and existing repository structure.
- Confirm that the project requires a full codebase skeleton when the ask is "مرحلة باء الكود".
- Map current documentation to `docs/` and control-plane standards to `02_MY_PROJECT/pazarat/`.

## Stage 2: Architecture and Routing

- Define the target folder shape for implementation.
- Route documentation to `docs/`.
- Route backend work to `backend/`.
- Route frontend work to `frontend/`.
- Route data work to `database/`.
- Route infrastructure and deployment work to `infra/` and `.github/`.
- Keep `00_PROJECT_TUNNEL/` as the Pazarat project-local control plane for identity, standards, routing, and traceability.
- Keep `00_PROJECT_TUNNEL/` as the local decision gate for complex task consistency.

## Stage 3: Execution

- Generate or organize concrete artifacts in the target project structure.
- Preserve naming, traceability, and folder ownership.
- Keep documentation artifacts separate from the runtime/orchestration tunnel.
- Ensure any model arriving at stage 3 uses the same funnel philosophy even under repetition or complex branching.

---

# Rule for Stage 3 Consistency

If a model reaches `02_MY_PROJECT/pazarat/project_tunnel/18_PAZARAT_PROJECT_FUNNEL_AND_MODEL_ROUTING_STANDARD.md` or an equivalent execution stage:

- it must not regress to an ad hoc documentation archive layout;
- it must not fold `00_PROJECT_TUNNEL/` control-plane content into `docs/`;
- it must not scatter implementation files across unrelated folders;
- it must continue to route code to `backend/`, `frontend/`, `database/`, `infra/`, and `scripts/`.

This rule ensures that the repository remains strong, packaged, and referenceable for arbitrarily complex tasks.
