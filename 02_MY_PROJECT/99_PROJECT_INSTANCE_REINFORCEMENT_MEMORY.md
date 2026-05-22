# PROJECT INSTANCE REINFORCEMENT MEMORY

# Purpose

This file is the compact reinforcement memory for the project instance layer.

It reinforces the highest-priority behaviors that must remain active when the model enters this layer and works with any actual project stored under it.

This file is not the full project identity.

It is not the full project standard.

It is not a project-specific PRD.

It is not a project status report.

It is not a replacement for any discovered project folder.

Its purpose is to ensure the model treats this layer as a gateway to project truth, discovers actual project content dynamically, enters any discovered project folder, reads local numbered tunnels, and answers from cumulative project context.

---

# Highest Priority Rule

This folder is the project instance entry layer.

The model must not assume that this folder itself is always the whole project.

The actual project may be inside a non-numbered folder under this layer.

The model must discover the project from:

- numbered files in this folder
- non-numbered folders and files after the numbered root tunnel
- discovered project folder names
- project-local numbered files
- project identity files
- project structure files
- current conversation
- user intent

The model must not require the project name to be hardcoded in upper layers.

The model must not stop at this layer when the user request clearly targets a real project inside it.

---

# Expected Root Pattern

A preferred project instance root may look like this:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/

The files `00_PROJECT_STANDARD_SEED.md` and `99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md` are entry guard files.

They are not substitutes for the actual project.

They tell the model how to continue into project content.

If a folder such as `<project_folder>/` exists after the numbered root files, the model should treat it as discovered project content or an active project candidate according to context.

---

# Root Numbered Tunnel Rule

Numbered root files directly inside this folder form the project instance root tunnel.

A numbered root file is a file directly inside this folder whose name begins with a numeric prefix from `00` to `99`.

The model must account for actual numbered root files in numeric order.

Numeric order determines traversal order.

File name suggests responsibility.

File content confirms actual purpose.

Missing numbers do not break the tunnel.

The model must not rely only on a hardcoded list of expected files.

If a new numbered root file appears in this folder, it should be treated as part of the root tunnel unless clearly obsolete, temporary, backup, unrelated, or outside active project scope.

---

# Non-Numbered Content After Root Tunnel

After the root numbered tunnel is accounted for, non-numbered files and folders in this layer are usually project content or project candidates.

They may include:

- a named project folder
- multiple project folders
- product branches
- documentation branches
- research folders
- knowledge folders
- learning modules
- raw references
- local standards
- implementation notes
- artifacts
- drafts
- placeholders

The model must not ignore non-numbered content because it is not explicitly registered.

The model must inspect non-numbered content dynamically according to the user’s request.

---

# Active Project Discovery Without Explicit Name

If this folder contains exactly one non-numbered project folder, the model should treat that folder as the active project candidate by default.

If this folder contains multiple non-numbered folders, the model should infer the active project or branch from:

- current conversation
- folder names
- target path
- project identity files
- local numbered standards
- recent user references
- repository structure
- project terminology
- artifact names
- user intent

Ask one focused question only when ambiguity materially changes the answer or generated artifact.

Do not fail because the active project name was not explicitly stated.

---

# Discovered Project Folder Rule

When the model discovers a non-numbered project folder inside this layer and the request is project-specific, it must enter that folder.

Inside the discovered project folder, the model must check for numbered root files.

If numbered root files exist, they form the project-local tunnel.

The model must account for the project-local tunnel before inspecting deeper project content.

Example:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/
        00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
        01_<PROJECT>_IDENTITY_AND_OBJECTIVES.md
        02_PLATFORM_STATE_TAXONOMY.md
        03_PLATFORM_EVENT_TAXONOMY.md
        04_PROJECT_STRUCTURE_TREE_INDEX.md
        05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
        06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
        07_<PROJECT>_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
        08_<PROJECT>_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md

In this pattern, `<project_folder>/` is the discovered project folder.

The model must not stop at `02_MY_PROJECT/`.

It must continue into `<project_folder>/` when the request is about the active project or when it is the only active project candidate.

---

# Project-Local Numbered Tunnel

A discovered project folder may define its own local numbered tunnel.

A project-local tunnel may contain:

- project cognition standards
- project identity and objectives
- state taxonomy
- event taxonomy
- structure tree
- UI/UX standards
- implementation standards
- hierarchical documentation protocols
- shared primitives
- decision logs
- roadmaps
- reinforcement memories
- local project-specific standards

The exact names are project-specific.

The model must not require a fixed list.

