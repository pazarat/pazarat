# PROJECT KNOWLEDGE DISCOVERY AND LEARNING MAP

# Purpose

This file defines how the model should discover, organize, evaluate, and route project-related knowledge needs.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific knowledge map.

It is not a domain encyclopedia.

It is not a research report.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, folder, file, knowledge gap, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for identifying what knowledge a project needs, how that knowledge should be organized, when research is required, and when knowledge should become part of the project instance layer.

The project orchestration layer defines how to discover and structure knowledge.

The project instance layer stores project-specific knowledge standards, maps, references, decisions, and accepted domain understanding.

---

# Core Principle

Every project depends on knowledge.

Some knowledge is general.

Some knowledge is domain-specific.

Some knowledge is project-specific.

Some knowledge is uncertain, disputed, current, high-stakes, or incomplete.

The model must identify what type of knowledge is involved before using it.

The model must not replace project-specific truth with generic knowledge.

The model must not pretend missing knowledge is available.

The model must not turn every knowledge question into a heavy research project.

Knowledge should improve clarity, decisions, standards, artifacts, and execution.

---

# What This File Owns

This file owns the project-orchestration method for knowledge discovery and learning map creation.

It defines:

- how to identify project knowledge needs
- how to classify knowledge type
- how to distinguish general knowledge from project-specific knowledge
- how to detect knowledge gaps
- how to decide when research is required
- how to build a project knowledge map
- how to support learning projects
- how to support research projects
- how to support domain-heavy product projects
- how to preserve evidence and uncertainty
- how to route accepted knowledge into the project instance layer
- how to avoid shallow or generic knowledge artifacts

This file does not own:

- a specific project’s final knowledge map
- a specific project’s domain taxonomy
- a specific project’s evidence hierarchy
- a specific project’s source list
- a specific project’s accepted research findings
- a specific project’s learning curriculum
- a specific project’s domain rules
- current external facts

Those belong in the project instance layer or require current research when accuracy depends on external facts.

---

# Knowledge Is Not Always Research

The model must distinguish knowledge work types.

## Explanation

The user wants to understand a concept.

## Learning

The user wants to develop skill or comprehension over time.

## Research

The user wants evidence, sources, comparison, verification, or findings.

## Domain Modeling

The user needs to define concepts, entities, categories, rules, or relationships inside a project.

## Project Knowledge Standard

The project needs durable rules about how knowledge should be gathered, trusted, cited, updated, or used.

## Decision Support

The user needs knowledge to choose between options.

## Artifact Support

The project needs knowledge to produce a PRD, policy, roadmap, workflow, lesson, paper, or implementation note.

Different knowledge work types require different outputs.

Do not treat them all as the same.

---

# Knowledge Type Classification

Before using or organizing knowledge, classify it.

## General Knowledge

Broad, stable, commonly understood knowledge.

Use it to explain, compare, or reason.

Do not treat it as project-specific truth.

## Domain Knowledge

Knowledge about a field, market, discipline, craft, system, or professional area.

It may require research, expertise, or source discipline.

## Project-Specific Knowledge

Knowledge accepted for a particular project.

It belongs in the project instance layer.

## Current Knowledge

Knowledge that may change over time.

It should be verified when accuracy matters.

## High-Stakes Knowledge

Knowledge that may affect health, law, finance, safety, compliance, religion, security, or critical decisions.

It requires careful uncertainty and verification.

## Procedural Knowledge

Steps, workflows, methods, or operating procedures.

May belong in project artifacts if accepted.

## Tacit Knowledge

User knowledge, preferences, repeated corrections, or working assumptions that are not yet formalized.

May need capture if it guides future project work.

## Missing Knowledge

Knowledge that is needed but not yet available.

Must be surfaced, not hidden.

---

# Knowledge Discovery Questions

When discovering project knowledge needs, internally ask:

1. What type of project or work is this?
2. What domain does it involve?
3. What concepts must be understood?
4. What decisions depend on knowledge?
5. What artifacts require knowledge support?
6. What knowledge is already documented?
7. What knowledge is only conversation-stated?
8. What knowledge is inferred?
9. What knowledge is missing?
10. What knowledge is uncertain or disputed?
11. What knowledge may be current or time-sensitive?
12. What knowledge is high-stakes?
13. What should become a project-specific knowledge standard?
14. What should remain general background?
15. What needs research before finalization?

Do not expose this full checklist unless the user asks for a knowledge audit or research planning.

---

# Knowledge Gap Signals

A project may have a knowledge gap when:

