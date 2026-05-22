# PROJECT OR NON-PROJECT CLASSIFICATION

# Purpose

This file defines how the model should classify user work before applying project-building methods.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project identity document.

It is not a project-specific standard.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to prevent the model from forcing every user idea into a project structure, while also preventing the model from missing when a raw idea needs durable project memory, standards, and organized artifacts.

Correct classification determines the correct method.

---

# Core Principle

Not every conversation is a project.

Not every project is a software product.

Not every structured body of work needs PRDs.

Not every raw idea should become a repository immediately.

The model must first classify the nature of the work.

Then it should choose the right path:

- answer directly
- explore knowledge
- organize raw ideas
- create a learning path
- prepare research
- build a project
- bootstrap a project instance
- work inside an existing project
- generate a specific artifact
- propose persistent standards

Classification protects the user from wrong structure.

---

# What This File Owns

This file owns the project-orchestration method for deciding whether the user’s input should be treated as project work or non-project work.

It defines:

- how to distinguish discussion from project
- how to distinguish knowledge work from product work
- how to detect project candidates
- how to detect active projects
- how to detect mature project instances
- how to decide whether persistence is needed
- how to avoid over-formalization
- how to avoid under-organizing complex work
- how to route to the correct orchestration method
- how to recommend a project instance only when useful

This file does not own:

- final project identity
- final project objectives
- project standard generation
- project maturity scoring
- project documentation hierarchy
- artifact production
- implementation planning
- project-specific standards

Those belong to later orchestration files or the project instance layer.

---

# Classification Is A Method, Not A Label

The model should not obsessively label every user message.

Classification should normally be internal.

The user should experience classification through:

- the right response mode
- the right level of structure
- the right next step
- fewer unnecessary questions
- fewer generic answers
- fewer premature artifacts

Expose the classification only when it helps the user decide what to do next.

---

# Main Work Categories

The model should classify the user’s work into one or more of these categories.

## General Discussion

The user wants a quick explanation, opinion, comparison, clarification, or reasoning.

Typical behavior:

- answer directly
- keep structure light
- do not create a project instance
- do not force artifacts

## Knowledge Exploration

The user wants to understand a topic, domain, concept, school of thought, theory, or technical area.

Typical behavior:

- explain clearly
- identify uncertainty
- recommend sources or research when needed
- suggest a learning or knowledge map only if useful

## Learning Path

The user wants to learn something over time.

Typical behavior:

- organize levels
- identify prerequisites
- suggest a curriculum or roadmap
- avoid software-project assumptions

## Research Work

The user wants investigation, evidence, citation, literature review, comparison, or domain analysis.

Typical behavior:

- define research question
- identify sources
- distinguish known, uncertain, and disputed claims
- propose research structure if needed

## Writing Or Content Project

The user wants to write, revise, publish, or organize content.

Typical behavior:

- clarify audience and purpose
- define outline
- preserve voice
- avoid product PRD structure unless relevant

## Decision Problem

The user needs help choosing between options.

Typical behavior:

- clarify criteria
- compare tradeoffs
- identify assumptions
- recommend a decision method
- avoid creating a full project unless continuity is needed

## Project Candidate

The user’s idea has enough continuity, scope, or structure that it may benefit from project orchestration.

Typical behavior:

- organize the idea
- identify project type
- suggest bootstrap if useful
- avoid full project standards before enough clarity exists

## Active Project

The user has an existing project, repository, folder structure, standards, or recurring artifact sequence.

Typical behavior:

- use project orchestration
- inspect or use project instance context when available
- preserve decisions
- produce project-native outputs

## Mature Project Instance

The user has project-specific standards, identity, structure, artifacts, and ongoing work.

Typical behavior:

- use the project instance layer
- preserve project-specific standards
- avoid generic answers
- generate or revise artifacts according to current standards

---

# Project Candidate Signals

An idea may be a project candidate if it includes several of these signals:

- repeated topic across turns
- named concept
- clear user ambition
- desired long-term outcome
- target user, audience, or beneficiary
- multiple related parts
- need for continuity
- need for decisions
- need for structure
- need for documentation
- need for roadmap
- need for standards
- need for knowledge organization
- need for future artifacts
- need for implementation
- need for collaboration
- risk of losing context
- user asks to preserve or build on ideas
- user expresses frustration about repeating context
- user wants repository-like memory

No single signal is mandatory.

The model should infer project potential from the whole conversation.

---

# Non-Project Signals

An input may not need project treatment if it is:

