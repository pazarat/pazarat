# PROJECT INSTANCE HANDOFF AND DYNAMIC DISCOVERY

# Purpose

This file defines how the model should hand off from the general project orchestration layer into the active project instance layer, then dynamically discover project-specific standards, content, folders, artifacts, and relevant context.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific structure map.

It is not a static repository map.

It is not a project status report.

It must not store fixed claims about any current project, artifact, folder, file, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define the general method for entering the project instance layer and discovering what exists there without relying only on hardcoded file lists, old assumptions, or explicit registration.

The project orchestration layer defines the handoff and discovery method.

The project instance layer contains the actual project truth.

---

# Core Principle

The project instance is where project truth lives.

The model must not stop at the cognitive runtime layer.

The model must not stop at the project orchestration layer when the user asks about a specific project.

The model must hand off into the project instance layer when project-specific truth, artifacts, standards, folders, or decisions are needed.

After entering the project instance, the model must discover current structure dynamically.

Numeric tunnel files guide entry.

Non-numbered folders and files after the tunnel are project content.

Current content beats old assumptions.

---

# What This File Owns

This file owns the project-orchestration method for project instance handoff and dynamic discovery.

It defines:

- when to enter the project instance layer
- how to identify the active project instance
- how to read the project-specific numbered tunnel
- how to treat minimal project instances
- how to discover non-numbered project content
- how to classify folders and files dynamically
- how to avoid relying on hardcoded file lists
- how to handle multiple possible project layouts
- how to distinguish standards from content
- how to inspect only what matters
- how to handle missing, partial, legacy, or migrated project instances
- how to use project-specific standards without polluting upper layers

This file does not own:

- the actual identity of a specific project
- the actual project structure tree
- the actual project standards
- the actual project artifacts
- the actual project roadmap
- the actual project maturity status
- the actual project decisions
- project-specific implementation content

Those belong in the project instance layer or current project response when explicitly assessed.

---

# Handoff Definition

Handoff means shifting from general method to project-specific context.

The cognitive runtime detects the user’s intent and selects the response mode.

The project orchestration layer determines the general method.

The project instance layer provides the actual project truth.

A correct handoff means:

- do not answer project-specific questions from general rules alone
- do not invent project truth from project orchestration methods
- do not ignore project-specific standards when available
- do not treat missing project standards as system failure
- do not assume non-numbered folders are irrelevant
- do not inspect everything when only one branch matters
- do inspect relevant current content before making project-specific claims

---

# When To Enter Project Instance

Enter the project instance layer when the user asks about:

- a specific project
- project-specific standards
- project-specific files
- project structure
- project folders
- project artifacts
- project PRDs
- project workflows
- project decisions
- project roadmap
- project knowledge
- project implementation
- project modules
- project screens
- project content branches
- project audit
- project migration
- project maturity
- project-specific next step

If the user is only discussing general method, stay in project orchestration.

If the user is only discussing model behavior, stay in cognitive runtime.

---

# Active Project Instance Identification

The active project instance is usually the numbered layer after project orchestration.

Preferred modern pattern:

    00_COGNITIVE_RUNTIME/
    01_PROJECT_ORCHESTRATION/
    02_MY_PROJECT/

The project instance may keep the generic folder name:

    02_MY_PROJECT/

Or it may be renamed to a project-specific folder:

    02_<PROJECT_NAME>_PROJECT/
    02_RESEARCH_PROJECT/
    02_LEARNING_SYSTEM/

The numeric prefix indicates layer order.

The folder name explains responsibility.

The model must identify the active project instance from current repository structure and current user context.

Do not assume the project instance is always named one exact name.

---

# Project Instance Numbered Tunnel

Inside the project instance layer, numbered root files form the project-specific tunnel.

Examples may include:

    00_PROJECT_STANDARD_SEED.md
    01_PROJECT_IDENTITY_AND_OBJECTIVES.md
    02_PROJECT_DOMAIN_AND_STATE_TAXONOMY.md
    03_PROJECT_EVENT_TAXONOMY.md
    04_PROJECT_STRUCTURE_TREE_INDEX.md
    05_PROJECT_KNOWLEDGE_MAP.md
    06_PROJECT_PRIMITIVES_AND_SHARED_RULES.md
    07_PROJECT_DECISION_LOG.md
    08_PROJECT_DELIVERY_ROADMAP.md
    99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md

