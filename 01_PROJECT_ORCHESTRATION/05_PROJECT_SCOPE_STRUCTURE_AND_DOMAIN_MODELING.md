# PROJECT SCOPE STRUCTURE AND DOMAIN MODELING

# Purpose

This file defines how the model should understand project scope, propose or discover project structure, model the project domain, and dynamically inspect project content after the project-specific numbered tunnel.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific structure tree.

It is not a project-specific taxonomy.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define the general method for turning a project’s identity and objectives into a useful structure and domain model.

The project orchestration layer defines how to build or discover structure.

The project instance layer stores the actual project structure and domain truth.

---

# Core Principle

Structure must serve understanding and execution.

The model should not impose a structure before the project type, scope, and domain are understood.

The model should not ignore existing structure when a project instance exists.

The correct structure is the one that helps the user preserve meaning, find artifacts, produce outputs, and evolve the project without losing context.

A project may have one folder.

A project may have many folders.

A project may start with only seed files.

A project may grow into a complex workspace.

The model must adapt.

---

# What This File Owns

This file owns the project-orchestration method for scope, structure, and domain modeling.

It defines:

- how to define project scope
- how to identify non-scope
- how to distinguish project structure from repository structure
- how to propose project folder structures
- how to discover existing structures
- how to treat non-numbered folders after the project tunnel
- how to build domain models
- how to identify entities, concepts, roles, states, events, and artifacts at a general level
- how to decide when a structure tree or taxonomy is needed
- how to avoid over-structuring
- how to avoid under-structuring
- how to handle multiple project branches
- how to route project-specific structure into the project instance layer

This file does not own:

- the final structure of a specific project
- the final taxonomy of a specific project
- project-specific folder names
- project-specific modules
- project-specific UI sections
- project-specific workflows
- project-specific implementation structure
- project-specific decisions

Those belong in the project instance layer.

---

# Scope Definition

Project scope answers:

- what belongs to the project
- what does not belong to the project
- what is part of the current phase
- what is future expansion
- what is intentionally excluded
- what is still unknown
- what level of detail should be documented now

Scope protects the project from drift.

Scope also prevents premature narrowing.

The model should help the user define scope progressively.

---

# Non-Scope Definition

Non-scope is as important as scope when a project risks over-expansion.

Non-scope may include:

- features not being built yet
- domains not being covered
- implementation not being started yet
- UI not being designed yet
- legal or medical advice not being finalized
- research claims not being treated as conclusions
- a specific project not being treated as a universal method
- upper layers not containing project-specific details

Non-scope should be used to protect focus, not to block evolution.

---

# Structure Definition

Project structure is the organization of project knowledge, standards, artifacts, and content.

It may be expressed through:

- folders
- numbered standard files
- indexes
- taxonomies
- modules
- chapters
- domains
- workflows
- roadmap phases
- knowledge areas
- decision logs
- implementation areas
- artifact hierarchies

Structure should help the model and user locate meaning.

It should not exist only for appearance.

---

# Repository Structure Versus Project Structure

Repository structure is how files and folders are physically arranged.

Project structure is how project concepts and artifacts relate.

They often overlap, but they are not the same.

A folder may represent a concept, module, area, phase, or technical grouping.

A file may be a standard, artifact, note, scaffold, raw reference, or output.

The model must inspect content and context before assigning meaning.

Do not infer maturity from folder existence alone.

---

# Project Instance Structure

Inside the project instance layer, numbered root files are project-specific standards.

After those numbered files, non-numbered folders and files are usually project content.

Example pattern:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      01_PROJECT_IDENTITY_AND_OBJECTIVES.md
      04_PROJECT_STRUCTURE_TREE_INDEX.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md
      product_area/
      research_area/
      documentation/
      implementation_notes/

The actual names depend on the project.

The model must not require every project to have the same branches.

---

# Dynamic Discovery After The Project Tunnel

After the project instance numbered tunnel is accounted for, the model should inspect non-numbered folders and files dynamically based on user intent.

The model should identify:

- which folders are project content
- which files are artifacts
- which files are raw references
- which folders represent major areas
- which folders are technical implementation folders
- which folders are knowledge or research areas
- which artifacts are standards
- which artifacts are outputs
- which artifacts are outdated or provisional
- which content is relevant to the current request

Do not inspect the entire project tree for every small question.

Do not ignore project content when it is the target.

---

# Folder Existence Is Structural Evidence Only

A folder existing means the project may recognize that area.

It does not mean:

- the area is mature
- the area is documented
- the area is implemented
- the area is ready
- the area has accepted standards
- the area has enough content for artifact generation

Use folder existence as structural evidence.

Use file content and conversation context for maturity and truth.

---

# File Content Beats File Name

A file name suggests responsibility.

File content confirms responsibility.

A file named as a standard may contain only a placeholder.

A file named as notes may contain important project decisions.

A file named as PRD may be raw, mature, outdated, or conflicting.

The model must inspect content when the answer depends on it.

Do not judge by name alone.

---

# Domain Modeling Definition

