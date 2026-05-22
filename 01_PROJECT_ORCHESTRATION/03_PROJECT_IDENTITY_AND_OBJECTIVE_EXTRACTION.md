# PROJECT IDENTITY AND OBJECTIVE EXTRACTION

# Purpose

This file defines how the model should extract, clarify, organize, and validate project identity and objectives.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific identity document.

It is not a project-specific objectives document.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for understanding what a project is, why it exists, who it serves, what it aims to achieve, and what should guide its future artifacts.

Project identity and objectives may later be stored inside the project instance layer.

This file defines how to extract them, not what they are for a specific project.

---

# Core Principle

Do not invent identity.

Extract it from evidence.

Clarify it through conversation.

Stabilize it only when enough signal exists.

Project identity is the anchor of future project work.

Project objectives are the direction of future project work.

If identity or objectives are wrong, later standards, artifacts, roadmaps, and implementation plans will drift.

---

# Project Balance Scale

Project orchestration must treat every new input as a balance between the user’s current intent and the documented project reality.

- The user’s current intent is derived from the live conversation and corrections.
- The documented reality is derived from the project instance tunnel, existing identity files, and persistent objectives.

Before deciding project identity or objectives, the model should:

1. classify the new input as continuation, correction, update, or divergence,
2. compare it with prior conversation state and accepted corrections,
3. compare it with committed project identity/objective evidence,
4. identify whether the new input strengthens, modifies, or conflicts with the existing project definition,
5. if conflict exists, flag it and either request clarification or recommend a project update path,
6. if the input is cumulative, treat it as building on the existing project context rather than replacing it.

This rule prevents the orchestration layer from hijacking the conversation’s emerging intent or from ignoring a real project’s established structure.

---

# What This File Owns

This file owns the general method for project identity and objective extraction.

It defines:

- how to detect identity signals
- how to detect objective signals
- how to distinguish vision, goal, problem, audience, scope, and constraint
- how to work with incomplete or scattered input
- how to extract identity from repositories or conversations
- how to avoid inventing identity
- how to produce a provisional identity
- how to validate identity with the user
- how to route accepted identity into the project instance layer
- how to update identity when new information appears
- how to identify conflicts between old and new identity statements

This file does not own:

- the final identity of a specific project
- the final objectives of a specific project
- project-specific taxonomy
- project-specific structure tree
- project-specific artifacts
- project-specific decisions
- project-specific roadmap
- project-specific implementation rules

Those belong in the project instance layer.

---

# Identity Definition

Project identity answers:

- What is this project?
- Why does it exist?
- Who or what does it serve?
- What problem, ambition, need, or domain does it address?
- What makes it distinct?
- What boundaries define it?
- What should remain true as the project evolves?

Identity is not only a name.

A project name without purpose is not enough.

A project purpose without audience is incomplete.

A project ambition without boundaries may become too broad.

---

# Objective Definition

Project objectives answer:

- What should the project achieve?
- What outcomes matter?
- What should improve?
- What should be built, learned, organized, researched, delivered, or preserved?
- What should future artifacts enable?
- What success direction should guide decisions?
- What must be avoided?

Objectives are not the same as features.

Objectives guide features, artifacts, and decisions.

A feature may change.

A core objective should be more stable.

---

# Identity Signals

The model should look for identity signals in user input and repository content.

Identity signals may include:

- project name
- domain
- target users
- target audience
- beneficiaries
- problem statement
- mission
- core idea
- operating philosophy
- value proposition
- unique approach
- scope boundary
- non-goal
- recurring terminology
- repeated user emphasis
- desired long-term role
- product category
- research category
- learning category
- documentation category
- platform category
- system category

Do not require all signals before forming a provisional identity.

But do not finalize identity from one weak signal.

---

# Objective Signals

The model should look for objective signals.

Objective signals may include:

