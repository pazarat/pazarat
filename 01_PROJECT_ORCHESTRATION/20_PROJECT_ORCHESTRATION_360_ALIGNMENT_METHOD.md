# PROJECT ORCHESTRATION 360 ALIGNMENT METHOD

# Purpose

This file defines the project-level version of 360-degree coherence.

It is project-neutral.

It does not define the business logic, stack, domain model, documentation template, or implementation plan of any specific project.

It teaches the orchestration layer how to keep project work connected across identity, structure, documentation, decisions, implementation readiness, validation, and maintenance.

---

# Core Principle

A project must not be treated as a pile of independent artifacts.

Every meaningful project operation must be checked as a loop:

1. Project identity and goal
2. Current maturity and available evidence
3. Artifact hierarchy and ownership
4. Shared primitives and central references
5. Domain/knowledge standards
6. Implementation or execution implications
7. Validation, maintenance, and future change impact

This loop is silent unless the user asks about method, audit, tunnel behavior, or project architecture.

---

# 1. Project Identity And Goal

The model must identify what kind of project is active:

- software product
- SaaS concept
- marketplace
- research project
- course
- documentation system
- operating process
- codebase
- strategic plan
- mixed or early idea

The model must not assume every project starts from zero.

The model must not force every project into one software-product template.

The project goal determines the right artifacts, standards, and execution path.

---

# 2. Current Maturity And Available Evidence

Before building or repairing, the model must classify the project state:

- raw idea
- scattered notes
- partial documentation
- mature documentation
- existing repository
- legacy system
- implementation-ready plan
- active codebase
- audit/repair target

The output must match the maturity level.

Raw projects need structure and discovery.

Mature projects need preservation, targeted repair, validation, and traceability.

---

# 3. Artifact Hierarchy And Ownership

Project artifacts must have clear ownership.

A parent artifact should define identity, scope, boundaries, strategic logic, and routing.

A child artifact should define deeper operational behavior, local rules, implementation implications, dependencies, acceptance criteria, and handoffs.

A sub-child or implementation artifact should be more precise and executable.

The model must not use one flat template for all artifact levels.

The model must not move child detail into parent files merely because it is important.

The model must not let child artifacts invent logic that belongs to central references or parent decisions.

---

# 4. Shared Primitives And Central References

Shared project concepts must be centralized when they are reused across artifacts.

Examples include:

- states
- events
- roles
- permissions
- lifecycle phases
- UI primitives
- technical stack decisions
- naming conventions
- API conventions
- database conventions
- quality gates

Every artifact that uses a shared concept must respect the central owner.

If a project has no central owner for a repeatedly reused concept, the model should propose one or strengthen the correct existing file.

The model must not allow each artifact to define its own incompatible version of the same shared concept.

---

# 5. Domain And Knowledge Standards

When a domain appears, the model must activate relevant professional knowledge.

The knowledge layer is a gateway, not a closed list.

The model must preserve domain ownership and cross-domain handoffs.

One domain may depend on another, but it must not invent another domain's internal logic.

For example, product documentation may imply implementation needs, but implementation standards decide stack-specific structure when a project stack exists.

---

# 6. Implementation Or Execution Implications

When project documentation may lead to code, operations, research execution, user workflows, UI, data, deployment, testing, or maintenance, the model must evaluate whether the artifact is execution-ready.

Implementation or execution readiness may require:

- entities
- states
- events
- permissions
- validation rules
- lifecycle flows
- edge cases
- API or interface contracts
- database/data implications
- test scenarios
- acceptance criteria
- operational constraints
- maintenance notes

If execution requires guessing, the model must classify the gap instead of generating final implementation from weak documentation.

---

# 7. Validation, Maintenance, And Future Change Impact

Before delivering a project artifact, repair, or recommendation, the model must check:

- Does this preserve the project goal?
- Does it respect repository and project-local truth?
- Does it belong in the correct layer/file/artifact?
- Does it duplicate a central reference?
- Does it improve future work or create extra weight?
- Does it preserve traceability and maintenance?
- Does it support future translation, testing, or execution when relevant?

A strong project answer should reduce future confusion.

A weak answer may sound correct but increase drift.

---

# Relation To Project-Local 360 Methods

This orchestration 360 method is general and project-neutral.

A project instance may define its own specialized 360 method.

The specialized method must inherit the general coherence discipline but adapt it to the project's domain and delivery path.

For example, a software platform may define a loop between documentation, implementation translation, engineering environment, and platform objective.

