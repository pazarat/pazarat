# NUMBERED TUNNEL DISCOVERY AND LAYER HANDOFF

# Purpose

This file defines how the model should discover numbered repository layers, traverse numbered root files, and hand off responsibility from the cognitive runtime layer to later layers.

It is part of the cognitive runtime layer.

It is not a project file.

It is not a project-management method file.

It is not a project identity document.

It is not a project status report.

It must not store fixed claims about any current project, folder, file, maturity, weakness, strength, or priority.

Its purpose is to prevent the model from skipping important layers or files when repository structure evolves.

The model must use current folder contents and numeric ordering, not only remembered paths or explicitly registered file lists.

---

# Core Principle

The tunnel is discovered from the current repository.

Numbers define traversal order.

File and folder names explain responsibility.

Content confirms purpose.

The model must not depend on hardcoded file lists as the source of truth.

A registered list may guide the model, but the actual current numbered folders and numbered root files determine the active tunnel.

---

# What This File Owns

This file owns cognitive-level tunnel behavior.

It defines:

- how to discover numbered layer folders
- how to identify numbered root files inside a layer
- how to sort tunnel entries
- how to avoid skipping newly added files
- how to hand off from the cognitive layer to project orchestration
- how to hand off from project orchestration to project instance
- how to treat non-numbered files and folders after the tunnel
- how to remain flexible across different project types
- how to handle missing, partial, legacy, or evolving structures

This file does not define:

- project identity
- project objectives
- project maturity
- project documentation hierarchy
- PRD structure
- screen standards
- workflow standards
- project-specific taxonomy
- project-specific folder tree
- implementation strategy

Those belong to project orchestration or project instance layers.

---

# Numbered Folder Tunnel

A numbered folder is a folder whose name begins with a numeric prefix.

Examples:

```text
00_COGNITIVE_RUNTIME/
01_PROJECT_ORCHESTRATION/
02_MY_PROJECT/
```

The folder number defines tunnel order.

The folder name explains the layer role.

The model should discover numbered folders from the actual current repository.

The model must not assume that only previously known folder names are valid.

If a new numbered folder appears, it must be considered part of the tunnel unless it is clearly obsolete, backup, temporary, unrelated, or outside the active repository scope.

---

# Expected High-Level Layer Pattern

The preferred modern architecture is:

```text
00_COGNITIVE_RUNTIME/
01_PROJECT_ORCHESTRATION/
02_MY_PROJECT/
```

## 00_COGNITIVE_RUNTIME

Model cognition and behavior layer.

It defines how the model synchronizes, preserves context, detects intent, uses evidence, avoids drift, handles uncertainty, and hands off work.

## 01_PROJECT_ORCHESTRATION

General project-building and project-organization layer.

It defines how the model turns raw input into structured project understanding, proposes standards, extracts goals, organizes knowledge, and prepares the project instance.

## 02_MY_PROJECT

The active project instance layer.

It contains the specific project’s standards, identity, structure, decisions, artifacts, and project content.

It may be minimal at first.

It may later become a full project such as a software platform, academic research project, learning system, knowledge base, operational system, documentation workspace, or any other structured body of work.

---

# Numbered File Tunnel

Inside each numbered layer folder, numbered root files form that layer’s internal tunnel.

A numbered root file is a file located directly inside the layer folder and beginning with a numeric prefix.

Examples:

```text
00_COGNITIVE_ENTRY_AND_CONTEXT_SYNCHRONIZATION.md
01_USER_INTERACTION_AND_BEHAVIOR_DIRECTIVES.md
02_NUMBERED_TUNNEL_DISCOVERY_AND_LAYER_HANDOFF.md
99_COGNITIVE_RUNTIME_REINFORCEMENT_MEMORY.md
```

The file number defines reading and traversal priority.

The file name explains responsibility.

The file content confirms the actual function.

The model must not judge responsibility from file name alone.

The model must not skip numbered root files because they are not mentioned in another file.

---

# Tunnel Range

The default tunnel range is:

```text
00 through 99
```

Files or folders beginning with numbers in this range are potential tunnel entries.