The model must discover actual numbered root files and account for them in numeric order.

Project-local numbered files govern project-specific work.

They must be considered before generating, revising, judging, or auditing project artifacts.

---

# Fourth-Level And Deeper Local Tunnels

A project may contain local tunnels inside branches, modules, domains, artifact families, or content folders.

Examples:

- dashboard branch tunnel
- admin dashboard tunnel
- module tunnel
- workflow family tunnel
- research area tunnel
- knowledge domain tunnel
- implementation branch tunnel
- UI branch tunnel
- child artifact folder tunnel

When the user targets a specific branch, module, artifact, scenario, workflow, or folder, the model must check the relevant folder and parent folders for numbered root files.

If local numbered files exist, they are local governing context.

The model must account for them before working on non-numbered content inside that branch.

---

# Tunnel Before Dynamic Exploration

The model must distinguish between tunnel traversal and dynamic exploration.

Tunnel traversal means accounting for numbered root files that govern project standards, local rules, artifact behavior, or branch logic.

Dynamic exploration means inspecting non-numbered files and folders according to the user’s current request.

Correct project-specific sequence:

1. Enter the project instance layer.
2. Account for numbered root files in this folder.
3. Discover non-numbered project candidates or project content.
4. Enter the relevant discovered project folder.
5. Account for numbered root files inside the discovered project folder.
6. Continue the same pattern for relevant branches, modules, domains, or artifact families.
7. After local tunnels are accounted for, inspect non-numbered target content dynamically.
8. Compare repository context with current conversation decisions and corrections.
9. Answer or generate from cumulative context.

The model must not jump directly to deep project files while skipping governing numbered files.

The model must not scan unrelated files when the request is focused.

---

# Project Files Should Be Locally Understandable

Project-specific files should be understood from their local project context.

They should not need to repeat exact paths to cognitive runtime or project orchestration layers.

The upper layers are responsible for routing the model into this project instance.

This layer is responsible for discovering project folders.

Each discovered project folder is responsible for preserving its own project-specific truth.

This keeps projects portable and prevents upper-layer architecture from polluting project-specific documentation.

---

# Project-Facing Artifact Alignment Marker Rule

Project-facing artifacts should remain locally understandable.

They should not expose full cognitive runtime or project orchestration file lists unless the artifact is specifically about repository architecture or methodology.

When an artifact needs to remind future AI to apply local project standards, use a compact alignment marker instead of listing internal governance files.

Recommended marker:

    This artifact must be interpreted through the active project-local numbered tunnel from 00 to 99 before generation, review, design translation, or implementation translation.

This marker is enough for future AI to apply the discovered project-local standards without exposing the full internal governance structure to human readers.

Human readers should see the resulting project logic, not the internal governance machinery.

If a developer or designer needs a reference, expose project-facing references such as:

    central state taxonomy
    central event taxonomy
    UI/UX standard
    implementation standard
    shared primitives
    acceptance criteria
    open decisions

The upper layers should guide the model silently.

The project artifact should remain clean, portable, and readable.

---

# Project-Specific Truth Priority

When answering or generating inside a discovered project, prioritize:

1. root numbered files in this project instance layer
2. discovered project folder numbered standards
3. branch-local numbered standards
4. project identity and objectives
5. project structure tree
6. project state, event, knowledge, decision, and primitive files
7. target artifact content
8. parent artifact context
9. child or sibling artifacts when relevant
10. current conversation and latest user corrections
11. general project orchestration method
12. general knowledge only as support

Do not answer project-specific questions from general method alone when project truth exists.

Do not present inferred or proposed project content as documented truth.

---

# Minimal Project Instance Is Valid

A minimal project instance may contain only:

    00_PROJECT_STANDARD_SEED.md
    99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md

This is valid.

It means the project instance is ready to grow.

It does not mean the repository is broken.

If no project content exists yet, the model should help bootstrap the project from conversation.

If project content exists but standards are minimal, the model should extract project signals carefully and propose the smallest useful next standard.

Do not create many empty files only to simulate maturity.

---


# Empty Project Slot And SaaS-Style Use

This layer may be intentionally empty except for the root guard files.

That state is valid.

It means there is no stored project truth yet beyond this gateway, not that the expert engine has failed.

When no project folder exists, the model must use the current conversation as the live working context and the upper layers as the expert reasoning environment.

The model should answer, plan, diagnose, or consult according to the user’s current intent.

If durable continuity would help, recommend or create the smallest useful project-local standard.

Do not invent a project folder, project identity, taxonomy, or artifact as existing truth.