- the domain is specialized
- the user asks for precise rules
- the topic is regulated
- current facts may have changed
- artifacts depend on external facts
- the project requires domain accuracy
- implementation decisions depend on unknown constraints
- the same concept is described inconsistently
- files use terms without definitions
- standards are being written without domain basis
- the user relies on assumptions not yet validated
- the project is entering a new domain branch

Knowledge gaps should be identified before producing final-sounding artifacts.

---

# Knowledge Is Contextual

The same knowledge may be used differently depending on project type.

A payment concept in a SaaS project may affect:

- product requirements
- compliance
- user flow
- data model
- reporting
- risk controls
- implementation notes

A payment concept in a learning project may affect:

- lesson sequence
- examples
- exercises
- glossary

A payment concept in a research project may affect:

- sources
- claims
- comparative analysis
- citations

The model must adapt knowledge use to project context.

---

# Project Knowledge Map

A project knowledge map is a project-specific artifact that organizes what the project needs to know.

It may include:

- knowledge domains
- key concepts
- source types
- evidence hierarchy
- open questions
- assumptions
- verified facts
- disputed claims
- glossary
- research priorities
- learning needs
- knowledge owners
- update policy
- artifact dependencies

The knowledge map belongs in the project instance layer.

This orchestration file defines when and how to create one.

---

# When A Knowledge Map Is Needed

Recommend a project knowledge map when:

- the project is domain-heavy
- the project has specialized concepts
- research affects future artifacts
- knowledge gaps are blocking progress
- repeated terminology needs consistency
- external sources are important
- current or regulated information matters
- multiple artifacts depend on shared knowledge
- the user is building a knowledge base
- the project is academic, scientific, religious, medical, legal, financial, or technical
- the project must preserve learning or research over time

Do not create a knowledge map for every small question.

---

# Minimal Knowledge Map

For an early project, a minimal knowledge map may include:

- domain areas
- key concepts
- known assumptions
- open questions
- required research
- trusted source types
- first knowledge artifacts

A minimal map is useful when the project needs continuity but is not ready for a full research system.

---

# Mature Knowledge Map

A mature knowledge map may include:

- domain taxonomy
- evidence hierarchy
- source policy
- glossary
- concept relationships
- accepted definitions
- unresolved disputes
- research notes
- decision impacts
- update schedule
- artifact dependencies
- citations or references
- confidence levels
- ownership of knowledge areas

A mature map should support reliable project work.

It should not become a dumping ground for every note.

---

# Knowledge Map File Placement

Project-specific knowledge maps belong in the project instance layer.

Possible path:

    02_MY_PROJECT/05_PROJECT_KNOWLEDGE_MAP.md

or another project-specific equivalent.

If the project has many knowledge domains, it may also contain a non-numbered knowledge folder after the project-specific numbered tunnel.

Example:

    02_MY_PROJECT/
      05_PROJECT_KNOWLEDGE_MAP.md
      knowledge/
      research/
      sources/

Exact structure depends on the project type.

---

# Knowledge And Project Standards

Knowledge may become a project standard when it governs future work.

Examples:

- source quality rules
- citation rules
- evidence hierarchy
- terminology policy
- glossary rules
- domain assumptions
- currentness policy
- research update policy
- accepted definitions
- risk classification
- decision evidence requirements

These belong in the project instance layer if project-specific.

The project orchestration layer may define how to create them.

---

# Knowledge And Domain Taxonomy

A domain taxonomy defines project concepts and categories.

It may include:

- entities
- roles
- states
- event types
- concepts
- source categories
- claim categories
- knowledge domains
- lesson categories
- research themes
- regulatory categories
- risk categories

If the taxonomy is project-specific, it belongs in the project instance layer.

Do not turn general concepts into project taxonomy unless accepted.

---

# Knowledge And State/Event Modeling

Some project knowledge involves states and events.

This is common when the project includes:

- workflows
- approvals
- lifecycle management
- learning progress
- research pipeline
- operational process
- user verification
- transactions
- governance
- automation

State and event knowledge should be project-specific when used to control artifacts or implementation.

General orchestration may explain how to discover it, but not hardcode a specific project’s states.

---

# Knowledge And Decision Memory

Knowledge often leads to decisions.

When knowledge produces an accepted project decision, route it to decision memory.

Examples:

- selecting a domain model
- accepting a source policy
- defining a project term
- choosing a research method
- accepting a risk assumption
- deciding a regulatory boundary
- selecting a learning sequence

Do not let important knowledge decisions disappear in conversation.

---

# Learning Project Method

When the user is building a learning project, knowledge discovery should identify:

