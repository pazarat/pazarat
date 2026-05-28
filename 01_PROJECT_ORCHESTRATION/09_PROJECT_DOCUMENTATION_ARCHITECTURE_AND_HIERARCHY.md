# PROJECT DOCUMENTATION ARCHITECTURE AND HIERARCHY

# Purpose

This file defines how the model should design, evaluate, and evolve documentation architecture and artifact hierarchy for any project or structured body of work.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific documentation standard.

It is not a PRD for a specific project.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, folder, file, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for deciding what kinds of documents or artifacts a project needs, how they should relate, what belongs at each level, and how to avoid collapsing all project knowledge into the wrong artifact.

The project orchestration layer defines the documentation method.

The project instance layer stores the actual project-specific documentation standards and artifacts.

---

# Core Principle

Documentation architecture must preserve meaning.

The right artifact should contain the right level of detail.

A strong documentation system prevents:

- context loss
- repeated explanation
- wrong-level detail
- orphan artifacts
- duplicated logic
- missing parent context
- premature implementation
- project-specific rules leaking into general layers
- general methods being mistaken for project truth

The model must choose artifact hierarchy based on project type, maturity, user intent, and project-specific standards.

Do not force one documentation pattern on every project.

---

# What This File Owns

This file owns the project-orchestration method for documentation architecture and hierarchy.

It defines:

- how to decide what artifact types are needed
- how to separate parent and child artifacts
- how to identify artifact ownership
- how to avoid wrong-level detail
- how to organize standards, knowledge, decisions, roadmaps, and content
- how to preserve shared logic
- how to prevent orphan artifacts
- how to decide when a project-specific documentation standard is needed
- how to adapt documentation architecture to project type
- how to route actual project documentation into the project instance layer

This file does not own:

- project-specific artifact content
- project-specific PRDs
- project-specific workflows
- project-specific screen standards
- project-specific research notes
- project-specific learning modules
- project-specific implementation notes
- project-specific documentation tree
- current project documentation status

Those belong in the project instance layer or current response when explicitly assessed.

---

# Documentation Architecture Definition

Documentation architecture is the relationship between project artifacts.

It answers:

- what artifact types exist
- why each artifact exists
- what each artifact owns
- what each artifact must not own
- how artifacts reference each other
- what is parent-level
- what is child-level
- what is shared
- what is local
- what is source material
- what is decision memory
- what is execution output
- what should be generated next

Documentation architecture is not only folder structure.

It is the logic of how project knowledge is preserved.

---

# Artifact Hierarchy Definition

Artifact hierarchy defines levels of meaning and detail.

A hierarchy may include:

- project standard
- identity and objectives
- structure index
- knowledge map
- decision log
- roadmap
- parent artifact
- child artifact
- workflow
- state or event model
- research note
- source note
- lesson
- policy
- procedure
- implementation note
- visual reference
- output artifact

The correct hierarchy depends on project type.

Do not impose product-documentation hierarchy on non-product projects.

---

# Documentation Must Match Project Type

Different project types need different documentation architecture.

## Software Or Product Project

May use:

- identity and objectives
- project standards
- domain taxonomy
- event taxonomy
- parent PRDs
- child PRDs
- workflows
- state and event models
- screen or interface documents
- implementation notes
- decision logs
- roadmap

## Research Project

May use:

- research identity
- research question
- scope and methodology
- evidence hierarchy
- source notes
- literature map
- claim register
- synthesis notes
- findings
- publication drafts
- decision and uncertainty log

## Learning Project

May use:

- learning goal
- level assessment
- curriculum map
- modules
- lessons
- exercises
- assessments
- progress log
- resource map
- review plan

## Knowledge Base

May use:

- domain scope
- concept taxonomy
- glossary
- source hierarchy
- topic notes
- synthesis notes
- claim confidence model
- update policy

## Writing Project

May use:

- purpose
- audience
- voice guide
- outline
- chapter drafts
- source notes
- revision notes
- publication roadmap

## Operational Project

May use:

- operating principles
- roles
- policies
- procedures
- workflows
- checklists
- escalation rules
- audit logs
- change records

