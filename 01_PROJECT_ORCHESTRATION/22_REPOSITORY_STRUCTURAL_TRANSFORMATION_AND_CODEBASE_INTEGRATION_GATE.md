# REPOSITORY STRUCTURAL TRANSFORMATION AND CODEBASE INTEGRATION GATE

# Purpose

This file defines the mandatory expert-engine gate for any task that changes the structural identity of an existing repository, documentation workspace, project tunnel, or codebase.

It exists because ordinary artifact generation, ordinary repository patching, and ordinary implementation translation are not sufficient when the user is asking to transform a repository into a different operating shape.

This is a general project-orchestration rule. It is not specific to Pazarat or to any one software stack.

---

# Core Principle

A structural transformation is not a scaffold-generation task.

Before changing a repository's root layout, merging documentation with code, adding backend/frontend/database folders, moving a tunnel, relocating documentation branches, or creating a derived codebase, the model must first understand the current repository topology and the intended future topology.

The model must produce or internally establish a migration map before generating files.

The model must not treat "create a project structure" as permission to replace the existing repository method with a new imagined structure.

---

# When This Gate Is Triggered

Activate this gate when the request includes, implies, or corrects any of the following:

- convert this repository into a software project;
- merge documentation and code in one repository;
- integrate a project tunnel with backend, frontend, database, infrastructure, or tests;
- create a codebase around an existing project documentation set;
- move, restructure, rename, or re-root major repository folders;
- create a ZIP or generated repository from an existing repository;
- combine a cognitive/project tunnel with product documentation and implementation folders;
- add a `docs/`, `backend/`, `frontend/`, `database/`, `infra/`, `src/`, `.ai/`, or similar structural root to an existing repository;
- the user reports that a generated structure misunderstood the root, tunnel, docs, or code ownership.

This gate also activates when the model is uncertain whether the user wants a new derived artifact or a patch/migration of the existing repository.

---

# Structural Transformation Failure Modes

The model must explicitly guard against these failures:

1. **False root selection**
   - treating a subfolder as the new root without verifying the intended repository root;
   - placing the actual operating entry files under a product documentation folder.

2. **Tunnel burial**
   - moving a cognitive/runtime/orchestration tunnel into `docs/` or another content folder when it is meant to remain an operating layer.

3. **Competing entrypoints**
   - creating `.ai/`, `PROJECT_MAP.md`, `README.md`, or generated maps that become alternative higher-priority AI entrypoints without being explicitly subordinate to the repository entry route.

4. **Scaffold-from-memory replacement**
   - generating a new folder tree that resembles the desired project while abandoning the baseline repository.

5. **Documentation/code ownership confusion**
   - mixing product documentation, project-local control-plane files, runtime rules, generated implementation code, and database artifacts without a routing map.

6. **Unmapped branch migration**
   - moving existing documentation branches into `docs/` or implementation folders without a before/after map.

7. **Existence-only validation**
   - validating success by checking that folders exist instead of validating ownership, entry route, layer boundaries, references, and unchanged baseline content.

---

# Mandatory Structural Preflight

Before generating or editing files for a structural transformation, the model must complete this preflight silently or visibly depending on the user's request:

1. **Baseline identification**
   - Identify the source repository, archive, folder, or file set that is the baseline.
   - If a ZIP or uploaded repository exists, extract/copy it and treat it as the baseline.
   - Do not build from a previous generated scaffold unless the user explicitly selects that scaffold as the baseline.

2. **Root entry discovery**
   - Locate root entry files, command boards, project indexes, package files, solution files, source folders, documentation roots, and any explicit project-local tunnel.
   - Determine which files are operating entrypoints and which are ordinary documentation.

3. **Transformation classification**
   Classify the task as one of:
   - in-place patch;
   - derived artifact generation;
   - structural migration;
   - codebase integration;
   - documentation relocation;
   - repository merge;
   - audit/diagnosis only.