The range does not require every number to exist.

A valid tunnel may contain:

```text
00
01
02
05
13
99
```

Missing numbers do not break the tunnel.

The model should traverse existing numbered entries in numeric order.

The tunnel ends for a layer when no more numbered root files exist directly inside that layer folder.

---

# Numeric Order Beats Memory Order

The model must prefer numeric order over remembered order.

If older instructions list files in a different order, use current numeric order.

If a new file is added, include it according to its prefix.

If two files share the same numeric prefix, inspect both and identify whether this is intentional, duplicate, temporary, conflicting, or a naming problem.

If the file name and content disagree, content determines responsibility, while numeric prefix determines traversal position.

---

# Registered Lists Are Not The Tunnel

Explicit file lists are useful but incomplete by design.

The model may use them as documentation.

However, the active tunnel is determined by current numbered folder and file discovery.

Incorrect behavior:

- reading only files explicitly named in an older guide
- skipping a new numbered file because it was not listed elsewhere
- assuming a folder is irrelevant because its name changed
- jumping directly to a deep project artifact before accounting for numbered layers
- treating a registered list as more authoritative than current folder contents

Correct behavior:

- discover numbered folders
- sort them by numeric prefix
- enter each relevant numbered layer
- discover numbered root files
- sort them by numeric prefix
- account for their guidance
- hand off to the next layer
- branch dynamically only after the relevant tunnel is complete

---

# Mandatory High-Level Tunnel Sequence

When the modern layer folders exist and the request is project-related or repository-related, the expected sequence is:

```text
00_COGNITIVE_RUNTIME/
→ numbered root files in 00_COGNITIVE_RUNTIME/

01_PROJECT_ORCHESTRATION/
→ numbered root files in 01_PROJECT_ORCHESTRATION/

02_MY_PROJECT/
→ numbered root files in 02_MY_PROJECT/

then:
→ non-numbered project folders and files relevant to the request
```

The cognitive layer must not jump directly into the project instance if project orchestration is present and relevant.

The project orchestration layer must not be skipped when the request involves project building, project organization, raw ideas, project standards, structure, maturity, roadmap, or documentation method.

The project instance layer must not be skipped when the request concerns a specific project or its artifacts.

---

# Recursive Numbered Tunnel Rule

The numbered tunnel is not limited to the first three repository layers.

The model must understand numbered tunnels as a recursive repository pattern.

A numbered tunnel may exist at:

- repository layer level
- cognitive runtime layer
- project orchestration layer
- project instance root
- discovered project folder
- project branch folder
- module folder
- domain folder
- artifact family folder

Any folder may contain numbered root files from `00` to `99`.

When the model reaches a folder that is relevant to the current task, it must check whether that folder contains numbered root files.

If numbered root files exist, they form a local tunnel for that folder.

The model must account for those numbered files in numeric order before treating the remaining non-numbered files and folders as dynamic content.

Numeric order defines traversal order.

File name suggests responsibility.

File content confirms actual purpose.

This rule allows a project to define its own internal standards, module standards, branch standards, or artifact-family standards without requiring the upper layers to know their names in advance.

---

# Project Instance Content Discovery Rule

When the model enters the project instance layer, it must not depend on a hardcoded project name.

The project instance layer may be named generically, such as:

    02_MY_PROJECT/

Inside that layer, the model must first account for numbered root files if they exist.

After the numbered root files are accounted for, any non-numbered file or folder is project content or a project candidate unless clearly classified otherwise.

If the project instance layer contains exactly one non-numbered folder, the model should treat that folder as the active project candidate by default.

If the project instance layer contains multiple non-numbered folders, the model should use the current conversation, folder names, project identity files, and relevant content to infer which project or branch is active.

If ambiguity remains and materially affects the output, ask one focused question.

The model must not fail merely because the project name was not explicitly registered in the upper layers.

The model should discover the project from structure and content.

---

# Discovered Project Folder Tunnel Rule

When a non-numbered project folder is discovered inside the project instance layer, the model must inspect whether that folder contains numbered root files.

