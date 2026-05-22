# PROJECT STANDARD LAYER FACTORY

# Purpose

This file defines how the model should propose, create, evolve, and maintain a project-specific standard layer.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific standard.

It is not a project identity document.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define the general method for creating the third layer: the project instance standard layer.

This layer is where a specific project stores its identity, objectives, standards, taxonomies, structure, decisions, and project-specific governance.

The project orchestration layer defines how to build that layer.

The project instance layer contains the actual project-specific standards.

---

# Core Principle

Every durable project needs its own standard layer.

But not every conversation needs one immediately.

The model must decide when a project-specific standard layer is useful, what it should contain, how heavy it should be, and how it should evolve.

The standard layer should grow from the user’s actual input and project needs.

It must not be copied blindly from one project to another.

It must not be forced before the idea is ready.

It must not be skipped when project continuity, consistency, or complexity requires it.

---

# What This File Owns

This file owns the project-orchestration method for building project-specific standard layers.

It defines:

- when a project standard layer is needed
- how to bootstrap a minimal project instance
- how to propose standard files
- how to adapt standards to project type
- how to avoid overbuilding
- how to evolve project standards progressively
- how to distinguish seed standards from mature standards
- how to decide what belongs in the project instance layer
- how to prevent project-specific standards from polluting general layers
- how to preserve accepted project-specific decisions
- how to validate the general method against a real active project without making that project universal

This file does not own:

- the final standards of a specific project
- the identity of a specific project
- the objectives of a specific project
- the taxonomy of a specific project
- the structure tree of a specific project
- project-specific decisions
- project-specific artifacts
- implementation details

Those belong in the project instance layer.

---

# Standard Layer Definition

A project standard layer is the numbered root tunnel inside a project instance.

Example:

    02_MY_PROJECT/
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

This example is not mandatory for every project.

The model must adapt the standard layer to the project type and maturity.

The numbered root files in the project instance form the project-specific tunnel.

Non-numbered folders and files after the tunnel are project content.

---

# Minimal Standard Layer

A valid project instance may start with only two standard files:

    02_MY_PROJECT/
      00_PROJECT_STANDARD_SEED.md
      99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md

This is valid.

It means the project instance exists and is ready to grow.

It does not mean the repository is weak or broken.

The model should use the seed file and reinforcement file to understand that project-specific standards may still be emerging.

---

# Purpose Of The Seed File

The project seed file should establish:

- this folder is the project instance layer
- the project may be incomplete or emerging
- the model should extract project standards from conversation and artifacts
- the model should not assume missing standards are failure
- numbered root files form the project-specific tunnel
- non-numbered folders and files are project content
- the model should propose additional standard files only when useful
- project-specific truth belongs here, not in the upper layers

The seed file is not the final identity.

It is the starting point for project-specific standard development.

---

# Purpose Of The Project Reinforcement File

The project instance reinforcement file should remind the model:

- preserve project-specific decisions
- use the project standard tunnel before deep project work
- do not overwrite accepted project standards casually
- treat conversation updates as possible project changes
- classify project artifacts before judging them
- preserve local project terminology
- do not turn upper-layer general methods into project-specific truth unless accepted
- do not ignore project-specific standards when generating artifacts

The reinforcement file is compact.

It reinforces project-local behavior.

---

# When To Create A Standard Layer

Recommend creating or expanding a project standard layer when:

- the user wants continuity
- the work will span multiple sessions
- the idea has multiple parts
- decisions must persist
- future outputs depend on current rules
- the user is building a project, research system, learning system, knowledge base, product, or documentation workspace
- repeated corrections indicate standards are needed
- project-specific terminology is emerging
- there are multiple artifacts or expected artifacts
- repository memory would improve future answers
- losing context would damage quality

Do not recommend a standard layer for every casual conversation.

---

# When To Stay Lightweight

Stay lightweight when:

- the user is exploring briefly
- the task is one-time
- the user only needs an answer
- the idea is too early
- project type is unclear
- standards would create friction
- the user has not asked for continuity
- future work is unlikely

Lightweight does not mean careless.

The model can still organize thoughts and suggest future structure.

---

# Project Type Determines Standards

Different project types need different standard layers.

Do not force one template.

## Software Or Product Project

May need:

- identity and objectives
- domain taxonomy
- state taxonomy
- event taxonomy
- structure tree
- PRD standard
- workflow standard
- screen or interface standards
- implementation note standard
- decision log
- roadmap

## Research Project

May need:

- research identity and question
- scope and methodology
- evidence hierarchy
- source policy
- literature map
- claim taxonomy
- findings log
- citation rules
- decision and uncertainty log
- publication or output plan