These names are examples.

The model must not require this exact list.

The model must discover existing numbered root files and account for them in numeric order.

The numeric prefix determines traversal order.

The file name suggests responsibility.

The content confirms responsibility.

---

# Minimal Project Instance Is Valid

A project instance may contain only:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md

This is valid.

It means the project instance exists but is still in bootstrap or early formation.

The model must not treat this as broken.

A minimal project instance should trigger careful project-standard development when the user wants durable project work.

Do not invent missing standard files as if they already exist.

Do not refuse to help because standards are minimal.

Use the minimal layer as a seed for growth.

---


# Empty Project Slot And Conversation-Grounded Work

A project instance may be intentionally minimal because the environment is being used like a SaaS-style expert project assistant rather than as a filled repository.

When `02_MY_PROJECT/` contains only root guard files and no discovered project folder, the model must treat it as an empty project slot, not as a broken project and not as a named project.

In this state, project-aware work should be grounded in:

1. the latest user input,
2. connected conversation history and accepted corrections,
3. cognitive runtime rules,
4. project orchestration methods,
5. the project instance guard files,
6. stable domain knowledge or verified external knowledge when required.

The model may still provide high-quality project planning, consultation, diagnosis, documentation drafts, knowledge maps, or bootstrap proposals.

The model must not invent a project folder, identity file, taxonomy, roadmap, or project-local standard as if it already exists.

If the conversation becomes durable project work, the model should propose the smallest useful project-local seed, such as identity and objectives, knowledge map, documentation standard, structure index, or execution-readiness standard depending on the project type.

---

# No Project Instance Behavior

If no project instance exists, do not invent one as current reality.

The model may still help with:

- discussion
- brainstorming
- learning
- strategy
- planning
- project candidate assessment
- bootstrap proposal
- first standard layer recommendation

If the work appears durable, recommend creating a project instance.

If the user wants one, project orchestration may propose or generate the seed files.

Until then, avoid claiming project-instance-backed continuity.

---

# Project Instance Standard Files

Project instance standard files define local project truth.

They may include:

- project identity
- objectives
- scope
- non-scope
- project principles
- domain taxonomy
- state taxonomy
- event taxonomy
- structure tree
- knowledge map
- decision log
- primitives
- artifact standards
- roadmap
- reinforcement memory

Project-specific standards govern project artifacts.

They should not be treated as optional when the user asks for project-specific work.

---

# Non-Numbered Project Content

After the project-specific numbered tunnel is accounted for, non-numbered folders and files are usually project content.

Project content may include:

- product areas
- dashboards
- web application folders
- mobile application folders
- backend folders
- research folders
- knowledge folders
- modules
- domains
- chapters
- lessons
- workflows
- screens
- implementation notes
- raw references
- source material
- data files
- design notes
- output artifacts

The model must inspect project content dynamically according to user intent.

Do not ignore non-numbered content because it is not listed in the standard files.

Do not inspect all content for every small request.

---

# Multiple Layout Support

The project instance may use different layouts.

## Direct Branch Layout

The project instance contains standard files and direct project branches.

    02_MY_PROJECT/
      numbered standards...
      A_dashboards/
      B_web_frontend/
      C_mobile_app/

## Named Project Folder Layout

The project instance contains standard files and one named project folder.

    02_MY_PROJECT/
      numbered standards...
      <project_folder>/
        A_dashboards/
        B_web_frontend/
        C_mobile_app/

## Knowledge Project Layout

The project instance contains standards and knowledge branches.

    02_MY_PROJECT/
      numbered standards...
      concepts/
      sources/
      syntheses/
      glossary/

## Research Project Layout

The project instance contains standards and research branches.

    02_MY_PROJECT/
      numbered standards...
      literature/
      methods/
      findings/
      drafts/

## Learning Project Layout

The project instance contains standards and learning branches.

    02_MY_PROJECT/
      numbered standards...
      curriculum/
      lessons/
      exercises/
      assessments/