Example pattern:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/
        00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
        01_<PROJECT>_IDENTITY_AND_OBJECTIVES.md
        02_PLATFORM_STATE_TAXONOMY.md
        03_PLATFORM_EVENT_TAXONOMY.md

In this pattern, the model must not stop at `02_MY_PROJECT/`.

It must continue into the discovered project folder when the user request is project-specific.

Inside the discovered project folder, numbered root files form the project’s local tunnel.

The model must account for that local tunnel before inspecting deeper project folders such as dashboards, web, mobile, modules, workflows, PRDs, research folders, or implementation notes.

This lets the project define its own standards without requiring the upper layers to explicitly name the project.

---

# Fourth Tunnel And Deeper Tunnel Rule

A project may contain a fourth tunnel or deeper local tunnels.

A fourth tunnel is any numbered local standard sequence inside the project after the main project instance tunnel.

Examples may include:

- a project folder tunnel
- a dashboard folder tunnel
- a module folder tunnel
- a research area tunnel
- a knowledge domain tunnel
- a workflow family tunnel
- a UI or implementation branch tunnel

When the user request targets a branch, module, domain, artifact family, or folder, the model must check for local numbered root files in that target path.

If such files exist, the model must treat them as local governing context.

The model must account for local governing context before generating, revising, judging, or auditing files inside that branch.

This prevents the model from ignoring project-specific or branch-specific standards.

---

# Tunnel Before Dynamic Exploration Rule

The model must distinguish between tunnel traversal and dynamic exploration.

## Tunnel Traversal

Tunnel traversal means reading or accounting for numbered root files that govern behavior, method, project standards, or local branch rules.

This is mandatory when relevant.

## Dynamic Exploration

Dynamic exploration means inspecting non-numbered files and folders based on the current user request.

This is contextual.

The correct sequence is:

1. account for the repository-level numbered layer tunnel
2. account for numbered root files in each relevant layer
3. enter the project instance layer
4. account for project instance numbered root files
5. discover non-numbered project candidates or project content
6. enter the relevant discovered project folder when project-specific work is requested
7. account for numbered root files in the discovered project folder
8. continue the same pattern for any relevant branch or module
9. only then inspect non-numbered dynamic content according to user intent

The model must not skip governing numbered files and jump directly to deep content.

The model must not scan every dynamic file when the user only needs a focused answer.

The tunnel gives the model the governing standards.

Dynamic exploration gives the model the target context.

Both are required at the correct depth.

---

# Project Files Should Not Depend On Upper Layer Paths

Once the model reaches a project-specific folder, project files should be understood from their local project context.

Project-specific files should not need to repeat or depend on exact paths to the cognitive runtime or project orchestration layers.

The upper layers are responsible for guiding the model into the project.

The project layer is responsible for defining project truth.

A project file may define its own local standards, local structure, local terminology, local artifacts, and local rules.

It should not need to restate the full upper-layer architecture unless the project itself is about that architecture.

This keeps project files portable and prevents upper-layer paths from polluting project-specific documentation.

---

# Cumulative Context After Tunnel Rule

After completing the relevant tunnel traversal, the model must produce answers from cumulative context.

Cumulative context includes:

- cognitive runtime behavior rules
- project orchestration method rules
- project instance standards
- discovered project folder standards
- local branch standards
- current conversation
- latest user correction
- accepted decisions
- relevant target artifacts
- related parent, child, sibling, roadmap, knowledge, or decision context

The model must not answer as if each request is isolated.

The model must not forget prior accepted corrections or decisions.

The model must compare the latest user message with repository context and accumulated conversation context before responding.

A correct answer should be the result of layered understanding, not a fresh generic response.

---

# Tunnel Failure Escalation Rule

If the user reports that the model missed context, misunderstood the project, ignored a branch, skipped a standard, or answered generically, the model should suspect a tunnel traversal failure.

Common tunnel failures include:

- stopping at `02_MY_PROJECT/` without entering a discovered project folder
- ignoring numbered files inside a project folder
- ignoring local numbered files inside a branch
- relying on hardcoded project names
- treating non-numbered project folders as irrelevant
- answering from project orchestration without project instance truth
- answering from project instance root without discovered project folder truth
- using dynamic content without first accounting for local standards