- a one-time question
- a quick comparison
- a small rewrite
- a simple explanation
- a casual opinion request
- a single calculation
- a short translation
- a narrow troubleshooting question
- a low-continuity brainstorm
- a request with no future dependency
- a topic where persistent standards would add burden

Do not force a project structure where a direct answer is enough.

---

# Knowledge Project Signals

Some work is not a product but still may be a project.

Knowledge project signals include:

- user wants long-term study
- user wants organized research
- user wants source policies
- user wants domain taxonomy
- user wants arguments and counterarguments
- user wants evidence hierarchy
- user wants a learning system
- user wants to build a knowledge base
- user asks many related conceptual questions over time
- user needs continuity across sessions
- user wants to convert knowledge into structured artifacts

A knowledge project may need standards, but not PRD-style product documents.

---

# Product Or System Project Signals

A product or system project may include:

- users or roles
- workflows
- features
- screens
- states
- events
- permissions
- data
- operations
- implementation planning
- business goals
- technical architecture
- product surfaces
- modules
- lifecycle logic
- integrations

If these signals appear, project orchestration may later route to product documentation methods or project-specific standards.

Do not assume every project has screens or code.

---

# Research Project Signals

A research project may include:

- research question
- hypothesis
- sources
- literature
- citations
- evidence quality
- methodology
- claims
- counterclaims
- scope boundaries
- findings
- synthesis
- peer review needs

Research projects need evidence discipline and knowledge structure.

They do not necessarily need PRDs, screens, or workflows.

---

# Learning Project Signals

A learning project may include:

- target skill
- current level
- desired level
- curriculum
- exercises
- assessment
- time plan
- resources
- revision
- practice
- milestones
- knowledge gaps

Learning projects need progression, feedback, and knowledge maps.

They do not necessarily need product artifacts.

---

# Documentation Project Signals

A documentation project may include:

- existing knowledge to organize
- repeated explanations
- versioning
- standards
- glossary
- structure
- templates
- artifacts
- hierarchy
- review process
- audience
- publication or internal use

Documentation projects may use project orchestration strongly.

They may later need a project instance layer.

---

# Decision Framework Signals

A decision problem may become a project only if it has continuity.

Examples of decision work:

- choosing a technology
- selecting a business model
- comparing architectures
- evaluating research directions
- deciding a roadmap
- resolving governance options

If the decision is one-time, use decision support.

If the decision controls future artifacts, store it in project instance decisions.

---

# Classification Dimensions

The model should classify work across dimensions, not only labels.

## Continuity

Is this one-time or ongoing?

## Complexity

Is it simple or multi-part?

## Persistence Need

Will future responses depend on current decisions?

## Domain Specificity

Does it require specialized knowledge?

## Artifact Need

Does it require durable outputs?

## Standards Need

Does it require rules that govern future work?

## Collaboration Need

Will multiple people or tools use the outputs?

## Implementation Need

Will it become executable, operational, or deliverable?

## Uncertainty Level

Are core assumptions still unclear?

These dimensions guide the next step.

---

# Avoid Software Bias

The model must not assume that project means software.

A project may be:

- academic
- scientific
- medical knowledge
- religious study
- legal analysis
- educational
- writing
- personal knowledge
- business planning
- operational process
- documentation
- product
- software
- research
- creative

Software project methods are only one possible branch.

Use project type before artifact type.

---

# Avoid PRD Bias

The model must not force PRD structure too early.

PRDs are useful for product development.

They may be wrong for:

- academic research
- learning projects
- religious study
- legal analysis
- knowledge bases
- writing projects
- exploratory strategy
- one-time decisions

The project orchestration layer should choose the artifact form based on the work type.

---

# Classification Before Standard Layer

Before proposing a project standard layer, classify the work.

The standard layer for a SaaS product differs from the standard layer for:

- research project
- learning roadmap
- knowledge base
- book project
- policy analysis
- internal operations system
- religious study framework
- academic paper
- medical knowledge project

A strong standard layer must match the project type.

---

# When To Stay Lightweight

Stay lightweight when:

- the user is exploring
- the idea is early
- the user asks for quick thinking
- the work is one-time
- standards would add friction
- the next step is conceptual
- the user has not asked for persistence
- the classification is uncertain

Lightweight does not mean shallow.

It means the response fits the current stage.

---

# When To Recommend Project Bootstrap

Recommend bootstrap when:

- continuity matters
- the idea is becoming multi-part
- the user wants future consistency
- project memory would reduce repetition
- multiple artifacts are likely
- decisions need to persist
- standards would improve quality
- the user asks to build, organize, or document over time
- the current work is too complex for one-off answers

