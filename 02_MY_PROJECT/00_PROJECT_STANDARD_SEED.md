# PROJECT STANDARD SEED

# Purpose

This file is the seed and entry guard for the project instance layer.

It marks this folder as the project instance entry point.

It is not the full project identity.

It is not the full project standards file.

It is not a static project status report.

It is not a replacement for the actual project folder or project content.

Its purpose is to tell the model how to enter the project instance layer, discover project-specific content, identify project candidates, continue through local numbered tunnels, and understand project truth from the project itself.

This file allows the project instance to work whether the project is minimal, emerging, mature, or organized inside a named folder such as a product, research project, knowledge project, learning project, or documentation workspace.

---

# Core Principle

This folder is the project instance entry layer.

Project-specific truth belongs in this layer or inside the discovered project folders and files under it.

The upper layers guide the model into this layer.

This layer guides the model into the actual project.

The model must not require the active project name to be hardcoded in upper layers.

The model must discover the active project from this folder’s numbered files, non-numbered folders, file contents, project identity files, and current conversation.

---

# This File Is A Gate, Not The Whole Project

This file does not replace the actual project.

This file explains how to find and understand the actual project.

The actual project may be:

- directly represented by files in this folder
- contained inside one non-numbered project folder
- spread across multiple non-numbered project folders
- minimal and still being bootstrapped
- mature and governed by its own local numbered standards
- migrated from an older structure
- a software project, research project, learning project, knowledge base, writing project, operational system, or mixed project

The model must not stop at this seed file when the user request is project-specific.

It must continue discovery.

---

# Project Instance Root Tunnel

Numbered root files directly inside this folder form the project instance root tunnel.

A numbered root file begins with a numeric prefix from 00 to 99.

This file is one such root file.

A reinforcement file may also exist at the end of the local sequence.

Example local entry pattern:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      project_or_content_folder/

The exact number of files may vary.

The model must account for existing numbered root files in numeric order.

Missing numbers do not break the tunnel.

The model must not rely only on registered names.

Numeric prefix determines traversal order.

File name suggests responsibility.

File content confirms actual purpose.

---

# Non-Numbered Content After Root Tunnel

After numbered root files in this folder are accounted for, any non-numbered file or folder should be treated as project content or a project candidate unless clearly classified otherwise.

Non-numbered content may include:

- a named project folder
- multiple project folders
- product branches
- research folders
- knowledge folders
- learning modules
- documentation folders
- raw references
- source material
- implementation notes
- project artifacts
- local standards
- drafts or placeholders

The model must not ignore non-numbered content merely because it is not explicitly registered in this file.

The model must inspect non-numbered content dynamically according to the user’s request.

---

# Active Project Discovery Without Explicit Name

The model must not require the project name to be stated explicitly by the user or hardcoded in this file.

If this folder contains exactly one non-numbered folder, treat that folder as the active project candidate by default.

If this folder contains multiple non-numbered folders, infer the active project or branch from:

- current conversation
- folder names
- project identity files
- numbered local standards
- recently referenced artifacts
- repository structure
- target file path
- project terminology
- user intent

Ask one focused question only if ambiguity materially changes the output.

The model must not fail merely because the project name is not predeclared.

---


## Dedicated Project Folder Meaning

`02_MY_PROJECT/` is not itself the business, software, or product project. It is a project-instance container that may hold one or more actual project folders.

When a project folder is discovered under `02_MY_PROJECT/`, that folder is the project boundary for project-local documentation, codebase folders, database folders, infrastructure folders, scripts, tests, and project-specific tunnel/control-plane files.

Therefore, phrases such as "inside the project", "within the project", "project docs", "project backend", or "project codebase" must be interpreted as inside the discovered project folder, not inside the `02_MY_PROJECT/` container itself.

Example:

```text
02_MY_PROJECT/
  <project_folder>/        # actual project boundary
    00_PROJECT_TUNNEL/     # local project tunnel/control plane when present
    docs/                  # project/product/developer documentation
    backend/               # backend implementation when the project is software
    frontend/              # frontend implementation when the project is software
    database/              # schemas, migrations, seeds, read models
```

The model must not place a project codebase directly beside the project folder when the user says "inside the project". It must place it inside the discovered project folder.

## Dedicated Project Tunnel Folder Rule

A mature project folder may keep its local numbered tunnel inside a dedicated entry folder such as `00_PROJECT_TUNNEL/`, `00_PROJECT_ENTRY/`, or an equivalent explicitly named project-control folder.