4. **Ownership map**
   Define where each category belongs after the transformation:
   - operating entry layer;
   - cognitive/runtime layer;
   - orchestration/expert layer;
   - project-instance control plane;
   - product/user/developer documentation;
   - backend code;
   - frontend code;
   - database artifacts;
   - infrastructure;
   - scripts and tests;
   - generated or temporary artifacts.

5. **Before/after migration map**
   For every major folder or file family that moves or is created, define:
   - source path;
   - target path;
   - owner;
   - purpose;
   - whether it is moved, copied, referenced, generated, or left unchanged;
   - which references must be updated.

6. **Constraint verification**
   Verify all user constraints, including names, root shape, language, project type, exact folder intent, and whether existing project documentation must remain recognizable.

7. **Patch plan**
   Select the smallest safe operation: patch existing files, add a missing gate, move documented branches, create code folders, generate templates, or stop and report missing information.

---

# Codebase Integration Rules

When transforming a project documentation workspace into a software codebase, the model must distinguish these layers:

```text
repository-root/
  operating entry files and runtime/orchestration layers
  project-instance control plane
  docs/              product/developer documentation
  backend|src/       backend implementation
  frontend|web/      frontend implementation
  database/          schemas, migrations, seeds, read models
  infra/             deployment, IaC, containers, operations
  scripts/           repeatable project commands
  tests/             cross-cutting tests when separate from stack-specific tests
```

The exact names are project-local decisions. The principle is not optional: documentation, control-plane logic, and implementation artifacts must not be collapsed into one ambiguous folder.

`docs/` means project/product/developer documentation unless a project explicitly defines otherwise.

A cognitive/runtime/orchestration tunnel must not be placed inside `docs/` merely because it is written in Markdown. It is an operating layer, not ordinary documentation.

If a lightweight `.ai/` helper is created, it must be explicitly subordinate to the main repository entry route and must not become a competing authority.

---

# Migration Map Requirement

A structural transformation must not be executed without a migration map.

The migration map may be a visible artifact or an internal working plan, but when delivering a patched repository the final report must summarize:

- baseline used;
- structural transformation type;
- folders/files added;
- folders/files moved or copied;
- folders/files intentionally unchanged;
- entrypoint preservation result;
- documentation routing result;
- code/database routing result;
- validation performed;
- known limitations.

If the transformation touches many files, prefer a generated manifest or diff summary over a prose-only claim.

---

# Validation Gate

Before delivery, validate at least the following:

1. Root entry files remain discoverable at the intended root.
2. Cognitive/runtime and project-orchestration layers remain project-neutral.
3. Project-specific truth remains in the project-instance layer or project documentation layer, not in upper layers.
4. `docs/` does not contain the general operating tunnel unless explicitly intended and justified.
5. Generated helper entrypoints are subordinate, not competing.
6. Existing documentation branches remain traceable after any move or copy.
7. Implementation folders have clear ownership and do not replace project-local truth.
8. No duplicated nested path such as `docs/ai_tunnel/docs/ai_tunnel/...` exists.
9. No mature baseline file is regenerated from memory when a patch was required.
10. Diff or manifest confirms that unrelated files were not changed.

---

# Repair Behavior

If a structural transformation failure is found, classify it first:

- application failure: the model ignored existing rules;
- missing general gate: the orchestration layer lacks a reusable guard;
- project-local routing gap: the active project lacks a codebase/docs routing standard;
- validation failure: the model checked existence but not ownership and entry route;
- user-intent ambiguity: the model selected a transformation mode before resolving root ownership.

Repair the smallest correct owner:

- patch the artifact if isolated;
- patch the project-local routing standard if the issue is local;
- patch this structural transformation gate or command boards if the issue is reusable across projects;
- avoid adding project-specific examples to upper layers.

---

# Final Principle

A repository structural transformation must preserve the intelligence of the existing repository while adding the requested execution structure.

The correct output is not the largest tree.

The correct output is a topology where each folder has a clear role, each layer keeps its ownership, the model has one reliable entry path, and future documentation, code, data, tests, and decisions can be routed without confusion.