The model must infer layout from current structure, file content, and user context.

Do not force all projects into one layout.

---

# Dynamic Discovery Method

When entering the project instance for a project-specific request, the model should:

1. identify the active project instance folder
2. account for numbered root files in numeric order
3. identify available project-specific standards
4. identify whether the project is minimal, emerging, structured, mature, or in migration
5. identify non-numbered folders and files
6. classify relevant folders by likely purpose
7. inspect target content when the user’s request points to it
8. compare target content with project standards
9. classify artifact intent and maturity when needed
10. answer or generate at the correct project level

Do not expose all steps unless the user asks for audit, diagnosis, or repository validation.

---
---

# Project Discovery Without Explicit Project Name

The model must not require the active project name to be registered in the upper layers.

A project instance layer may be generic.

Example:

    02_MY_PROJECT/

Inside that project instance layer, the active project may appear as one or more non-numbered folders or files after the project instance numbered tunnel.

Example:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/

In this case, `<project_folder>/` is a discovered project folder.

The model must infer project presence from structure and content, not only from explicit upper-layer naming.

If exactly one non-numbered folder exists inside the project instance layer, treat it as the active project candidate by default.

If multiple non-numbered folders exist, use:

- current conversation
- folder names
- project identity files
- project standards
- recently referenced artifacts
- relevant content
- user intent

to infer the active project or branch.

Ask one focused question only if ambiguity materially changes the output.

---

# Project Instance Root Guard Files

The project instance root should ideally contain guard files.

Recommended pattern:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      project_or_content_folder/

These guard files are not replacements for the actual project.

They are the project instance entry gate.

They should explain that non-numbered folders and files after the numbered tunnel are project content or project candidates.

The model must use these files to understand how to continue into the actual project content.

If the guard files are missing, the model must not stop or assume there is no project.

Missing guard files should be treated as a structure gap, not proof that the project is absent.

The model should continue by inspecting non-numbered project candidates when the user request is project-specific.

---

# Discovered Project Folder Handoff

When the model discovers a project folder inside the project instance layer, it must hand off into that folder when the user request is project-specific.

Example:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      <project_folder>/
        00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
        01_<PROJECT>_IDENTITY_AND_OBJECTIVES.md
        02_PLATFORM_STATE_TAXONOMY.md
        03_PLATFORM_EVENT_TAXONOMY.md
        A_dashboards/

The model must not stop at `02_MY_PROJECT/`.

It must enter `<project_folder>/` when the user is asking about the active project or when it is the only discovered project candidate.

Inside the discovered project folder, numbered root files form the project-local tunnel.

The model must account for those numbered files before inspecting deeper project folders.

---

# Project-Local Numbered Tunnel

A discovered project folder may contain its own numbered root files.

These files define project-local standards.

They may include:

- project identity
- product standards
- PRD standards
- taxonomy
- event model
- structure tree
- UI or design system standards
- implementation standards
- shared primitives
- decision memory
- roadmap
- reinforcement memory

The exact names are project-specific.

The model must not require a fixed list.

The model must discover existing numbered root files and account for them in numeric order.

The numeric prefix determines traversal order.

The file name suggests responsibility.

The content confirms actual purpose.

Project-local numbered files govern project-specific work.

They must be considered before generating, revising, judging, or auditing project artifacts.

---

# Fourth-Level And Deeper Local Tunnels

A project may contain local tunnels inside branches, modules, domains, artifact families, or content folders.

Examples may include:

- dashboard branch tunnel
- admin dashboard tunnel
- module tunnel
- workflow family tunnel
- research area tunnel
- knowledge domain tunnel
- implementation branch tunnel
- UI branch tunnel

When the user targets a specific project branch or artifact family, the model must check that target folder and its relevant parent folders for numbered root files.

If local numbered files exist, they are local governing context.

The model must account for local governing context before working on non-numbered files inside that branch.

This prevents branch-specific standards from being skipped.

---

# Project-Local Tunnel Performance Continuity

Tunnel-performance discipline must continue after handoff into the project instance.

When the model enters a project-local numbered tunnel, branch-local tunnel, module tunnel, research tunnel, documentation tunnel, or artifact family, it must use the same engineering discipline at the local level:

- understand the local tunnel's purpose,
- identify which local file owns each objective,
- distinguish useful reinforcement from harmful duplication,
- detect weak wording, missing links, misplaced logic, or incomplete handoffs,
- preserve accepted project truth,
- strengthen the correct owner before deleting or reducing duplicate text,
- repair the smallest local weakness that improves future project work,
- and keep the local project flow aligned with upper-layer method without importing project-specific truth into upper layers.

This allows the model to improve project documentation, scenarios, research structures, knowledge systems, and code-oriented artifacts with the same precision used to improve the repository tunnel.

Project-local tunnel performance work must remain project-local unless the weakness reveals a reusable upper-layer behavior issue.

---

# Tunnel Before Branch Content

For project-specific work, the correct sequence is:

1. enter the project instance layer
2. account for project instance numbered root files if present
3. discover non-numbered project candidates or project content
4. enter the relevant discovered project folder
5. account for numbered root files inside the discovered project folder
6. continue into relevant branches or modules
7. account for any local numbered files in those branches
8. inspect non-numbered target content according to user intent

The model must not jump directly to a deep artifact while skipping project or branch standards.

The model must not scan unrelated project content when the request is focused.

Tunnel traversal supplies governing standards.

Dynamic discovery supplies target context.

Both are required.

---

# Project Files Should Be Locally Understandable

Project-specific files should not need to repeat exact paths to the cognitive runtime or project orchestration layers.

The upper layers are responsible for guiding the model into the project.

The project folder is responsible for defining project-specific truth.

Once inside the project, the model should understand the project from:

- project-local numbered standards
- project-local structure
- project identity files
- project taxonomies
- project artifacts
- project decisions
- project knowledge
- branch-local standards
- current conversation

This keeps project files portable and prevents upper-layer architecture from polluting project-specific documentation.

---

# Project Name Inference

The model may infer the active project name from:

- discovered project folder name
- project identity file
- project title
- repeated project terminology
- user message
- artifact names
- structure tree
- README-like files
- project-local standards

Folder name alone is a clue, not final truth.

If folder name and project identity conflict, project identity content is more authoritative.

If identity is missing, use the folder name as a provisional project label.

Do not require the user to explicitly state the project name when repository structure and context make it clear.

---

# Dynamic Discovery After Local Tunnel

After local tunnels have been accounted for, non-numbered files and folders become dynamic project content.

Dynamic project content may include:

- dashboards
- modules
- PRDs
- workflows
- screens
- research notes
- implementation notes
- raw references
- placeholder files
- route markers
- local standards
- source material
- child artifacts
- sibling artifacts

The model should inspect only the content relevant to the current user request.

For a targeted request, inspect target, parent, sibling, and governing standards as needed.

For a full audit, inspect more broadly.

Do not treat every non-numbered file as equally relevant to every response.

---

# Missing Root Guard Recovery

If the project instance root does not contain `00` and `99` guard files, but contains non-numbered project folders, the model should still proceed.

Behavior:

- recognize the missing guard files as a structure weakness
- continue into the likely project folder if user intent is project-specific
- infer project identity from project-local files
- recommend restoring project instance root guard files when appropriate
- do not treat the absence of guard files as absence of project

This rule protects project discovery even when the ideal architecture is incomplete.

---

# Project-Specific Answer Source Stack

When answering after handoff into a discovered project folder, use cumulative context.

Source stack:

1. cognitive runtime rules
2. project orchestration methods
3. project instance root guard files if present
4. discovered project folder numbered standards
5. branch-local numbered standards if present
6. project structure files
7. project identity and objectives
8. project knowledge and decision files
9. target artifact content
10. related parent, child, or sibling artifacts
11. current conversation and latest user corrections
12. general knowledge only as support

Do not answer from the target artifact alone if governing standards exist.

Do not answer from general orchestration alone if project truth is available.

---

# Handoff Failure Signals

Handoff failure may occur when the model:

- stops at `02_MY_PROJECT/` and does not enter the discovered project folder
- requires the project name to be explicitly registered in the upper layers
- ignores non-numbered folders after the project instance tunnel
- skips project-local numbered files
- skips local numbered files inside a branch
- treats missing root guard files as absence of project
- answers from general method while project-specific standards exist
- treats project files as dependent on upper-layer paths
- inspects deep content without governing standards
- scans too broadly and ignores the focused target

When this happens, correct the route and re-enter through the relevant local tunnel.

---

# Discover Only What Matters

Dynamic discovery does not mean exhaustive scanning every time.

The model should scale discovery depth to the request.

## Light Discovery

Use for simple project-aware answers.

## Focused Discovery

Use when the user asks about a specific folder, artifact, section, or next step.

## Deep Discovery

Use for project audit, migration, conflict resolution, maturity assessment, or architecture redesign.

## Full Discovery

Use only when the user asks to inspect the whole project or validate repository structure.

Efficient discovery prevents noise.

Sufficient discovery prevents stale or generic answers.

---

# Project Content Classification

When discovering project content, classify relevant items as:

- standard
- index
- artifact
- parent artifact
- child artifact
- workflow
- research note
- knowledge note
- implementation note
- screen or interface artifact
- raw reference
- source material
- placeholder
- route marker
- scaffold
- old version
- migration artifact
- decision record
- roadmap item
- conflicting artifact
- outdated artifact
- unknown

Classification should be based on content and context, not only file name.

---

# Targeted Branch Discovery

When the user mentions a specific branch, module, section, file, or artifact, the model should discover:

- governing project standards
- parent context
- sibling context when relevant
- child artifacts when relevant
- related knowledge
- decisions affecting it
- maturity and intent of the target artifact
- whether the requested output belongs there

Do not treat a target artifact as isolated if project context exists.

Do not over-scan unrelated branches.

---

# Parent And Child Discovery

If the user asks about a child artifact, discover the parent.

If the user asks about a parent artifact, identify likely children or child roadmap.

If the user asks about a branch, identify relevant standards and local structure.

Do not generate a child artifact without parent context when parent context matters.

Do not force parent/child hierarchy on projects that do not use it.

---

# Standard Versus Content Discovery

The model must distinguish project standards from project content.

A numbered root file inside the project instance is likely a project standard.

A non-numbered folder after the numbered tunnel is likely project content.

However, content may contain local standards.

If a local standard exists inside a branch, use it for that branch.

A local standard should not override project-level standards unless explicitly designed to specialize them.

---

# Local Standards

A project branch may contain local standards.

Examples:

- module standard
- section standard
- research area standard
- curriculum standard
- screen standard
- implementation standard
- source policy for a specific domain
- local artifact naming rule

When local standards exist, the model should use them for branch-specific work.

If local standards conflict with project-level standards, classify the conflict.

Do not silently choose one.

---

# Project-Specific Truth Priority

For project-specific work, use this priority:

1. project instance numbered standards
2. target branch local standards
3. target artifact content
4. parent artifact
5. sibling or child artifacts when relevant
6. project decision log
7. project knowledge map
8. current conversation and user corrections
9. project orchestration method
10. general knowledge

This priority may vary slightly by task, but project truth must come from the project instance.

---

# Conversation During Project Handoff

The current conversation may update project truth.

If the user introduces a project-specific correction or decision, the model should treat it as live input.

If the correction should persist, recommend updating the project instance.

If the repository still says something older, classify it as possible outdated content, conflict, or migration state.

Do not ignore the conversation because project files exist.

Do not ignore project files because conversation is rich.

---

# Repository Update During Project Handoff

When the user says the repository was updated:

- invalidate old project assumptions
- re-check current project context when possible
- do not repeat old paths blindly
- treat prior generated files as potentially saved
- avoid claiming exact current content without inspection
- continue from accepted architecture and sequence

Repository updates can change the project instance.

---

# Legacy Structure Compatibility

Older structures may use paths such as:

    AI_COGNITIVE_RUNTIME/
    ACTIVE_PROJECT/
    ACTIVE_PROJECT/<project_folder>/

During migration, the model may recognize these as legacy or prior architecture.

The preferred modern structure uses numbered layer folders.

If both exist, identify which structure is active from user direction and repository evidence.

Do not merge legacy and modern paths blindly.

Do not continue using old paths when the user has accepted migration.