When such a dedicated local tunnel folder exists, the model must treat that folder as the project-local control plane and read its numbered files before editing `docs/`, `backend/`, `frontend/`, `database/`, `infra/`, `scripts/`, or `tests/` inside the same project folder.

This dedicated project tunnel is not ordinary documentation. It is the project-local operating control plane.

# Discovered Project Folder Rule

When the model discovers a non-numbered project folder inside this layer, and the user request is project-specific, the model must enter that folder.

Inside the discovered project folder, the model must check for numbered root files.

If numbered root files exist, they form the project-local tunnel.

The model must account for that project-local tunnel before inspecting deeper project content.

Example:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/
        00_<PROJECT>_COGNITION_AND_TRACEABILITY_STANDARD.md
        01_<PROJECT>_IDENTITY_AND_OBJECTIVES.md
        02_<PROJECT>_DOMAIN_OR_STATE_TAXONOMY.md
        03_<PROJECT>_EVENT_OR_PROCESS_TAXONOMY.md
        project_content_or_branches/

In this pattern, this seed file does not need to know the project name in advance.

The model discovers the project folder, enters it, reads its local numbered standards, then explores project content dynamically.

---

# Local Numbered Tunnel Rule

Any relevant folder inside the project may contain its own numbered root files.

These files form a local tunnel for that folder.

Local tunnels may exist inside:

- discovered project folder
- product surface folder
- dashboard folder
- module folder
- research area
- knowledge domain
- learning module
- workflow family
- implementation branch
- artifact family

When the user targets a folder, module, artifact, or branch, the model must check whether that target path or relevant parent path contains numbered root files.

If local numbered files exist, they are governing context for that local area.

The model must account for them before generating, revising, judging, or auditing non-numbered content inside that area.

---

# Project-Local Performance Engineering Rule

The project instance is not only a storage area.

It is the place where tunnel discipline becomes project-specific reasoning.

When the model works inside a project, the same performance-engineering principles apply to local project files:

- understand the artifact or branch objective,
- detect whether a weakness is local, structural, cross-artifact, or upper-layer,
- identify harmful duplication versus useful reinforcement,
- preserve accepted project meaning,
- strengthen the correct project owner before deleting weak duplicated content,
- move misplaced logic to the correct local owner when needed,
- repair missing links between local standards and artifacts,
- and choose the solution method that best advances the project without unnecessary disruption.

This rule helps the model improve existing projects, not only create new ones.

It applies to software projects, research projects, learning projects, documentation systems, knowledge bases, operational workflows, and mixed projects.

---

# Tunnel Before Dynamic Exploration

The model must distinguish between tunnel traversal and dynamic exploration.

Tunnel traversal means accounting for numbered root files that govern behavior, standards, project truth, branch rules, or artifact rules.

Dynamic exploration means inspecting non-numbered folders and files based on the user’s request.

Correct sequence inside this project instance:

1. Account for numbered root files in this folder.
2. Discover non-numbered project content or project candidates.
3. Enter the relevant project folder when the request is project-specific.
4. Account for numbered root files inside the discovered project folder.
5. Continue the same pattern for relevant branches, modules, or domains.
6. After local tunnels are accounted for, inspect non-numbered target content dynamically.
7. Use current conversation and accepted decisions as live input.
8. Answer or generate from cumulative context.

The model must not jump directly to deep project files while skipping governing numbered files.

The model must not scan unrelated files when the request is focused.

---

# Project Files Should Be Locally Understandable

Project-specific files should be understood from local project context.

They do not need to repeat exact paths to the upper behavior or orchestration layers.

The upper layers are responsible for routing the model into this project instance.

This project instance is responsible for preserving project-specific truth.

A project folder is responsible for defining its own local identity, standards, structure, terminology, decisions, and artifacts.

This keeps projects portable and prevents upper-layer architecture from polluting project-specific documentation.

---

# Project Truth Sources

When working inside this project instance, the model should prioritize project-specific truth from:

1. numbered root files in this project instance
2. discovered project folder numbered files
3. local numbered files in relevant branches
4. project identity and objective files
5. project structure files
6. project knowledge files
7. project decision files
8. target artifact content
9. parent, child, and sibling artifacts when relevant
10. current conversation and latest user corrections
11. general project orchestration method
12. general knowledge only as support

Do not answer project-specific questions from general method alone when project truth exists.

Do not present inferred project truth as documented truth.

---

# Minimal Project Instance Is Valid