Do not force file creation when the user wants only a high-quality SaaS-like consultation or discussion.

---

# Project Content May Exist Before Standards

A project may contain content folders before standards are complete.

This is common.

The model should:

- inspect relevant content when available
- classify content intent
- extract implicit standards
- preserve useful raw material
- recommend formal standards when repeated logic appears
- avoid dismissing content because standards are weak
- avoid treating raw content as final truth

Existing content can help build project standards.

---

# Raw References Are Valuable

Raw references may exist inside this project instance or inside discovered project folders.

They may be rough, duplicated, partial, incomplete, copied, or exploratory.

The model must not treat raw references as useless.

Raw references may contain:

- original user intent
- project decisions
- examples
- source material
- domain knowledge
- rejected directions
- terminology
- constraints
- future artifact seeds

The model should preserve raw references and extract useful signal when needed.

---

# Placeholders And Route Markers

A file or folder may be short or empty because it is a placeholder, route marker, or future structural node.

This is not automatically a problem.

The model must classify intent before judging.

Possible classifications include:

- intentional placeholder
- route marker
- empty structural node
- scaffold
- raw source
- old version
- accidental empty file
- ready-to-fill artifact

Do not treat every short file as weak.

Do not treat every placeholder as failure.

---

# Scaffolds Are Not Project Truth

A scaffold may provide temporary structure.

It may contain copied, generic, or placeholder content.

The model should not treat scaffold content as accepted project truth.

When replacing a scaffold:

- preserve useful structure
- remove generic filler
- add project-specific substance
- preserve accepted decisions
- keep open questions when needed

A scaffold is a starting point, not final maturity.

---

# Project Type Flexibility

This project instance may support many kinds of work.

It may contain:

- software platform
- SaaS product
- marketplace
- mobile application
- web application
- internal system
- research project
- learning project
- knowledge base
- academic project
- religious study system
- medical knowledge project
- legal analysis workspace
- writing project
- operational workflow system
- documentation workspace
- personal knowledge system
- complex mixed project

The model must not force software artifacts, PRDs, UI screens, or implementation notes on non-software projects.

Project artifacts must match the actual project type and user intent.

---

# Conversation Is Live Project Input

The current conversation may contain project-specific information that is not yet saved.

It may include:

- decisions
- corrections
- identity signals
- objective signals
- naming choices
- terminology
- scope boundaries
- rejected directions
- roadmap choices
- artifact instructions
- knowledge assumptions
- migration decisions

The model must use live conversation carefully.

If conversation updates project truth, recommend storing it in the right project file when useful.

Do not ignore conversation because files exist.

Do not ignore files because conversation is rich.

---

# Current Input As Intent Anchor

The latest user input is the first anchor for understanding the current request.

The model must not treat cumulative context as automatic continuation of the previous topic.

Conversation history is a searchable memory used to improve understanding of the latest input.

The model should first understand the current input, then retrieve relevant prior conversation threads.

When using prior conversation, classify each relevant thread as:

    accepted context
    modified context
    rejected context
    superseded context
    supporting context
    unrelated context
    conflicting context

Only accepted, modified, or supporting context should strengthen the current answer.

Rejected, superseded, unrelated, or conflicting context must not silently control the response.

If the latest input changes the meaning of an earlier concept, the latest accepted clarification should update the cumulative understanding.

If the latest input introduces a new distinction, the model must answer that distinction before continuing older work.

If the latest input exposes a failure in previous behavior, the model must treat that failure as a live project input and consider whether the repository needs a standard update.

Cumulative context means cumulative interpretation, not topic drift.

The model must not answer from an older thread unless it is relevant to the latest user input.

Correct interpretation order:

    current user input
    relevant prior conversation threads
    accepted or modified decisions
    current repository truth
    project-local standards
    general orchestration method
    final response or artifact

This order prevents both isolated answers and uncontrolled thread drift.

---

# Cumulative Context Rule

The model must answer from cumulative context.

Cumulative context includes:

- upper-layer behavior rules already applied
- project orchestration methods already applied
- this project instance entry gate
- discovered project folder standards
- local branch standards
- current conversation
- accepted decisions
- latest user corrections
- target artifact content
- parent, child, sibling, structure, knowledge, roadmap, primitive, and decision context when relevant

Cumulative context does not mean continuing the immediately previous topic by default.

It means interpreting the latest user input through relevant accepted context, prior decisions, project standards, and current repository truth.

The latest user input remains the active intent anchor.

The model must not behave as if each request is isolated.

The model must not add a new part while forgetting a previously accepted part.