- current level
- target level
- prerequisites
- learning domains
- sequence
- practice methods
- assessment methods
- resources
- review schedule
- milestones
- common misconceptions
- knowledge gaps

A learning map belongs in the project instance layer if the learning project is persistent.

Do not force product PRD structure onto learning projects.

---

# Research Project Method

When the user is building a research project, knowledge discovery should identify:

- research question
- scope
- methodology
- source types
- evidence hierarchy
- literature areas
- claim categories
- known debates
- open questions
- citation needs
- uncertainty levels
- synthesis method
- findings structure
- publication or output goals

Research projects need stronger evidence discipline.

Do not generate final claims without evidence.

---

# Knowledge Base Method

When the user is building a knowledge base, knowledge discovery should identify:

- domain scope
- topic hierarchy
- concept taxonomy
- source policy
- glossary
- note types
- confidence levels
- update rules
- synthesis patterns
- relationship mapping
- navigation method

A knowledge base should be structured for retrieval and future reasoning.

---

# Product Knowledge Method

When the user is building a product or system, knowledge discovery should identify:

- domain concepts
- user roles
- workflows
- business rules
- operational constraints
- technical constraints
- regulatory requirements
- data concepts
- risk areas
- implementation dependencies
- user expectations
- market or stakeholder assumptions

Product knowledge should support artifacts and execution.

Do not use generic product assumptions as project truth.

---

# Domain-Heavy Project Signals

A project is domain-heavy if it involves:

- finance
- payments
- taxes
- customs
- shipping
- healthcare
- law
- religious studies
- education
- security
- compliance
- scientific research
- analytics
- AI systems
- marketplace governance
- public policy
- regulated operations

Domain-heavy projects need stronger knowledge maps and source discipline.

---

# High-Stakes Knowledge Handling

For high-stakes knowledge, the model must avoid shallow certainty.

High-stakes areas include:

- medical
- legal
- financial
- tax
- compliance
- security
- safety
- religious rulings when authority matters
- regulated industries
- engineering decisions with safety impact

The model should:

- identify uncertainty
- recommend verification
- use current sources when needed
- separate general information from authoritative advice
- avoid final operational rules without evidence
- mark assumptions
- preserve open questions

High-stakes knowledge may still be organized into a project structure.

But it must be treated carefully.

---

# Current Knowledge Handling

Some knowledge changes over time.

Examples:

- laws
- platform policies
- software APIs
- pricing
- market facts
- regulations
- medical guidance
- technical standards
- product capabilities

When current accuracy matters, research or verification is required.

If research is not available, label the answer as limited.

Do not store volatile current claims as permanent project truth without update policy.

---

# Source Policy

A project may need a source policy.

A source policy may define:

- acceptable source types
- preferred sources
- prohibited sources
- citation expectations
- date sensitivity
- authority hierarchy
- treatment of user-provided sources
- treatment of AI-generated summaries
- update frequency
- evidence confidence levels

Source policy belongs in the project instance layer when project-specific.

---

# Evidence Hierarchy

A project may need an evidence hierarchy.

Examples of evidence levels:

- primary source
- official documentation
- peer-reviewed research
- authoritative commentary
- expert interpretation
- user-provided material
- general knowledge
- inference
- proposal
- assumption

The hierarchy depends on project type.

Do not use the same evidence hierarchy for every project.

---

# Knowledge Confidence Levels

A project may track confidence levels.

Possible levels:

- verified
- documented
- user-provided
- inferred
- proposed
- uncertain
- disputed
- outdated
- requires research

Confidence levels help prevent weak knowledge from becoming final project truth.

---

# Glossary And Terminology

Projects with repeated terms may need a glossary.

A glossary is useful when:

- terms are used inconsistently
- domain terminology matters
- multiple languages are involved
- implementation depends on exact meaning
- users or collaborators need shared understanding
- artifacts use specialized vocabulary

Project-specific glossary belongs in the project instance layer.

---

# Multi-Language Knowledge

Some projects use multiple languages.

The model should preserve:

- official names
- technical identifiers
- translated labels
- domain-specific terms
- user-preferred phrasing
- direction safety in Arabic/English contexts

Do not translate technical terms in ways that break meaning.

Do not mix languages inside project standards without a reason.

---

# Knowledge From Conversation

The conversation may contain important knowledge.

Classify conversation knowledge as:

- user statement
- correction
- decision
- example
- assumption
- raw note
- project-specific standard candidate
- research question
- glossary candidate
- open issue

If conversation knowledge should persist, recommend placing it in the project instance layer.

---

# Knowledge From Repository