- desired outcome
- user pain to solve
- quality target
- operational goal
- business goal
- learning goal
- research goal
- documentation goal
- automation goal
- clarity goal
- consistency goal
- execution goal
- continuity goal
- decision quality goal
- user experience goal
- implementation goal
- knowledge preservation goal
- risk reduction goal
- future expansion goal

Objectives may be explicit or implied.

Implied objectives should be labeled as inferred until accepted.

---

# Distinguish Related Concepts

The model must distinguish these concepts.

## Name

The label used to refer to the project.

## Identity

The stable definition of what the project is.

## Vision

The long-term ambition.

## Mission

The project’s reason for existing.

## Problem

The pain, gap, opportunity, or need being addressed.

## Audience

Who benefits from or uses the project.

## Objectives

The outcomes the project should achieve.

## Scope

What the project includes.

## Non-Scope

What the project intentionally excludes.

## Principles

Rules or values that guide decisions.

## Features

Possible capabilities or outputs.

## Artifacts

Documents, files, screens, workflows, notes, plans, or deliverables.

Do not confuse these during extraction.

---

# Input Sources

Identity and objectives may come from multiple sources.

## Conversation

The user may explain the project directly or indirectly.

Conversation is live and may contain newer decisions than the repository.

## Repository

The project instance may contain identity, objectives, standards, artifacts, or old versions.

Repository is persistent but may lag behind recent conversation corrections.

## Uploaded Files

Uploaded files may contain current or historical identity.

Classify them before use.

## Existing Artifacts

Artifacts may imply identity or objectives.

Do not infer too strongly from a single artifact.

## Repeated Corrections

User corrections often reveal hidden objectives.

Example:

If the user repeatedly says the model must not lose context, continuity may be a core objective.

## Proposed Direction

The model may propose an identity or objective, but it remains proposed until accepted.

---

# Extraction From Raw Input

When identity is emerging from raw input:

1. Preserve the user’s original idea.
2. Identify the likely work type.
3. Extract candidate identity signals.
4. Extract candidate objective signals.
5. Separate confirmed from inferred.
6. Avoid over-formal wording too early.
7. Produce a provisional identity only if useful.
8. Ask one focused question if a missing identity decision blocks progress.
9. Recommend bootstrap if identity needs persistence.
10. Store or propose storage only when appropriate.

Do not force a polished identity statement before the user has clarified enough.

---

# Extraction From Existing Project

When a project instance exists:

1. Account for the project instance numbered tunnel.
2. Inspect available identity and objective files if accessible.
3. Compare identity files with current conversation.
4. Identify current documented identity.
5. Identify current documented objectives.
6. Identify conflicts or outdated statements.
7. Identify missing identity elements.
8. Recommend update if conversation has newer accepted direction.
9. Do not replace project identity silently.

Project-specific identity belongs in the project instance layer.

---

# Provisional Identity

A provisional identity is useful when the project is not yet fully defined.

It should be:

- clear
- short
- faithful to user input
- marked as provisional
- not over-polished
- not over-specific
- not presented as final
- useful enough to guide the next discussion

A provisional identity may include:

- project type
- core purpose
- target beneficiary
- main value
- current uncertainty

Example style:

"This appears to be a project candidate for organizing and preserving complex project reasoning through a repository-based cognitive method. The identity is still provisional until the project user, delivery model, and scope are clarified."

Do not use examples as current project truth.

---

# Final Identity

A final or accepted identity should only be used when:

- user explicitly accepts it
- repository documents it clearly
- project instance standards contain it
- enough evidence supports it and no conflict exists

Even final identity may evolve through controlled revision.

Do not treat early wording as permanent if the user is still exploring.

---

# Objective Extraction Method

When extracting objectives:

1. Identify explicit objectives.
2. Identify implied objectives.
3. Separate outcomes from features.
4. Separate short-term goals from long-term goals.
5. Identify constraints and non-goals.
6. Identify quality objectives.
7. Identify operational objectives.
8. Identify knowledge or learning objectives if relevant.
9. Identify documentation or continuity objectives if relevant.
10. Mark inferred objectives as inferred until accepted.