## Learning Project

May need:

- learning goal
- current level
- target level
- curriculum map
- prerequisite map
- resource policy
- practice plan
- assessment method
- progress log
- review schedule

## Knowledge Base

May need:

- domain scope
- concept taxonomy
- source hierarchy
- note structure
- claim confidence rules
- glossary
- topic map
- update policy
- synthesis method

## Writing Or Book Project

May need:

- purpose and audience
- voice and style guide
- theme map
- outline
- source notes
- chapter structure
- revision rules
- publication plan

## Operational System

May need:

- process identity
- roles
- policies
- workflows
- state definitions
- event triggers
- SOPs
- responsibility matrix
- audit and escalation rules

The model should infer or ask what type of standard layer fits the work.

---

# Standard Layer Growth Stages

A project standard layer can grow progressively.

## Stage 0 — No Project Instance

The user is discussing or exploring.

No project standard layer exists.

Behavior:

- help clearly
- do not invent current project files
- suggest project instance only if useful

## Stage 1 — Seeded Project Instance

Only seed and reinforcement files exist.

Behavior:

- treat this as valid
- extract identity and standards from conversation
- propose next standard files gradually

## Stage 2 — Basic Standards

Identity, objectives, and initial structure exist.

Behavior:

- use standards for project-specific answers
- identify gaps
- propose missing standards when useful

## Stage 3 — Domain Standards

Taxonomies, knowledge maps, decision logs, and shared rules exist.

Behavior:

- preserve project-specific terminology and logic
- generate artifacts with stronger consistency

## Stage 4 — Artifact Governance

PRD, workflow, screen, research, or implementation standards exist as needed.

Behavior:

- generate artifacts according to project-specific conventions

## Stage 5 — Mature Project Intelligence

The project has strong standards, artifacts, decisions, roadmap, and knowledge continuity.

Behavior:

- act project-native
- detect contradictions
- preserve standards
- produce high-quality artifacts efficiently

Stages are dynamic.

Do not store fixed stage as permanent status unless the project instance intentionally records an audit.

---

# Standard File Selection Method

When proposing standard files, consider:

1. project type
2. project maturity
3. user intent
4. continuity need
5. knowledge complexity
6. artifact complexity
7. implementation need
8. collaboration need
9. decision persistence
10. risk of context loss
11. domain specificity
12. existing repository structure
13. current conversation corrections
14. user tolerance for structure

Do not propose too many files at once unless the user wants a full architecture.

Prefer the minimum useful standard layer.

---

# Minimum Useful Standard Layer

For most project candidates, the first useful standard layer is:

    00_PROJECT_STANDARD_SEED.md
    01_PROJECT_IDENTITY_AND_OBJECTIVES.md
    99_PROJECT_INSTANCE_REINFORCEMENT_MEMORY.md

If the project is complex, add:

    02_PROJECT_DOMAIN_AND_STATE_TAXONOMY.md
    03_PROJECT_EVENT_TAXONOMY.md
    04_PROJECT_STRUCTURE_TREE_INDEX.md
    05_PROJECT_KNOWLEDGE_MAP.md
    06_PROJECT_DECISION_LOG.md

If the project needs artifacts, add artifact-specific standards later.

Do not add artifact-specific standards before project identity and objectives are stable enough.

---

# Project-Specific Standards Belong In Project Instance

A rule belongs in the project instance if it defines how a specific project should behave, be documented, or be implemented.

Examples:

- project-specific identity
- project-specific objectives
- project-specific state taxonomy
- project-specific event taxonomy
- project-specific UI conventions
- project-specific PRD traceability rules
- project-specific implementation assumptions
- project-specific folder structure
- project-specific business logic
- project-specific terminology
- project-specific acceptance criteria

Do not place these in cognitive runtime or project orchestration.

---

# General Methods Belong In Project Orchestration

A rule belongs in project orchestration if it defines how to build, organize, evaluate, or evolve projects generally.

Examples:

- how to extract identity
- how to classify raw input
- how to propose a standard layer
- how to assess maturity
- how to build a roadmap
- how to generate artifacts from accepted standards
- how to organize knowledge
- how to handle decisions
- how to migrate project structures

Do not put one project’s truth inside general methods.

---

# Cognitive Rules Belong In Cognitive Runtime

A rule belongs in cognitive runtime if it defines how the model should behave across all work.

Examples:

- context synchronization
- intent detection
- evidence discipline
- output safety
- path safety
- copy-block safety
- conversation memory
- failure recovery
- tunnel discovery

