# TARGET REPOSITORY TOPOLOGY CONTRACT GATE

# Purpose

This gate prevents structural-generation failures by requiring a clear target topology before producing or patching a repository, ZIP, codebase skeleton, documentation migration, or tunnel/code integration.

It is general to all projects. It must not contain project-specific technology choices, project names, or product-specific business logic.

---

# Core Rule

When the user asks for a structural repository output, the model must establish a target repository topology contract before generating the final artifact.

A topology contract defines where each class of artifact belongs and what each folder means.

The model must not infer that a container folder is the actual project when the repository standard says actual projects live inside that container.

---

# Mandatory Distinctions

For any structural transformation or generated project repository, distinguish:

1. repository operating entry;
2. cognitive/runtime method layer;
3. orchestration/expert method layer;
4. project-instance container;
5. actual project folder;
6. project-local tunnel/control plane;
7. product/developer documentation;
8. backend/source implementation;
9. frontend/client implementation;
10. database artifacts;
11. infrastructure and operations;
12. scripts, tools, and tests.

---

# Project Container Rule

A folder that exists to contain project instances is not itself the actual project unless the repository explicitly declares it so.

If a container contains a named project folder, then that named folder is the project boundary.

Therefore, "inside the project" means inside the named project folder, not inside the project-instance container.

---

# Contract Fields

Before delivery, the model must be able to answer:

- What is the baseline repository?
- What is the actual project folder?
- Where is the project-local tunnel/control plane?
- Where is product/developer documentation?
- Where is backend/source code?
- Where is frontend/client code?
- Where are database artifacts?
- Where are infra, scripts, tools, and tests?
- Which folders are forbidden as tunnel locations?
- Which paths are canonical after migration?
- What existing folders were moved, copied, preserved, or removed?

---

# Forbidden Patterns

Reject or repair these patterns:

- treating a project-instance container as the actual project when a project folder exists inside it;
- placing the general operating tunnel inside ordinary product documentation;
- creating two competing project-local tunnels;
- duplicating product documentation under old and new roots without a migration manifest;
- creating backend/frontend/database beside the project folder when the user requested them inside the project;
- changing upper-layer general methods to include project-specific stack choices;
- validating only folder existence while ignoring ownership and routing.

---

# Validation

A generated repository must include a concise report or manifest identifying the selected topology and the validation performed.

If the topology contract cannot be established, the model must not produce a final ZIP as if the shape were confirmed. It must either ask the smallest necessary question or deliver a partial diagnostic when the user requested audit.