When a tunnel failure is detected, the model must correct the route, account for the missed tunnel, and continue with the right project context.

---

# Context-Aware Tunnel Depth

The tunnel is mandatory as a method.

Depth is context-aware.

## Light Tunnel Pass

Use for simple questions or general conversation.

The model should still preserve awareness that the tunnel exists but should not over-traverse or over-narrate.

## Focused Tunnel Pass

Use for a specific project, file, section, artifact, scenario, correction, or next-step decision.

The model should account for the relevant numbered layers and target branch.

## Deep Tunnel Pass

Use for repository audit, architecture redesign, file generation, project bootstrap, maturity assessment, migration, conflict resolution, or behavior diagnosis.

The model should explicitly verify layer responsibilities and current structure when needed.

## Full Tunnel Pass

Use when the user asks to inspect the whole repository, validate the tunnel, redesign the architecture, or diagnose why the model skipped context.

The model may discuss the tunnel explicitly in this mode.

---

# Silent Traversal Rule

The tunnel should usually remain invisible in normal responses.

Silent traversal means the model applies the tunnel without narrating it.

Silent traversal does not mean skipped traversal.

Do not begin normal answers with:

- I entered the tunnel
- I inspected layer 00
- I read the numbered files
- the tunnel says
- according to file X

unless the user asks for audit, diagnosis, traceability, repository health, or file validation.

The user should see the benefit of the tunnel through accurate, grounded, context-aware answers.

---

# Handoff From Cognitive Runtime To Project Orchestration

The cognitive layer must hand off to project orchestration when the request involves:

- organizing raw ideas
- turning scattered input into structured understanding
- deciding whether something is a project
- extracting project identity
- extracting objectives
- creating or improving project standards
- proposing a project structure
- planning documentation
- assessing project maturity
- classifying artifact intent
- building a roadmap
- deciding what files should exist
- deciding whether a project instance should be created or expanded

The cognitive layer must not absorb these responsibilities as if they were pure model behavior.

It should detect the need and route to project orchestration.

---

# Handoff From Project Orchestration To Project Instance

Project orchestration must hand off to the project instance when the request concerns:

- a specific project
- project-specific standards
- project-specific identity
- project-specific objectives
- project-specific taxonomy
- project-specific structure
- project-specific decisions
- project-specific files
- project-specific artifacts
- project branches or modules
- project content generation or revision

The project instance layer is where project truth lives.

Project orchestration provides the method.

The project instance provides the actual project context.

---

# Project Instance Tunnel

The project instance layer may contain numbered root files.

These numbered root files form the project-specific tunnel.

Examples may include:

```text
00_PROJECT_STANDARD_SEED.md
01_PROJECT_IDENTITY_AND_OBJECTIVES.md
02_PROJECT_DOMAIN_TAXONOMY.md
03_PROJECT_EVENT_TAXONOMY.md
04_PROJECT_STRUCTURE_TREE_INDEX.md
99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
```

The model must not assume all these files exist.

The model must use what currently exists.

If only seed files exist, the project is in bootstrap mode.

If many standards exist, the project has a stronger project-specific tunnel.

If non-numbered folders exist after the numbered tunnel, treat them as project content unless classified otherwise.

---

# Non-Numbered Project Content

After the numbered root files inside a project instance are accounted for, non-numbered folders and files are usually project content.

They may include:

- product folders
- dashboards
- websites
- mobile apps
- modules
- domains
- research areas
- chapters
- lessons
- policies
- PRDs
- workflows
- screen documents
- implementation notes
- knowledge files
- raw references

The model should inspect non-numbered project content dynamically based on user intent.

Do not inspect everything for every small request.

Do not ignore non-numbered content when it is the target of the request.

---

# Minimal Project Instance Is Valid

A project instance may start with only:

```text
02_MY_PROJECT/
  00_PROJECT_STANDARD_SEED.md
  99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
```

This is valid.

The model must not treat it as a broken repository.

It means the system has reached the project instance layer and can now help the user build project-specific standards from raw input.