Domain modeling identifies the meaningful concepts inside the project.

Depending on project type, these may include:

- entities
- actors
- roles
- audiences
- user types
- workflows
- states
- events
- concepts
- knowledge areas
- research themes
- claims
- sources
- policies
- modules
- interfaces
- chapters
- lessons
- operations
- constraints
- outputs

Domain modeling should match the project type.

Do not force software entity modeling on non-software work.

---

# Project Type Shapes Domain Model

A software platform may need:

- users
- roles
- permissions
- modules
- data entities
- states
- events
- workflows
- interfaces
- integrations

A research project may need:

- research questions
- sources
- claims
- methods
- evidence hierarchy
- themes
- findings
- counterarguments

A learning project may need:

- topics
- prerequisites
- skill levels
- practice tasks
- assessments
- resources
- milestones

A knowledge base may need:

- concepts
- taxonomies
- source hierarchy
- glossary
- confidence levels
- update rules

An operational system may need:

- roles
- policies
- processes
- handoffs
- triggers
- states
- escalation paths
- audit rules

The model must adapt the domain model to the work.

---

# Scope Extraction Method

When scope is unclear, extract it from:

- project identity
- objectives
- user statements
- repeated concerns
- repository folders
- existing artifacts
- explicit exclusions
- roadmap discussions
- implementation constraints
- knowledge needs
- project type

Classify scope as:

- confirmed
- inferred
- proposed
- future
- excluded
- uncertain

Do not present inferred scope as documented truth.

---

# Structure Proposal Method

When proposing a structure:

1. classify the project type
2. identify the minimum useful structure
3. preserve existing structure if it is useful
4. avoid creating many empty folders
5. align folders with project concepts
6. align files with standards or artifacts
7. separate project standards from project content
8. avoid mixing general methods with project truth
9. identify what can wait
10. propose the next smallest useful structure

A structure should reduce future confusion.

---

# Existing Structure Discovery Method

When discovering existing structure:

1. account for the numbered tunnel
2. identify project instance standards
3. identify non-numbered folders and files
4. classify folders by likely purpose
5. inspect content when needed
6. compare structure with project identity and objectives
7. detect missing indexes or structure maps
8. detect misplaced rules
9. detect orphan artifacts
10. recommend structure updates only when useful

Do not rewrite structure only because it is different from a template.

---

# Structure Tree Index

A project may need a structure tree index when:

- the project has many folders
- the project has multiple artifact types
- the user needs dynamic discovery
- future AI work depends on reliable navigation
- there are parent and child artifacts
- project content is spread across branches
- the project has dashboards, modules, chapters, domains, or knowledge areas
- collaborators need orientation
- repeated navigation confusion occurs

The structure tree belongs in the project instance layer.

The project orchestration layer defines when and how to create it.

---

# Domain Taxonomy

A project may need a domain taxonomy when:

- terminology repeats
- concepts are easy to confuse
- different files use inconsistent names
- states, roles, or categories matter
- knowledge needs structure
- artifacts depend on shared definitions
- implementation depends on entity clarity
- research depends on concept boundaries

The taxonomy belongs in the project instance layer.

The project orchestration layer defines when and how to propose it.

---

# State And Event Modeling

Some projects need state and event modeling.

This is common in:

- software platforms
- workflows
- operational systems
- governance systems
- lifecycle-heavy products
- approval systems
- automation-heavy systems
- research pipelines
- learning progress systems

State and event modeling should be proposed only when useful.

It belongs in the project instance standards or relevant artifacts.

Do not force it on projects that do not need it.

---

# Branching Strategy

A project may branch by:

- product surface
- user role
- domain
- workflow
- chapter
- topic
- research question
- knowledge area
- implementation layer
- roadmap phase
- artifact type

Choose branching based on project logic, not habit.

For a large software project, branches might be dashboards, frontend, mobile, backend, integrations, or domains.

For a research project, branches might be themes, sources, methods, findings, and publications.

For a learning project, branches might be levels, modules, exercises, and assessments.

---

# Multiple Project Content Layouts

The project instance may organize content in different ways.

## Single Root Project

    02_MY_PROJECT/
      standards...
      modules/
      workflows/
      notes/

## Named Project Folder Inside Instance

    02_MY_PROJECT/
      standards...
      <project_folder>/
        A_dashboards/
        B_web_frontend/
        C_mobile_app/

## Direct Major Branches

    02_MY_PROJECT/
      standards...
      A_dashboards/
      B_web_frontend/
      C_mobile_app/

## Knowledge Project

    02_MY_PROJECT/
      standards...
      concepts/
      sources/
      syntheses/
      claims/

## Research Project

    02_MY_PROJECT/
      standards...
      literature/
      methods/
      findings/
      drafts/

The model should infer layout from current structure and user direction.

Do not assume one layout is mandatory.

---

# Project Content Classification

When inspecting project content, classify each relevant artifact or folder as one or more of:

- standard
- index
- artifact
- raw reference
- source material
- draft
- mature document
- placeholder
- scaffold
- decision record
- knowledge note
- workflow
- implementation note
- visual or UI artifact
- research source
- output artifact
- obsolete content
- conflicting content

Classification helps decide the next action.

---

# Orphan Content Detection

A project artifact may be orphaned if:

- it has no clear parent
- it is not referenced by a structure map
- it duplicates another artifact
- it belongs to a different project type
- it lacks project-specific standards
- it uses inconsistent terminology
- it sits outside the expected branch
- it was copied as scaffold and never rewritten

Do not delete automatically.

Classify and recommend relocation, rewrite, merge, or reference update.

---

# Misplaced Structure Signals

Structure may need correction when:

- project-specific standards are in upper layers
- general methods are in project instance
- project content appears before project standards
- non-numbered folders are treated as invisible
- numbered project standards are skipped
- folder names do not match content
- file names do not match titles
- artifacts are duplicated across branches
- a large project lacks a structure index
- project branches do not reflect actual scope

Correct structure carefully.

Preserve useful content.

---

# Scope Expansion Handling

Projects evolve.

When scope expands:

- identify what changed
- classify expansion as accepted, proposed, or exploratory
- identify affected standards
- identify affected structure
- identify new knowledge needs
- identify whether new branches or artifacts are needed
- avoid silently expanding project scope without user acceptance

Scope growth should be controlled, not accidental.

---

# Scope Reduction Handling

Projects may also need scope reduction.

When scope is too broad:

- identify the core objective
- identify non-essential branches
- identify future items
- identify what can be deferred
- preserve future ideas without forcing them into current structure
- recommend a smaller current scope

A narrower project can be stronger if it protects execution.

---

# Structure And Roadmap Relationship

Structure is not the same as roadmap.

Structure answers:

- where things belong
- how concepts relate
- how artifacts are organized

Roadmap answers:

- what to do first
- what to build next
- what to defer
- what sequence reduces risk

Both may be needed.

Do not confuse folder hierarchy with execution priority.

---

# Structure And Knowledge Relationship

Some structure is conceptual rather than product-based.

Knowledge-heavy projects need taxonomies, evidence maps, source maps, and topic trees.

Product-heavy projects may need modules, workflows, screens, data, and implementation notes.

The model should choose structure according to knowledge type and project type.

---

# Structure And Artifact Hierarchy

A project may need artifact hierarchy.

Examples:

- standard → artifact
- parent scenario → child scenario
- research question → source notes → synthesis
- learning goal → curriculum → exercises
- policy → procedure → checklist
- roadmap phase → task → implementation note

Artifact hierarchy should be built by project need.

Do not impose parent/child PRD structure on every project.

---

# Minimal Structure Principle

Start with the smallest structure that can preserve meaning and guide next work.

A minimal project instance may need:

- seed
- reinforcement
- identity and objectives
- one structure note or index
- one content area

A mature project may need many layers.

Do not confuse minimal with weak.

Minimal can be correct for early stages.

---

# Structure Should Enable Dynamic Discovery

The structure should help both user and model find relevant context.

A good structure lets the model answer:

- where is the project identity?
- where are project standards?
- where is the branch related to the current request?
- what content is project-specific?
- what is raw reference?
- what is mature?
- what is missing?
- what is next?

Dynamic discovery is more important than memorized file lists.

---

# When To Generate Structure Files

Generate or recommend a structure file when:

- the project has multiple branches
- navigation is becoming difficult
- artifacts are increasing
- dynamic discovery matters
- files are being misplaced
- the user asks for repository organization
- a project needs a standard tunnel
- future AI work depends on reliable structure

Do not generate structure files for a one-time small task.

---

# Structure File Output

When generating a project structure file, place it in the project instance layer.

It should usually include:

- purpose
- project root
- numbered standard files
- non-numbered project content folders
- branch responsibilities
- artifact types
- navigation principles
- dynamic discovery rules
- open structure questions
- update policy

Exact content depends on project type.

---

# Relationship With Standard Layer Factory

The standard layer factory defines what standard files should exist.

This file defines how project scope and structure should be understood or proposed.

They work together.

A project may need identity before structure.

A project may need basic structure before detailed taxonomies.

Use context.

---

# Failure Signals

Scope, structure, and domain modeling failures include:

- imposing software structure on non-software work
- ignoring existing folders
- treating folder existence as maturity
- ignoring non-numbered project content
- skipping the project-specific tunnel
- creating many empty branches
- failing to propose structure when project complexity requires it
- mixing roadmap with structure
- mixing upper-layer methodology with project-specific content
- failing to detect scope creep
- treating project-specific folder names as universal
- deleting useful raw references because they look unstructured
- generating a structure that cannot support dynamic discovery

When failure occurs, correct the model and preserve useful content.

---

# Final Principle

Project structure is a thinking tool.

It should preserve meaning, support discovery, reduce confusion, and guide future work.

The model must build or discover structure from project identity, objectives, domain, current files, and user intent.

A strong structure makes the project easier to understand, expand, audit, and execute.