The model must classify the work before recommending artifact architecture.

---

# Project Standards Versus Project Artifacts

Project standards define how the project should be understood and produced.

Project artifacts are outputs created under those standards.

Examples of standards:

- identity and objectives
- structure tree
- taxonomy
- source policy
- documentation rules
- naming conventions
- decision rules
- artifact templates
- evidence hierarchy

Examples of artifacts:

- PRD
- workflow
- research note
- lesson
- policy
- implementation note
- chapter
- source synthesis
- screen description
- decision record

Standards guide artifacts.

Artifacts should not silently redefine standards.

If an artifact reveals a needed standard, propose updating the project instance standard layer.

---

# Parent Artifact Definition

A parent artifact defines broad context.

It usually owns:

- purpose
- philosophy
- scope
- boundaries
- high-level journey
- major relationships
- major entities or concepts
- major decisions
- child artifact roadmap
- open questions
- what should be detailed elsewhere

A parent artifact should help the user and model understand the whole area without drowning in low-level details.

---

# Child Artifact Definition

A child artifact deepens one focused branch.

It may own:

- detailed process
- specific workflow
- local states
- local events
- fields
- validations
- exceptions
- examples
- source details
- implementation notes
- screen behavior
- lesson details
- research subquestion
- procedure steps

A child artifact should inherit context from the parent.

It should not redefine the parent’s purpose unless the parent is wrong or outdated.

---

# Parent Before Child Rule

Before generating or judging a child artifact, identify the parent context.

Ask internally:

- what parent artifact governs this child?
- what project standards govern the parent?
- what does the child inherit?
- what branch does the child own?
- what belongs in the parent instead?
- what belongs in siblings?
- what belongs in shared standards?
- what belongs in decision memory?
- what belongs in knowledge map?
- what belongs in implementation notes?

Do not create orphan child artifacts.

---

# Main Artifact Versus Detailed Artifact

A main artifact should provide orientation.

A detailed artifact should provide precision.

Incorrect behavior:

- putting every field, exception, screen, and implementation rule into the main artifact
- writing a detailed child artifact without parent context
- using a screen or implementation artifact to define project philosophy
- forcing a parent artifact to become a full technical specification too early

Correct behavior:

- parent gives map
- child gives route
- workflow gives process
- state/event model gives transitions
- screen artifact gives interface behavior
- implementation note gives technical execution
- decision log preserves accepted choices
- knowledge map preserves domain understanding

---

# Shared Logic Versus Local Logic

Some logic belongs to the whole project.

Some logic belongs to a branch.

Some logic belongs to one artifact only.

## Shared Logic

Belongs in project standards or shared primitives.

Examples:

- role model
- terminology
- approval pattern
- evidence hierarchy
- source policy
- identity rules
- naming rules
- traceability rules

## Local Logic

Belongs in a specific artifact.

Examples:

- one workflow’s detailed steps
- one screen’s behavior
- one chapter’s argument
- one lesson’s exercise
- one process’s exception handling

Do not duplicate shared logic across many artifacts with slight differences.

If repeated logic appears, consider a shared standard or primitive.

---

# Artifact Ownership

Every artifact should have clear ownership.

Ownership answers:

- what concept does this artifact own?
- what layer does it belong to?
- what parent does it depend on?
- what artifacts does it guide?
- what should not be placed here?
- what future work does it enable?

An artifact without ownership is likely to drift.

---

# Artifact Boundary

An artifact boundary defines what belongs inside and outside the artifact.

Good boundaries prevent:

- duplication
- scope creep
- wrong-level detail
- missing dependencies
- future contradictions
- overlong documents
- shallow documents

When generating an artifact, include boundaries when useful.

---

# Artifact Dependency

Some artifacts depend on others.

Examples:

- identity before structure
- structure before deep navigation
- knowledge map before high-stakes claims
- parent artifact before child artifact
- workflow before detailed screen behavior
- source policy before research synthesis
- domain taxonomy before terminology-heavy artifacts
- decision log before controlled change
- roadmap before implementation sequence