This project instance may contain only this seed file and a reinforcement file.

That is valid.

A minimal project instance means the project is ready to grow.

It does not mean the repository is broken.

If no project content exists yet, the model should help bootstrap the project from conversation.

If project content exists but standards are minimal, the model should extract project signals carefully and propose the smallest useful next standard.

Do not create many empty files only to simulate maturity.

---


# Empty Project Slot Is Valid

This folder may intentionally contain only the two root guard files.

That means the project instance layer is available as a stable destination for future project truth, even if no project folder or project content exists yet.

When no non-numbered project content exists, the model must not search for a missing project name, assume an old project, or behave as if the repository is incomplete.

Instead, it must treat the current conversation as the live working surface and use the upper layers to provide disciplined expert assistance.

If the user is using the environment like a SaaS project-building assistant without saving files yet, the model should still operate with project-quality reasoning:

- infer intent from the latest input and connected conversation,
- activate relevant domain alphabets and standards,
- identify the likely project type and maturity,
- propose a suitable project-local standard only when continuity needs it,
- avoid forcing file creation when the user wants discussion or consultation,
- avoid claiming persistent project truth that has not been stored or accepted.

---

# Project Content May Exist Before Standards

A project may contain content folders before project standards are complete.

This is common.

The model should:

- inspect relevant content when available
- classify content intent
- extract implicit standards
- recommend formal standards when repeated logic appears
- preserve useful raw material
- avoid treating weak standards as project failure
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

The model must classify the intent before judging.

Possible classifications:

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

This project instance may represent different types of work.

It may become:

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

Project artifacts must match project type and user intent.

---

# Identity May Be Missing

The project identity may not exist yet.

That is acceptable.

If identity is missing, the model should extract identity signals from:

- folder names
- current conversation
- project-local numbered files
- raw references
- existing artifacts
- repeated terminology
- user corrections
- project objectives
- domain content

The model may propose a provisional identity.

It must not invent a final identity.

---

# Objectives May Be Missing

Project objectives may not exist yet.

That is acceptable.

If objectives are missing, the model should extract objective signals from:

- user goals
- repeated concerns
- project artifacts
- project scope
- desired outcomes
- quality expectations
- documentation needs
- knowledge needs
- execution needs
- current conversation

Do not confuse files, folders, features, or artifacts with objectives.

A file is a tool.

An objective explains why the tool matters.

---

# Structure May Be Missing

A project structure index may not exist yet.

That is acceptable.

If the project contains multiple folders, branches, modules, chapters, knowledge areas, workflows, or artifact families, the model should recommend a structure index when useful.

A structure index should explain responsibilities and navigation.

It should not merely list folders.

---

# Knowledge May Be Missing

A project knowledge map may not exist yet.

That is acceptable.

If the project depends on domain knowledge, research, sources, terminology, current facts, high-stakes information, or learning structure, the model should recommend a knowledge map when useful.

Do not treat general knowledge as project-specific truth unless accepted by the project.

---

# Decisions May Be Missing

A project decision log may not exist yet.

That is acceptable.

If important decisions are accumulating, the model should recommend decision memory.

Project decisions may include:

- identity
- objectives
- scope
- naming
- structure
- taxonomy
- standards
- roadmap
- artifact sequence
- source policy
- implementation assumptions
- rejected directions

Important decisions should not disappear in conversation.

---

# Roadmap May Be Missing

A project roadmap may not exist yet.

That is acceptable.

If sequencing matters, the model should recommend or create a roadmap when useful.

A roadmap answers what should happen first and why.

A roadmap is not the same as folder structure.

Numeric tunnel order is not automatically execution priority.

---

# Cumulative Context Rule

The model must answer from cumulative context.

Cumulative context includes:

- upper-layer behavior and project-building methods already applied before reaching this file
- numbered files in this project instance
- discovered project folder standards
- branch-local standards
- current conversation
- accepted decisions
- user corrections
- target artifact content
- parent, child, sibling, structure, knowledge, roadmap, and decision context when relevant

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
- decide whether user decision is needed
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

When such failure occurs, correct the route and continue.

---

# Final Principle

This file is the project instance gate.

It ensures the model does not stop too early, does not require a hardcoded project name, and does not ignore local project tunnels.

The project should be understood from its own files, folders, standards, artifacts, and current conversation.

The model must enter the relevant project, read its local numbered standards, then explore dynamically according to the user’s goal.

A strong project instance entry makes future work cumulative, accurate, and project-native.