Future answers must build on prior accepted context.

---

# Dynamic Discovery Depth

Discovery depth should match the request.

## Light Discovery

Use for simple project-aware answers.

## Focused Discovery

Use for a specific file, module, branch, artifact, scenario, workflow, or next step.

## Deep Discovery

Use for audit, migration, conflict resolution, maturity assessment, or architecture redesign.

## Full Discovery

Use only when the user asks for a full project or repository inspection.

The model must avoid both over-scanning and under-scanning.

---

# Project Artifact Generation

When generating project-specific files or artifacts, the model should identify:

- target path
- artifact type
- governing numbered tunnel files
- local standards
- project identity
- project objectives
- parent context
- relevant sibling or child context
- knowledge gaps
- accepted decisions
- maturity and readiness
- output safety requirements

Do not generate polished but unsupported project artifacts.

If context is incomplete but progress is useful, produce provisional content and preserve assumptions.

---

# Project Artifact Revision

When revising project-specific artifacts, preserve:

- accepted baseline
- accepted terminology
- accepted decisions
- project-specific rules
- parent context
- artifact purpose
- layer ownership
- previous user corrections
- raw source value
- output safety

Do not rewrite accepted artifacts as unrelated new versions.

Revision must be cumulative.

---

# Project-Local Tunnel And Artifact Performance Reinforcement

Project-local work must use the same disciplined engineering mindset as tunnel maintenance.

When a project file, scenario, research note, module standard, branch tunnel, or documentation artifact shows drift, weak logic, missing linkage, harmful repetition, poor execution-readiness, or unclear ownership, the model must diagnose the local weakness before editing.

The model should repair the smallest correct project owner:

- strengthen the right paragraph,
- replace unclear wording,
- add a missing bridge,
- move misplaced content,
- merge duplicate objectives,
- delete only after preserving useful meaning,
- or leave the artifact unchanged if behavior application is sufficient.

The goal is to make the project easier to understand, extend, design, implement, test, and maintain.

Project-local performance repair must not become upper-layer pollution, and upper-layer method must not overwrite project truth.

---

# Project Change Control

Accepted project standards and major artifacts should not change silently.

Use deliberate change awareness when modifying:

- identity
- objectives
- scope
- taxonomy
- structure
- artifact hierarchy
- roadmap
- terminology
- naming
- implementation assumptions
- mature accepted artifacts

Small wording or formatting fixes can stay lightweight.

Major changes should identify affected project context.

---

# Conflict Handling

If project sources conflict:

- identify the conflict
- identify likely authoritative source
- compare with current conversation
- determine whether user decision is needed
- propose update, merge, archive, rename, or replacement
- avoid silent compromise

Conflicts should become decisions or controlled updates.

---

# Output Safety

When generating files for this project instance, use strict output safety.

The model must protect:

- standalone path display
- correct numeric prefix
- correct extension
- correct layer path
- correct title responsibility
- copy-safe file block
- outer fence longer than internal fences
- no generated file content outside the block
- no commentary inside generated file content unless it belongs there

Broken output can damage project updates.

---

# Failure Signals

Project instance entry failures include:

- stopping at this file and not entering discovered project content
- requiring explicit project name registration
- ignoring non-numbered project folders
- skipping project-local numbered files
- skipping branch-local numbered files
- treating missing standards as project failure
- treating raw references as final artifacts
- treating placeholders as failures
- treating scaffolds as accepted truth
- answering project-specific questions generically
- judging maturity by file or folder existence alone
- forgetting accepted conversation decisions
- generating artifacts without parent or local standard context
- relying only on hardcoded project names
- relying only on explicit tunnel file lists instead of actual numbered files

When such failure occurs, correct the route and continue.

---

# Final Principle

This file is the reinforcement gate for the project instance layer.

It ensures the model does not stop too early, does not require a hardcoded project name, and does not ignore local project tunnels.

The project should be understood from its own files, folders, standards, artifacts, and current conversation.

The model must enter the relevant discovered project, read its actual local numbered standards, then explore dynamically according to the user’s goal.

A strong project instance entry makes future work cumulative, accurate, and project-native.

---

# Project Instance Runtime Gate Reinforcement

The project instance layer continues the tunnel into real project work.

Project-root YAML gates are active project-entry checks. They should help the model discover the active project, preserve project truth, localize repairs, and maintain translation paths from documentation to design, code, tests, or operations.

Do not escalate a project-local issue into the general tunnel unless the issue is reusable beyond the project.

Do not patch project artifacts when the failure is only a one-time execution mistake.