Do not place cognitive behavior rules inside a project instance unless they are local reminders derived from general behavior.

---

# Adapting Standards To Project Type

Before generating standard files, classify the project type.

Then ask:

- What must be preserved?
- What future outputs will depend on this?
- What errors would occur without standards?
- What decisions need memory?
- What knowledge needs structure?
- What artifacts are likely?
- What should remain flexible?
- What should be fixed now?
- What should wait?

A strong standard layer is tailored, not templated.

---

# Avoid File Explosion

Do not create many files just because the architecture allows them.

Too many early files can:

- overwhelm the user
- create empty scaffolds
- reduce clarity
- increase maintenance
- simulate maturity without content
- make the model follow structure without understanding

Prefer staged creation.

Create or propose files when they solve a real continuity or reasoning problem.

---

# Avoid Under-Structuring

Do not avoid structure when the project clearly needs it.

Under-structuring causes:

- repeated explanations
- inconsistent decisions
- weak artifacts
- lost terminology
- poor project memory
- generic answers
- difficulty scaling
- unclear next steps

If the user is building something durable, standards are useful.

---

# Seed To Standard Evolution

When moving from seed to standards:

1. identify accepted project identity
2. identify accepted objectives
3. identify project type
4. identify required standard categories
5. identify which standards are missing
6. propose one or a small group of next files
7. generate only what the user accepts or clearly requests
8. preserve project-specific decisions in the project instance

Do not jump from seed to full mature repository unless requested.

---

# Conversation To Standard Conversion

User conversation may contain project standards.

Convert conversation into project standards when:

- user repeats a rule as important
- user explicitly accepts a principle
- the rule will guide future outputs
- the rule is project-specific
- loss of the rule would harm future work
- the user asks to persist it

Before converting, classify whether the rule belongs in:

- cognitive runtime
- project orchestration
- project instance
- a specific project artifact
- a decision log
- a knowledge map

Do not place every conversation note into standards.

---

# Project Instance Standard File Naming

Standard files inside the project instance should normally use numeric prefixes.

The prefix determines tunnel order.

The file name should describe responsibility.

Examples:

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

Exact names may vary by project type.

Numeric order matters more than exact name registration.

Content confirms responsibility.

---

# Project Content After Standard Tunnel

After the project instance numbered root files are accounted for, non-numbered files and folders are treated as project content unless classified otherwise.

Project content may include:

- product folders
- research folders
- knowledge folders
- modules
- chapters
- workflows
- screens
- PRDs
- implementation notes
- raw references
- source files
- data files
- decision artifacts

The model should inspect project content dynamically based on user intent.

Project content should not need to be fully pre-registered to be discoverable.

---

# Standard Layer And Project Instances

A complex project instance should live in the project instance layer.

The active project may have a rich standard layer and many project content folders.

The upper layers should help the active project by:

- preserving tunnel discipline
- enforcing layer ownership
- preventing context loss
- improving artifact quality
- identifying misplaced rules
- preserving project-specific standards
- supporting dynamic discovery
- helping produce better PRDs, workflows, and implementation notes

Generalizing the upper layers must make the active project stronger, not weaker.

---

# Standard Layer Audit

When auditing a project instance standard layer, inspect:

- whether seed exists
- whether reinforcement exists
- whether identity exists
- whether objectives exist
- whether project type is clear
- whether structure tree exists
- whether knowledge needs are captured
- whether decision memory exists
- whether artifact standards are appropriate
- whether project-specific rules are misplaced
- whether general rules polluted the project instance
- whether important standards are missing
- whether files are placeholders, raw, mature, outdated, or conflicting

Do not judge by file existence alone.

---

# Standard Layer Maturity

The standard layer may be:

## Missing

No project instance standards exist.

## Seeded

Only seed and reinforcement exist.

## Emerging

Identity or objectives are forming.

## Basic

Identity, objectives, and structure exist.

## Developed

Domain standards, knowledge map, decision log, and shared rules exist.

## Mature

Standards guide artifacts consistently and project-specific outputs are strong.

Maturity is dynamic.

Do not store it as permanent status in this file.

---

# Standard Layer Conflict Handling

Conflicts may occur when:

- conversation updates identity but identity file is old
- project-specific rule exists in upper layer
- two standards disagree
- project folder structure contradicts structure tree
- old artifact conflicts with new objectives
- seed file says one thing and later standards say another
- project type changed

Handle conflicts by:

1. identifying the conflict
2. identifying likely newer source
3. identifying authoritative layer
4. recommending update or asking a focused question
5. avoiding silent merge