The absence of detailed standards should trigger bootstrap support, not failure.

---

# No Project Instance Behavior

If no project instance layer exists, the model should not invent one as current reality.

It may propose creating one if the user’s intent suggests project building.

The model can still provide high-quality help without a project instance.

The absence of a project folder does not prevent:

- discussion
- brainstorming
- reasoning
- learning
- strategy
- planning
- early idea capture

But persistent project work benefits from a project instance layer.

---

# Legacy Structure Compatibility

Older repositories may use different names, such as:

```text
AI_COGNITIVE_RUNTIME/
ACTIVE_PROJECT/
ACTIVE_PROJECT/<project_folder>/
```

The model may recognize legacy structures during migration or audit.

However, the preferred modern architecture uses numbered layer folders.

If both structures exist, the model should identify the active structure from current repository evidence and user instruction.

Do not merge legacy and modern structures blindly.

Do not treat legacy paths as current truth if the repository has migrated.

---

# Layer Ownership Detection

The model must infer layer ownership from both location and content.

A file belongs in the cognitive layer if it mainly defines model behavior.

A file belongs in project orchestration if it mainly defines how to build, organize, assess, or manage projects.

A file belongs in the project instance if it defines project-specific standards, project content, domain logic, artifacts, or implementation details.

If a useful rule is found in the wrong layer, preserve the rule but move or reframe it in the appropriate layer during redesign.

Do not delete valuable guidance merely because it was previously misplaced.

---

# Misplaced Responsibility Signals

Possible signs that a file is in the wrong layer:

- a cognitive file defines project-specific UI standards
- a cognitive file teaches PRD hierarchy in detail
- a project orchestration file contains a specific product identity
- a project orchestration file hardcodes one project as the only expected project
- a project instance file defines general model behavior
- a project instance file repeats general orchestration rules instead of project-specific standards

These signals do not mean the content is useless.

They mean the responsibility may need relocation or abstraction.

---

# Project-Specific Standards Are Not General Rules

Project-specific standards belong in the project instance layer.

Examples:

- the identity of a specific project
- a specific platform’s state taxonomy
- a specific product’s event taxonomy
- a specific project’s screen style rules
- project-specific PRD traceability rules
- project-specific implementation assumptions
- domain-specific vocabulary unique to one project

The project orchestration layer may define how such standards are created, but it should not hardcode one project’s standards as universal.

---

# General Project Method Is Not Project Content

Project orchestration files may define how to:

- extract identity
- clarify objectives
- organize structure
- assess maturity
- propose standards
- plan delivery
- manage decisions
- classify artifacts

These methods are general.

They should not be treated as the content of a specific project.

---

# Tunnel Failure Detection

A tunnel failure may occur when the model:

- skips a numbered layer
- skips a numbered root file
- jumps directly to a deep artifact
- treats a project instance as absent without checking
- relies on an old list instead of current folder contents
- ignores a newly added numbered file
- uses project-specific content as a general rule
- uses project orchestration rules as project truth
- gives a generic answer when a project instance exists
- over-narrates the tunnel instead of using it

When a tunnel failure is detected, the model should correct the route and continue.

---

# Missing Access Behavior

If the model cannot inspect the repository, folder, or file needed for the task, it must not pretend that it did.

It should state the limitation only when it affects the answer.

If a user requests a file generation based on missing current structure, the model may generate a proposed file, clearly treating it as proposed rather than repository-verified.

---

# Copy-Safe Generation Reminder

When generating complete repository files, preserve copy-block integrity.

Use one complete copy-safe block.

For Markdown files that contain internal fenced examples, use an outer fence longer than the internal fences.

This prevents file content from spilling outside the block.

This file does not own output formatting in detail, but it reinforces the rule because broken generation can corrupt repository updates.

---

# Final Principle

The numbered tunnel is the backbone of repository-based cognition.

The model must discover it from current structure, traverse it in numeric order, hand off responsibilities across layers correctly, and branch dynamically only after the relevant tunnel has been accounted for.

The goal is not to recite the tunnel.

The goal is to make the model reliably use all governing context before producing useful answers, files, analysis, or decisions.