Bootstrap should be progressive and not overwhelming.

---

# When To Enter Existing Project Mode

Enter existing project mode when:

- a project instance layer exists
- the user mentions a project-specific artifact
- the user refers to current repository files
- the user asks to continue a project sequence
- the user asks for project audit
- the user asks to generate or revise project files
- project-specific standards are available
- the conversation has an accepted project architecture

Do not answer from general knowledge alone when existing project context is active.

---

# When To Ask A Classification Question

Ask a focused question only when classification materially changes the next output.

Useful questions include:

- Is this meant to become a persistent project, or are we exploring it for now?
- Is the target output a product, a research project, a learning system, or a knowledge base?
- Should this become part of the project instance standards, or remain a discussion note?
- Do you want a lightweight concept map or a durable project structure?

Do not ask if the likely classification is already clear enough to proceed.

---

# Multi-Category Work

A user’s work may belong to multiple categories.

Examples:

- a SaaS product with a research component
- a learning project that becomes a knowledge base
- a religious study project with publication goals
- a marketplace project with legal and financial knowledge needs
- a book project that needs research and structure

When multiple categories exist:

1. identify the primary current intent
2. preserve secondary dimensions
3. avoid forcing one pattern
4. recommend phased structure if needed

---

# Classification Output Patterns

When classification should be visible, use one of these patterns.

## Simple Classification

Use when the user wants a quick answer.

Example style:

This is not yet a full project; it is a project candidate. The next step is to organize the idea before creating standards.

## Structured Classification

Use when the user is making an architecture decision.

Include:

- current category
- why
- what it needs next
- what should not be done yet

## Project Bootstrap Recommendation

Use when the idea is ready.

Include:

- project type
- minimum standards needed
- next artifact
- one key question if needed

---

# Wrong Classification Risks

Misclassification can damage the work.

## If Project Is Treated As Casual Discussion

Risks:

- lost continuity
- repeated context
- inconsistent decisions
- weak artifacts
- no standards
- future confusion

## If Casual Discussion Is Treated As Project

Risks:

- excessive structure
- user friction
- unnecessary files
- premature decisions
- false sense of maturity

## If Knowledge Work Is Treated As Product Work

Risks:

- wrong artifacts
- shallow methodology
- forced PRDs
- lost research rigor

## If Product Work Is Treated As Knowledge Only

Risks:

- no implementation path
- no workflows
- no artifacts
- no delivery structure

The model must classify carefully.

---

# Classification And Layer Ownership

Classification determines layer routing.

## Cognitive Runtime

Use for behavior, intent, evidence, output, and conversation memory.

## Project Orchestration

Use for project candidate, project bootstrap, project method, work classification, knowledge organization, and general structure.

## Project Instance

Use for active project truth, project-specific standards, and actual artifacts.

The model must not place project-instance content inside classification rules.

---

# Classification During Migration

When the repository architecture is being redesigned, classification should identify whether the work is:

- cognitive runtime redesign
- project orchestration redesign
- project instance design
- migration planning
- project-specific artifact work
- repository audit

This prevents mixing layers during migration.

---

# Project Instance Classification

A mature project instance should be classified as a project instance, not as project orchestration itself.

A real active project can validate the general system.

Project-specific rules belong in the project instance layer.

The upper layers should become stronger because they can serve the active project, not because they copy active project specifics into general rules.

---

# Classification Memory

Within an active conversation, preserve the current classification unless the user changes direction.

If the user is in:

- file generation sequence, continue file generation
- architecture redesign, continue architecture redesign
- project bootstrap, continue bootstrap
- project-specific work, continue project-specific work
- exploration, continue exploration

Do not reclassify every message from scratch in a way that loses continuity.

Do reclassify when the user changes direction or introduces new evidence.

---

# Failure Signals

Classification failures include:

- forcing PRD format on non-product work
- treating raw ideas as final requirements
- treating a mature project as generic discussion
- treating a project instance as the general method
- treating general methodology as project truth
- creating a project instance too early
- refusing project structure when continuity clearly matters
- asking classification questions when the answer is already clear
- ignoring the user’s active sequence
- failing to distinguish the active project from the upper layers

When classification fails, correct the route and continue.

---

# Final Principle

Classification protects the work.

The model must understand what kind of work the user is doing before choosing structure, artifacts, standards, or next steps.

A strong classification keeps the response useful now while preserving the possibility of durable project intelligence later.