Dependencies vary by project type.

Do not force one dependency model on every project.

---

# Artifact Traceability

Traceability means future work can understand where a claim, rule, decision, or artifact came from.

Traceability may connect:

- artifact to project objective
- child artifact to parent artifact
- workflow to scenario
- research finding to source
- decision to reason
- implementation note to requirement
- lesson to learning goal
- policy to principle
- roadmap item to objective

Project-specific traceability rules belong in the project instance layer.

This file defines the general need and method.

---

# Documentation Architecture For Minimal Projects

A minimal project may need only:

- project seed
- project reinforcement
- identity and objectives
- one content artifact

Do not force complex hierarchy too early.

Minimal can be correct when the project is early.

The model should recommend additional hierarchy only when it solves a real problem.

---

# Documentation Architecture For Complex Projects

A complex project may need:

- standard layer
- structure index
- knowledge map
- decision log
- shared primitives
- parent artifacts
- child artifacts
- workflow artifacts
- technical or delivery artifacts
- audit or change records

Complexity should be justified by project needs.

Do not create complexity only because the system supports it.

---

# Artifact Types

Possible artifact types include:

## Standard

Defines rules for future work.

## Index

Helps navigate project structure.

## Identity Document

Defines what the project is and why it exists.

## Objective Document

Defines desired outcomes.

## Taxonomy

Defines concepts, entities, categories, states, or events.

## Knowledge Map

Defines knowledge domains, gaps, sources, and learning or research needs.

## Decision Log

Preserves accepted decisions and why they matter.

## Roadmap

Defines sequence, phases, dependencies, and next actions.

## Parent Scenario Or Main Concept Artifact

Defines high-level story, purpose, boundaries, and child roadmap.

## Child Scenario Or Sub-Artifact

Defines focused detail under a parent.

## Workflow

Defines process, sequence, responsibilities, transitions, and exceptions.

## State/Event Model

Defines states, events, triggers, transitions, and effects.

## Screen Or Interface Artifact

Defines UI or interaction behavior when relevant.

## Research Note

Captures sources, claims, methods, and synthesis.

## Lesson Or Learning Module

Defines learning content and progression.

## Policy Or Procedure

Defines operational rules and steps.

## Implementation Note

Defines technical execution detail.

Do not use all artifact types by default.

---

# Choosing Artifact Type

Before generating an artifact, determine:

1. what work type this is
2. what the user wants now
3. what project standards exist
4. what level of detail is needed
5. what parent context exists
6. what knowledge is required
7. what decisions are accepted
8. what should be deferred
9. what artifact type best fits the next action

Artifact type should follow purpose.

Do not choose PRD because it is familiar.

---

# PRD Is Not Universal

A PRD is useful for product requirements.

It may not be suitable for:

- pure research
- early exploration
- learning plans
- religious study
- legal analysis
- book outlines
- personal knowledge systems
- one-time decisions
- general discussion

If the project is not product-oriented, choose a better artifact type.

If a product project needs PRDs, project-specific PRD standards should live in the project instance layer.

---

# UI And Screen Artifacts Are Not Universal

Screen or UI artifacts are useful only when the project involves interfaces.

Do not put screen-specific standards into general orchestration unless they are framed as a possible artifact type.

Project-specific screen conventions belong in the project instance layer.

A research project, learning project, or knowledge base may not need screen artifacts at all.

---

# Workflow Artifacts Are Not Universal

Workflow artifacts are useful when process, sequence, lifecycle, or handoff matters.

Do not force workflows on every project.

Use workflows when they clarify:

- operations
- user journeys
- research process
- learning progression
- approval flows
- state changes
- implementation sequence
- publication process

---

# Knowledge Artifacts Are Not Optional In Knowledge-Heavy Projects

Some projects require knowledge artifacts before other artifacts.

Examples:

- medical knowledge system
- legal analysis
- religious study
- scientific research
- compliance-heavy product
- financial system
- academic project
- complex marketplace

If knowledge controls quality, do not skip knowledge architecture.

---

# Decision Artifacts

Decision artifacts preserve accepted choices.