---

# Project Instance Migration

When migrating a project into the modern architecture:

1. identify old project location
2. identify new project instance folder
3. preserve project-specific standards
4. move general method rules out of project instance
5. move project-specific rules into project instance
6. preserve raw references
7. preserve accepted artifacts
8. identify placeholders and scaffolds
9. update structure indexes
10. avoid weakening the project during migration

Migration should improve project discoverability and reasoning.

---

# Project Instance With Multiple Projects

A repository may contain more than one project instance or subproject.

The model should identify which project is active from:

- user message
- current sequence
- folder names
- project standards
- recent conversation
- target artifact
- repository structure

If ambiguity affects the output, ask one focused question.

Do not merge different project instances.

---

# Project Instance With One Large Project

A project instance may contain one large project with many branches.

Example:

    02_MY_PROJECT/
      numbered standards...
      <project_folder>/
        A_dashboards/
        B_web_frontend/
        C_mobile_app/

In this case, the named folder may hold project content while numbered standards remain at the project instance root.

The model should use both:

- root project standards
- named project folder content

The model should not assume the named project folder is a separate orchestration layer.

---

# Project Instance With Direct Project Branches

A project instance may place major branches directly after standards.

Example:

    02_MY_PROJECT/
      numbered standards...
      A_dashboards/
      B_web_frontend/
      C_mobile_app/

In this case, the non-numbered folders are direct project content branches.

The model should inspect them dynamically based on the request.

Do not require an extra named project folder.

---

# Project Instance With Only Standards

A project instance may temporarily contain standards but no content branches.

This may happen early.

The model should:

- use standards to guide discussion
- propose first content branches if useful
- avoid claiming project content exists
- help the user create the next artifact or structure

This is a valid stage.

---

# Project Instance With Only Content And Weak Standards

A project may have content folders but weak or missing standards.

The model should:

- inspect relevant content
- identify implicit standards
- recommend creating or improving standards
- avoid forcing a full rebuild
- preserve useful project content
- avoid treating content as invalid merely because standards are weak

This is common in evolving projects.

---

# Project Instance With Conflicting Standards

If standards conflict:

- identify the conflicting files
- identify which is newer when possible
- identify which is more authoritative
- consider current conversation corrections
- recommend update, merge, or replacement
- avoid silently combining incompatible rules

Project standards must be reliable.

---

# Project Instance With Missing Structure Index

If the project has many branches but no structure index, recommend creating one when useful.

A structure index helps dynamic discovery.

It may document:

- numbered standards
- content branches
- local standards
- artifact types
- navigation rules
- parent/child relationships
- raw references
- implementation areas
- knowledge areas

Do not require a structure index for very small projects.

---

# Project Instance With Raw References

Raw references may appear inside project content.

The model should not treat raw references as final artifacts.

It should:

- preserve them
- classify them
- extract useful signal
- transform them when requested
- avoid overwriting source material prematurely
- create mature artifacts from them when appropriate

Raw references may be very important.

---

# Project Instance With Placeholders

Placeholders may appear inside the project instance.

The model should classify whether they are:

- intentional future routes
- empty structural nodes
- accidental empty files
- scaffolds awaiting content
- outdated placeholders
- ready to be filled

Do not assume placeholder equals failure.

---

# Project Instance With Generated But Unaccepted Artifacts

A generated artifact may not yet be accepted.

If the user has not accepted or saved it, treat it as proposed.

If the user says it was added to the repository, treat it as likely accepted but verify if exact current state matters.

Do not treat every generated proposal as project truth.

---

# Dynamic Discovery And Output Generation

Before generating project-specific files, the model should identify:

- project instance root
- governing project standards
- target path
- artifact type
- parent context
- relevant local standards
- current maturity
- accepted decisions
- required knowledge
- output safety requirements

Then generate using cognitive runtime output rules.

---

# Dynamic Discovery And Audit

When auditing a project instance, inspect:

- standard layer completeness
- structure clarity
- project content branches
- misplaced rules
- placeholder and scaffold intent
- artifact maturity
- conflicts
- outdated content
- missing indexes
- missing decision memory
- missing knowledge map
- project-specific versus general-layer pollution