Repository knowledge may be:

- accepted
- outdated
- raw
- duplicated
- conflicting
- project-specific
- general method
- misplaced
- placeholder
- source material

Do not assume repository text is current truth without checking context.

If repository knowledge conflicts with conversation, classify the conflict.

---

# Knowledge From External Research

External research should be used when needed and available.

When using external research:

- prefer authoritative sources
- match citations to claims
- avoid overquoting
- distinguish current facts from general principles
- note limitations
- route accepted findings into project instance only when appropriate

External research is not automatically project truth.

The user or project standards may need to accept it.

---

# Knowledge Artifacts

Possible knowledge artifacts include:

- knowledge map
- research plan
- source policy
- glossary
- domain taxonomy
- evidence hierarchy
- literature map
- learning roadmap
- claim register
- assumption log
- open questions list
- synthesis note
- decision impact note
- domain brief
- reference index

Choose the artifact based on need.

Do not create all knowledge artifacts by default.

---

# Knowledge Gap Output Patterns

When a knowledge gap matters, output may include:

## Quick Gap Note

A short statement of what is missing and why it matters.

## Knowledge Gap Map

A grouped list of missing knowledge areas.

## Research Plan

A stepwise plan to verify or collect needed knowledge.

## Source Policy Proposal

A proposed rule for acceptable sources.

## Project Knowledge Map

A project-instance artifact that organizes knowledge domains.

## Artifact Warning

A warning that final artifact generation should wait for research.

Do not overuse warnings when a provisional answer is acceptable.

---

# Knowledge And Roadmap

Knowledge work may affect the roadmap.

A project may need to research before building.

A learning project may need prerequisites before advanced topics.

A product may need compliance knowledge before implementation.

A research project may need source collection before synthesis.

The model should identify when knowledge must come before artifacts.

---

# Knowledge And Artifact Generation

Before generating a knowledge-dependent artifact, ask internally:

- is the domain understood enough?
- is the claim current?
- is this high-stakes?
- are assumptions clear?
- are open questions captured?
- should the artifact be provisional?
- should research come first?
- should knowledge map be generated first?

If knowledge is insufficient, either produce a provisional artifact with assumptions or recommend knowledge work first.

---

# Avoid Knowledge Overload

Do not overload the user with every possible knowledge issue.

Prioritize:

- knowledge that affects the current decision
- knowledge that affects future artifacts
- knowledge that prevents errors
- knowledge that must persist
- knowledge that blocks progress
- high-risk knowledge gaps

Keep knowledge work practical.

---

# Avoid Shallow Knowledge

Do not produce shallow final outputs in domain-heavy areas.

If the model lacks enough knowledge:

- identify missing knowledge
- define assumptions
- recommend research
- create a knowledge map
- ask a focused question
- produce a provisional version only when useful

Shallow certainty is worse than useful uncertainty.

---

# Knowledge And Project Instances

A complex project instance may require many knowledge domains:

- marketplace governance
- seller verification
- user identity
- approvals
- dashboards
- fulfillment
- payments
- logistics
- analytics
- permissions
- compliance
- UX patterns
- implementation constraints

These belong in the active project instance when accepted.

The general orchestration layer should provide the method, not project-specific knowledge.

A real active project can validate whether the knowledge discovery method supports a large, complex project.

---

# Relationship With Other Orchestration Files

This file works with:

- raw input understanding
- project classification
- identity and objectives
- standard layer factory
- scope and structure modeling
- maturity assessment
- roadmap method
- documentation architecture
- artifact generation and revision
- decision memory
- project instance handoff

It should not duplicate all of them.

Its focus is knowledge discovery and knowledge organization.

---

# Failure Signals

Knowledge discovery failures include:

- using general knowledge as project truth
- ignoring project-specific knowledge standards
- generating final artifacts from shallow domain knowledge
- failing to identify high-stakes knowledge
- failing to research current facts when needed
- forcing product knowledge structure onto learning or research projects
- creating a knowledge map when a direct answer is enough
- not creating a knowledge map when project complexity requires it
- storing volatile facts without update policy
- presenting inferred knowledge as documented
- losing user-provided domain knowledge
- ignoring terminology inconsistencies
- missing knowledge gaps that affect decisions

When failure occurs, correct the knowledge classification and continue.

---

# Final Principle

Knowledge is the fuel of project intelligence.

The model must discover what knowledge is needed, distinguish knowledge types, surface gaps, verify current or high-stakes claims when needed, and preserve accepted project knowledge in the project instance layer.

A strong knowledge method makes future artifacts more accurate, consistent, and trustworthy.