A decision log is useful when:

- architecture changes
- standards are accepted
- scope changes
- naming changes
- project type is decided
- roadmap sequence is accepted
- conflicts are resolved
- project-specific rules are approved

Decisions should not disappear into conversation when they control future work.

---

# Documentation Architecture And Roadmap

Documentation architecture says what artifacts exist and how they relate.

Roadmap says when to create or update them.

Do not confuse artifact hierarchy with execution order.

A child artifact may be structurally valid but not roadmap-ready.

A parent artifact may be needed before several children.

---

# Documentation Architecture And Maturity

Artifact hierarchy should match maturity.

Early project:

- lighter hierarchy
- provisional artifacts
- fewer standards

Mature project:

- stronger standards
- clearer hierarchy
- governed decisions
- project-specific artifact conventions

Do not treat many artifacts as maturity.

Assess content and integration.

---

# Documentation Architecture And Layer Ownership

Layer ownership must stay clean.

## Cognitive Runtime

Owns model behavior and output safety.

## Project Orchestration

Owns general methods for documentation architecture.

## Project Instance

Owns actual project-specific documentation standards and artifacts.

If a documentation rule is general, keep it in orchestration.

If it is project-specific, place it in the project instance.

If it is about model output behavior, place it in cognitive runtime.

---

# Documentation Architecture In Project Instance

A project instance may include project-specific documentation standards.

Possible files:

    02_MY_PROJECT/09_PROJECT_DOCUMENTATION_STANDARD.md
    02_MY_PROJECT/06_PROJECT_PRIMITIVES_AND_SHARED_RULES.md
    02_MY_PROJECT/04_PROJECT_STRUCTURE_TREE_INDEX.md

Exact names depend on the project.

The project-specific documentation standard may define:

- artifact types used by the project
- naming rules
- parent/child rules
- traceability rules
- review rules
- update rules
- language conventions
- local examples
- local exclusions

---

# Orphan Artifact Detection

An artifact may be orphaned if:

- it has no parent
- it is not referenced by structure
- it does not map to project objectives
- it uses unknown terminology
- it conflicts with standards
- it duplicates another artifact
- it belongs to another layer
- it has no clear future use

Do not delete automatically.

Classify and recommend action.

Possible actions:

- attach to parent
- move to correct folder
- convert to raw reference
- merge
- rewrite
- archive
- update structure index
- create missing parent

---

# Misplaced Artifact Detection

An artifact may be misplaced if:

- project-specific content is in upper layers
- general method is in project instance
- cognitive behavior rule is in project artifact
- a child artifact lives outside its parent branch
- raw source is treated as final artifact
- implementation detail is inside identity
- screen detail is inside broad project standard
- project roadmap is inside general orchestration

Preserve useful content.

Move or reframe it.

---

# Duplicate Artifact Handling

Duplicate artifacts may be:

- harmful duplication
- intentional reinforcement
- scaffolding
- old version
- migration residue
- parallel draft
- conflict

Classify before deleting.

If duplication is useful reinforcement, keep it compact.

If duplication creates conflicting truth, consolidate or decide.

---

# Artifact Granularity

Artifact granularity should match purpose.

Too large:

- hard to review
- mixes levels
- causes contradictions
- slows updates

Too small:

- fragments meaning
- creates too many files
- increases navigation burden
- simulates maturity

The model should recommend granularity that supports future use.

---

# Parent Artifact Content Guidance

A parent artifact may include:

- purpose
- identity of the area
- scope and boundaries
- high-level user or knowledge journey
- major concepts
- major relationships
- major decisions
- child artifact map
- open questions
- non-goals
- dependencies

A parent artifact should usually avoid:

- every field
- every UI component
- every technical implementation detail
- every microstate
- every validation rule
- every local exception
- every source quote
- every task

---

# Child Artifact Content Guidance

A child artifact may include:

- detailed branch purpose
- inherited parent context
- local scope
- detailed process
- specific rules
- examples
- edge cases
- local states or events
- field behavior if relevant
- local decisions
- implementation or execution implications
- open questions specific to the child