---

# Standard Layer Output Patterns

Depending on user intent, output may be:

## Recommendation

Suggest whether a standard layer is needed.

## Minimal Seed Proposal

Suggest seed and reinforcement files.

## Standard Layer Map

List proposed project-specific standard files.

## Gap Analysis

Identify missing standards.

## File Generation

Generate a specific standard file in the project instance.

## Migration Plan

Move misplaced project-specific rules into the project instance.

Do not generate all standards unless the user asks or the project is ready.

---

# Standard Layer Creation Sequence

A safe default sequence:

1. create or confirm project instance seed
2. create or confirm project instance reinforcement
3. extract identity and objectives
4. create identity and objectives file
5. create structure tree if project scope requires it
6. create domain or knowledge taxonomy if needed
7. create decision log if decisions are accumulating
8. create artifact-specific standards only when artifacts become necessary
9. generate project content according to standards

This sequence may change based on project type.

---

# User As Standard Co-Designer

The user may be designing the standard layer itself.

In that case, the model should:

- preserve the user’s conceptual intent
- identify layer implications
- suggest refinements
- warn against overfitting
- warn against losing effective rules
- propose practical file structures
- generate files only when direction is accepted
- avoid replacing user vision with generic templates

The standard layer should reflect the project’s real needs.

---

# Avoiding False Maturity

A standard layer with many files is not automatically mature.

False maturity occurs when:

- many files exist but are empty
- standards are generic
- project identity is unclear
- objectives are vague
- project content does not follow standards
- decisions are not captured
- artifacts contradict standards
- files are copied scaffolds without project truth

Assess maturity from content and usage, not count.

---

# Avoiding Fragility

A standard layer should not be so rigid that the project cannot evolve.

Healthy standards:

- guide future outputs
- preserve decisions
- reduce repetition
- support change control
- identify open questions
- adapt to new accepted decisions
- avoid over-specifying immature areas

Standards should enable intelligence, not freeze exploration.

---

# Relationship With Other Orchestration Files

This file works with:

- raw input understanding
- project classification
- identity and objective extraction
- structure and domain modeling
- maturity and artifact intent assessment
- knowledge discovery
- roadmap method
- documentation architecture
- artifact generation and revision
- decision memory
- project instance handoff

It should not duplicate all of them.

It defines the factory for the project-specific standard layer.

---

# Failure Signals

Standard layer failures include:

- creating a heavy standard layer too early
- failing to create standards when continuity clearly needs them
- copying one project’s standards into all projects
- placing project-specific standards in project orchestration
- placing general methods in project instance
- creating many empty files
- treating seed-only project as broken
- treating file count as maturity
- ignoring project type
- ignoring user decisions
- overwriting accepted project standards casually
- failing to use project standards when generating artifacts

When failure occurs, correct the layer and continue.

---

# Final Principle

The project standard layer is the project’s local mind.

The project orchestration layer teaches the model how to build that local mind.

A strong standard layer is tailored, progressive, durable, and useful.

It should make future project work more accurate, consistent, and intelligent.
---

# Project-Local 360 Standards Must Be Built From Project Type

When creating or strengthening a project-specific standard layer, the model must not copy one project's 360 method into another project.

The project-local 360 method must be derived from the project's type, objective, domain, maturity, artifacts, execution path, and risks.

Examples:

- a software platform may need a local 360 loop connecting documentation, implementation translation, data model, API contracts, engineering environment, tests, deployment, and product objective;
- a research project may need a local 360 loop connecting research questions, sources, methodology, evidence grading, analysis, citation discipline, and publication output;
- a writing project may need a local 360 loop connecting premise, world rules, character arcs, plot continuity, tone, scene sequence, and revision memory;
- an operational process may need a local 360 loop connecting actors, responsibilities, handoffs, compliance, records, metrics, escalation, and auditability.

The upper layers provide the method for discovering and building these loops.

The project instance owns the actual project-specific loop.

---

# Standard Layer Must Support Raw-To-Gold Transformation

A project-specific standard layer should not only store headings, folder maps, or templates.

It should help the expert project engineer transform rough project input into mature project output.

A mature project standard layer should therefore help answer:

- what the project is trying to achieve;
- what sections or modules exist;
- how project lifecycle works;
- which shared primitives govern repeated logic;
- how raw scenarios should be tested against project reality;
- what domain knowledge applies;
- what downstream execution or delivery requires;
- how to classify confirmed truth, inference, recommendation, and open decisions.

If repeated raw-to-gold failures occur inside one project, the model should strengthen the project-local standards before patching the general layer again.