Objectives should guide future project standards and artifacts.

---

# Objective Types

Projects may have different objective types.

## Product Objectives

Related to users, features, workflows, market, product value, and delivery.

## Technical Objectives

Related to architecture, implementation, performance, scalability, security, or maintainability.

## Knowledge Objectives

Related to learning, research, evidence, taxonomy, domain understanding, or teaching.

## Documentation Objectives

Related to preserving context, standards, artifacts, traceability, and consistency.

## Operational Objectives

Related to process, governance, decisions, automation, workflows, roles, or execution.

## Strategic Objectives

Related to long-term positioning, business model, differentiation, or growth.

## Quality Objectives

Related to accuracy, usability, reliability, clarity, safety, or trust.

Not every project needs every type.

The model should select objective types based on project classification.

---

# Avoid Feature Mistaken As Objective

A feature is something the project may include.

An objective is why that feature matters.

Incorrect:

"The objective is to have dashboards."

Better:

"The objective is to provide role-specific operational visibility and control. Dashboards may be one artifact or interface supporting that objective."

Incorrect:

"The objective is to create PRDs."

Better:

"The objective is to preserve project logic in durable artifacts so future design and implementation remain consistent."

This distinction prevents shallow planning.

---

# Avoid Artifact Mistaken As Objective

An artifact is a deliverable.

An objective is an outcome.

Incorrect:

"The goal is to create a file."

Better:

"The goal is to create a durable standard that prevents future context loss."

Files are tools.

Objectives explain why they are needed.

---

# Avoid Name Mistaken As Identity

A project name is not enough.

Incorrect:

"The project is <project_name>."

Better:

"The project is a marketplace/platform/system/etc. named <project_name>, serving X through Y, with objectives Z."

The model must extract meaning, not only labels.

---

# Identity Conflict Handling

Identity conflicts may appear when:

- repository says one thing and conversation says another
- old project files contain outdated identity
- the project has expanded beyond its original scope
- user corrects the model’s understanding
- multiple artifacts describe the project differently
- a proposed identity is not accepted
- a project was migrated to a broader system

When conflict appears:

1. Identify the conflicting sources.
2. Determine which is newer.
3. Determine which is more authoritative for the claim.
4. Ask a focused question if needed.
5. Recommend updating the project instance identity file if a new identity is accepted.

Do not silently merge conflicting identities.

---

# Objective Conflict Handling

Objective conflicts may appear when:

- a short-term feature contradicts long-term direction
- user’s current request conflicts with documented objectives
- old objectives remain in files after strategy changed
- implementation pressure distorts project purpose
- project-specific standards conflict with new ambition

When conflict appears:

- classify it as update, contradiction, or open decision
- do not silently overwrite objectives
- recommend controlled revision if needed

Objectives should be stable enough to guide, but not frozen against accepted evolution.

---

# Identity And Scope

Identity must include scope boundaries when needed.

Scope answers:

- what belongs in the project
- what does not belong
- what may be future expansion
- what is intentionally excluded
- what is unknown

Weak scope causes project drift.

Overly strict scope may block evolution.

Use scope carefully.

---

# Non-Goals

Non-goals are useful when the project risks over-expansion.

Non-goals may include:

- not building implementation yet
- not creating UI before scenario maturity
- not forcing PRDs on knowledge work
- not treating one project as universal method
- not making upper layers project-specific
- not discarding current effective standards during modernization

Non-goals protect focus.

---

# Identity As Future Filter

A clear identity should help decide:

- what files belong
- what standards are needed
- what artifacts should exist
- what knowledge is relevant
- what should be deferred
- what is outside scope
- what project instance should contain
- what project orchestration should not own

If identity does not help decisions, it is too vague.

---

# Objectives As Future Filter

Objectives should help decide:

- what next step matters
- what artifact to create
- what questions to ask
- what risks to address
- what success looks like
- what should not be overbuilt
- what project standards should govern future work

If objectives do not guide action, they need refinement.

---

# Accepted Identity Storage

When identity is accepted and should persist, store or propose storing it inside the project instance layer.

Possible file:

    02_MY_PROJECT/01_PROJECT_IDENTITY_AND_OBJECTIVES.md

or a project-specific equivalent.

Do not store a specific project identity inside project orchestration unless used only as a clearly marked example.

---

# Accepted Objectives Storage

When objectives are accepted and should persist, store or propose storing them inside the project instance layer.

Objectives may be placed with identity or in a dedicated objectives file depending on project complexity.

Do not store current objectives in cognitive runtime or general orchestration files.

---

# Updating Identity

Identity may evolve.

When updating identity:

- preserve accepted prior meaning unless explicitly changed
- identify what changed
- identify why it changed
- identify affected standards or artifacts
- avoid rewriting unrelated project rules
- update project instance files if requested

Do not change identity casually.

---

# Updating Objectives

Objectives may evolve.

When updating objectives:

- separate new objective from existing objectives
- identify whether it replaces, expands, or refines older objectives
- identify affected roadmap, structure, standards, or artifacts
- preserve previous accepted objectives unless contradicted
- record decisions when project instance supports decision logs

---

# Identity Extraction Output Patterns

Use different output patterns depending on user intent.

## Quick Understanding

Use when user asks what the model understands.

Include:

- likely identity
- likely objective
- uncertainty
- next useful question or step

## Provisional Identity Draft

Use when the user wants to clarify an emerging project.

Include:

- project type
- purpose
- audience
- value
- scope
- uncertainty

## Identity Audit

Use when repository or project instance exists.

Include:

- documented identity
- conversation updates
- conflicts
- missing elements
- recommended update

## File Generation

Use when user asks for identity file.

Generate the project instance identity file, not this general method file.

---

# Objective Extraction Output Patterns

Depending on intent, produce:

- concise objective list
- grouped objective map
- accepted versus inferred objectives
- objective conflicts
- objective update proposal
- full objective document inside project instance

Do not overload the user with every possible objective type unless useful.

---

# Minimal Question Rule

Ask a question only when the next output depends on it.

Useful identity questions include:

- Who is the primary beneficiary?
- Is this a product, research project, learning system, or documentation system?
- What outcome matters most first?
- Should this become a persistent project instance?
- Is this identity accepted or still exploratory?

Ask one focused question, not a questionnaire.

---

# Identity And Objectives In Multi-Project Repositories

A repository may contain more than one project instance.

The model must identify which project instance is active before extracting or updating identity.

If unclear, infer from user context.

If still unclear and it matters, ask a focused question.

Do not merge multiple project identities.

---

# Identity And Objectives During Migration

During architecture migration, distinguish:

- identity of the architecture/system being built
- identity of a project instance inside it
- identity of a legacy project being migrated
- identity of a proposed SaaS product based on the architecture

Do not confuse them.

For example:

- the cognitive/orchestration architecture may be a general project intelligence system
- the named project may be a specific project instance
- a future SaaS may be another product built from the architecture

Each may need its own identity.

---

# Failure Signals

Identity and objective extraction failures include:

- inventing identity from weak evidence
- treating project name as full identity
- treating features as objectives
- treating files as objectives
- freezing provisional identity too early
- ignoring user corrections
- merging conflicting identities silently
- storing project identity in the general orchestration layer
- applying one project’s objectives to all projects
- asking too many questions before offering a useful synthesis
- ignoring repository identity when available
- ignoring conversation updates when newer than repository

When failure occurs, correct the extraction method and continue.

---

# Final Principle

Project identity and objectives are the compass of project work.

The model must extract them carefully, distinguish confirmed from inferred, avoid invention, and store accepted identity only in the correct project instance layer.

A strong identity and objective method prevents future artifacts from drifting.