A child should not redefine the whole project.

---

# Workflow Artifact Content Guidance

A workflow artifact may include:

- trigger
- actors
- steps
- decisions
- inputs
- outputs
- states
- events
- exceptions
- responsibilities
- audit points
- notifications
- completion conditions

Use workflow artifacts only when process matters.

---

# Research Artifact Content Guidance

A research artifact may include:

- research question
- scope
- source list
- method
- evidence hierarchy
- claims
- counterclaims
- findings
- uncertainty
- synthesis
- implications
- next research steps

Do not force PRD structure on research artifacts.

---

# Learning Artifact Content Guidance

A learning artifact may include:

- learning objective
- prerequisite knowledge
- concepts
- examples
- exercises
- assessment
- resources
- progression
- review plan
- common mistakes

Do not force implementation artifacts on learning work.

---

# Implementation Note Content Guidance

An implementation note may include:

- technical context
- dependency
- data model implication
- API implication
- service boundary
- risk
- assumptions
- open technical questions
- acceptance considerations

Implementation notes should not rewrite project identity.

---

# Documentation Architecture Output Patterns

Use different output patterns depending on intent.

## Quick Recommendation

Use when the user asks what artifact is needed next.

## Hierarchy Map

Use when artifact relationships are unclear.

## Artifact Boundary Advice

Use when a file is mixing levels.

## Documentation Architecture Proposal

Use when a project needs a documentation system.

## Project-Specific Standard File

Use when the user asks to generate the project’s documentation standard.

Place it in the project instance layer.

## Audit

Use when reviewing existing files.

Identify misplaced, orphan, duplicate, weak, mature, or missing artifacts.

---

# Do Not Over-Architect

Avoid creating excessive documentation architecture too early.

Signals of over-architecture:

- many artifact types before identity is stable
- complex hierarchy for simple work
- PRD standards for non-product exploration
- screen standards before interface need exists
- decision logs for one-off questions
- structure maps with no project content

Start with what the project needs now.

---

# Do Not Under-Architect

Avoid weak documentation architecture when complexity is high.

Signals of under-architecture:

- many artifacts with no parent
- project-specific rules scattered in conversation
- recurring decisions not recorded
- children generated before parent
- knowledge-heavy work without source policy
- product work without domain model
- repeated user corrections about lost context
- unclear folder purpose
- AI cannot discover relevant context dynamically

When under-architecture appears, recommend the missing artifact or standard.

---

# Documentation Architecture And Dynamic Discovery

Good documentation architecture supports dynamic discovery.

The model should be able to determine:

- where standards live
- where project truth lives
- what artifact owns the current topic
- what parent governs the child
- what file is raw source
- what file is mature
- what artifact should be updated
- what content should not be edited
- what branch to inspect next

If dynamic discovery fails, documentation architecture may need improvement.

---

# Documentation Architecture And Project Instances

A complex project such as a named active project may require rich documentation architecture.

It may need:

- project-specific standards
- structure index
- parent and child PRDs
- workflow artifacts
- state and event models
- screen or interface artifacts
- implementation notes
- knowledge references
- decision logs

These belong inside the active project instance.

The general orchestration layer provides the method.

Do not copy project-specific artifact types into every project as mandatory.

---

# Failure Signals

Documentation architecture failures include:

- forcing PRDs on non-product work
- forcing UI standards on projects without interfaces
- putting project-specific documentation rules in orchestration
- putting general documentation method in project instance
- generating child artifacts without parent context
- mixing parent and child detail
- creating many files with unclear ownership
- treating raw references as final artifacts
- losing decisions in conversation
- duplicating shared logic across artifacts
- confusing folder structure with documentation hierarchy
- confusing roadmap with artifact hierarchy
- making the system too abstract to guide real project work

When failure occurs, correct artifact ownership and hierarchy before generating more content.

---

# Final Principle

Documentation architecture is how project intelligence becomes durable.

The model must place the right knowledge in the right artifact at the right level.

Strong documentation hierarchy lets any future conversation, artifact, or implementation continue from preserved meaning instead of reconstructing context from scratch.