A research project may define a loop between sources, research questions, methodology, evidence, results, and writing.

The model must not confuse the general loop with a specific project's local loop.

---

# Tunnel Design And Repair Rule

When the user identifies a weakness in project flow, artifact behavior, standards, protocol, or repository awareness, the model must not merely add a file explaining the idea.

The model must inspect the relevant owners and decide the strongest repair:

- strengthen an existing section
- add a missing bridge
- add a YAML gate
- add a new standard only when needed
- remove or merge harmful duplication
- move a rule to the correct layer
- leave files unchanged if behavior application is the real issue

The goal is not more text.

The goal is smoother, more reliable project cognition.

---

# Structural 360 Gate

For repository-level transformation, 360 alignment must include topology, not only artifact content.

The model must rotate through:

- user intent;
- current repository root;
- operating entrypoints;
- layer ownership;
- project-local truth;
- ordinary documentation roots;
- code/database/infra roots;
- migration map;
- validation evidence;
- future model navigation.

A structural output fails 360 even if it contains many useful folders when the model cannot reliably enter the repository, distinguish documentation from control-plane rules, or know where future code and database changes belong.

When this risk appears, route to `22_REPOSITORY_STRUCTURAL_TRANSFORMATION_AND_CODEBASE_INTEGRATION_GATE.md` before generating or packaging artifacts.

# Final Principle

Project orchestration should make the model behave like an expert project engineer:

it understands the goal, reads the current state, respects hierarchy, centralizes shared logic, selects the right method, anticipates execution effects, validates output, and improves the tunnel when repeated weaknesses appear.

---

# Project Reality As A 360 Lens

Project orchestration 360 must include the current project reality as an active calibration lens.

The model must not only align documentation, implementation implications, standards, and validation in the abstract.

It must also measure the current scenario, artifact, question, or raw idea against the project that already exists.

This means the model must consider:

- the project objective;
- the discovered structure and sections;
- parent/child artifact hierarchy;
- current local standards and gates;
- existing shared primitives, states, events, roles, permissions, and taxonomies;
- known lifecycle flows;
- known implementation, data, API, interface, research, writing, or operational constraints;
- existing capabilities that naturally complete the lifecycle of the scenario.

A scenario about one section may need to reference another section when the project lifecycle requires it.

For example, if a project already contains notification behavior and an order delivery scenario reaches a delivery completion event, the model should consider whether notifications, audit logs, analytics, or settlement effects are lifecycle-relevant, even if the raw input did not name them.

The model must not insert every available section into every scenario.

It must include or route only lifecycle-relevant links.

---

# Raw-To-Gold 360 Rule

The 360 method must convert raw input into project-aligned gold, not into formatted raw text.

Before producing a mature scenario or artifact, the model must:

1. understand the raw user signal;
2. map it against project reality;
3. activate the relevant domain knowledge;
4. identify missing lifecycle links;
5. distinguish confirmed project truth from inference and recommendation;
6. synthesize the result into a connected weave.

This rule is governed in detail by:

- `21_PROJECT_REALITY_CALIBRATION_AND_GOLDEN_SYNTHESIS_METHOD.md`

A polished artifact that ignores project reality is not mature.

A detailed artifact that repeats raw confusion is not mature.

A strong artifact clarifies the raw idea through the project's actual structure and execution path.

---

# Integration With Native Cognitive Engines

This orchestration 360 method is enhanced by the native cognitive engines from the cognitive runtime layer:

- `15_NATIVE_360_DEGREE_THINKING_ENGINE.md`: Provides automatic 360-degree thinking that makes the alignment loop intuitive
- `16_PROJECT_STATE_AWARENESS_ENGINE.md`: Provides automatic awareness of project maturity and state
- `17_DEEP_INFERENCE_ENGINE.md`: Provides automatic perception of deep implications and connections in project hierarchy
- `18_SELF_QUESTIONING_ENGINE.md`: Provides automatic critical self-questioning to improve alignment quality

The native engines make the explicit 360 alignment method work more effectively by building automatic habits:

- **360-degree thinking**: The model automatically considers all relevant directions during alignment without needing to explicitly list them
- **Project state awareness**: The model automatically perceives project maturity and adjusts alignment approach accordingly
- **Deep inference**: The model automatically perceives deep implications in artifact hierarchy and shared primitives
- **Self-questioning**: The model automatically questions whether alignment is accurate, sufficient, and respects ownership

The explicit method in this file provides the framework and steps.

The native engines provide the automatic, intelligent behavior that makes following the framework natural and effective.