Audit findings should be current and evidence-based.

Do not repeat old audits after repository changes.

---

# Dynamic Discovery And Next Step

When asked for the next step inside a project instance, consider:

- current project standards
- project maturity
- active branch
- roadmap
- missing standards
- current user intent
- blockers
- dependencies
- knowledge gaps
- accepted sequence

Do not always choose the next numeric file.

Numeric order controls tunnel reading, not necessarily execution order.

---

# Handoff Output Patterns

Depending on user intent, output may be:

## Simple Project-Aware Answer

Use project context silently and answer directly.

## Project Instance Finding

Mention relevant project layer or target branch.

## Discovery Map

Use when the user asks how the project is organized.

## Audit Findings

Use when the user asks to inspect or diagnose.

## Next Action

Recommend the next project-specific move.

## File Generation

Generate a project instance file or artifact with correct path and copy-safe block.

## Migration Recommendation

Suggest moving, renaming, or restructuring project-specific content.

Use the output pattern that serves the user.

---

# Avoid Over-Discovery

Over-discovery can slow work and produce noise.

Avoid:

- scanning unrelated branches
- explaining the whole repository for a small file
- auditing when the user asks for one artifact
- treating every non-numbered file as relevant
- producing long structure reports during active file generation

Use enough discovery to be accurate.

---

# Avoid Under-Discovery

Under-discovery causes generic or wrong answers.

Avoid:

- answering project-specific questions from general method only
- skipping project standards
- ignoring local branch standards
- ignoring target artifact content
- ignoring parent context
- using old assumptions after update
- treating project content as invisible because it is not listed

Use focused discovery when project truth matters.

---

# Project Instance And Active Project Discovery

If the active project is placed in the project instance layer, it should be treated as project-specific truth, not general method.

A project instance may contain:

- project-specific standards
- platform identity
- state taxonomy
- event taxonomy
- structure tree
- dashboards
- web
- mobile
- modules
- PRDs
- workflows
- implementation notes
- knowledge references
- raw sources

The upper layers should improve the model’s ability to work with the active project.

They should not absorb project-specific content into general orchestration.

A real active project validates the architecture without becoming a dependency of the upper layers.

---

# Failure Signals

Project instance handoff and discovery failures include:

- stopping at project orchestration when project truth is needed
- answering from cognitive runtime only
- skipping project-specific numbered standards
- ignoring non-numbered project content
- relying only on hardcoded file lists
- assuming a minimal project instance is broken
- treating file existence as maturity
- treating folder existence as implementation
- ignoring local standards
- merging multiple project instances
- using legacy paths after migration
- generating project artifacts without target path awareness
- treating generated proposals as saved truth
- over-scanning unrelated branches
- under-scanning relevant branches
- making project-specific claims without evidence

When failure occurs, re-enter the project instance correctly and continue.

---

# Final Principle

Project instance handoff is the bridge from general method to real project truth.

The model must enter the project instance when the work becomes project-specific, account for the project-specific numbered tunnel, discover relevant content dynamically, and produce outputs grounded in the actual project.

A strong handoff prevents generic answers and makes the repository function as a living project mind.
---

# Project Reality Discovery For Scenario And Artifact Synthesis

Dynamic discovery is not only for locating files.

It is also used to understand project reality before synthesizing scenarios, PRDs, workflows, standards, implementation plans, audits, or repairs.

When the user asks for mature project output, the model must discover enough project reality to avoid isolated reasoning.

Depending on the request, relevant discovery may include:

- project identity and objectives;
- numbered local standards;
- structure tree or module map;
- parent artifact and sibling artifacts;
- central states, events, roles, permissions, primitives, or taxonomies;
- lifecycle documents;
- implementation, data, API, environment, research, writing, or operating standards;
- existing content in the affected branch.

The model should not inspect the entire repository when a focused branch is enough.

But it must not generate project-specific synthesis while ignoring obvious project-local context.

Use discovery depth proportional to the risk and scope of the output.

For project-aware raw-to-gold synthesis, hand off to:

- `21_PROJECT_REALITY_CALIBRATION_AND_GOLDEN_SYNTHESIS_METHOD.md`
