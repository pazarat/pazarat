# PROJECT ARTIFACT GENERATION AND REVISION METHOD

# Purpose

This file defines how the model should generate, revise, replace, preserve, and improve project artifacts.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific artifact.

It is not a project-specific PRD standard.

It is not a static project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for producing artifacts from project context, user intent, standards, knowledge, maturity, and accepted decisions.

The project orchestration layer defines how artifact generation and revision should work.

The project instance layer stores the actual project-specific artifacts and project-specific artifact standards.

---

# Core Principle

Artifacts must be generated from context, not from templates alone.

A strong artifact should reflect:

- user intent
- project type
- project identity
- project objectives
- project standards
- current maturity
- relevant knowledge
- accepted decisions
- correct layer ownership
- correct artifact type
- correct level of detail
- current conversation corrections
- output safety requirements

The model must not generate polished but context-poor artifacts.

The model must not revise artifacts in ways that lose accepted meaning.

---

# What This File Owns

This file owns the project-orchestration method for artifact generation and revision.

It defines:

- when to generate an artifact
- when not to generate an artifact
- how to select artifact type
- how to place artifacts in the correct layer
- how to generate from raw input
- how to generate from project standards
- how to revise accepted artifacts
- how to preserve accumulated corrections
- how to avoid divergent rewrites
- how to handle missing context
- how to choose patch versus full replacement
- how to assess readiness before generation
- how to create provisional artifacts
- how to avoid false maturity
- how to hand off artifact content to the project instance layer

This file does not own:

- the final content of a specific project artifact
- a specific project’s PRD format
- a specific project’s screen format
- a specific project’s research format
- a specific project’s implementation notes
- a specific project’s acceptance criteria
- a specific project’s current artifact status

Those belong in the project instance layer or current project response when explicitly produced.

---

# Artifact Definition

An artifact is any durable output that may guide future work.

Artifacts may include:

- project standard
- identity document
- objectives document
- structure index
- knowledge map
- decision log
- roadmap
- PRD
- scenario
- workflow
- state or event model
- research note
- source synthesis
- lesson
- curriculum
- policy
- procedure
- implementation note
- architecture note
- glossary
- prompt guide
- operating manual
- audit report
- visual reference description
- code-related documentation

The correct artifact depends on project type and user intent.

Do not force all artifacts into a software PRD pattern.

---

# Artifact Generation Is A Controlled Action

Generating an artifact changes the project’s durable memory if the user saves or accepts it.

Therefore, before generating, the model should check:

- is the artifact requested?
- is the artifact needed now?
- what layer does it belong to?
- what project standards govern it?
- what parent or source context governs it?
- what accepted decisions should be preserved?
- what knowledge is required?
- what uncertainty exists?
- should the output be final, draft, provisional, seed, or patch?
- will generating this artifact create false maturity?
- will this artifact reduce future confusion?

Do not generate artifacts merely because a template exists.

---

# Artifact Readiness Gate

Before generating a significant artifact, internally assess readiness.

Readiness may depend on:

## Identity Readiness

Is the project or artifact area clearly identified?

## Objective Readiness

Is the desired outcome clear enough?

## Scope Readiness

Does the artifact know what it covers and excludes?

## Standard Readiness

Are project-specific standards available or should the artifact be provisional?

## Knowledge Readiness

Is the required domain knowledge sufficient?

## Parent Readiness

Does parent context exist when the artifact is a child?

## Decision Readiness

Are key decisions accepted or still open?

## Maturity Readiness

Is the current material raw, draft, scaffold, or mature?

## Output Readiness

Can the output be generated in a safe, copy-ready, usable form?

If readiness is low, the model may still generate a provisional artifact, but must not present it as final.

---

# When To Generate

Generate an artifact when:

- the user asks for it
- an active generation sequence is underway
- the next step clearly requires a durable artifact
- the project has enough context for the artifact’s intended maturity
- the artifact will preserve decisions or reduce future repetition
- the artifact will clarify structure, standards, knowledge, or execution
- the user wants a complete file
- replacing a weak or misplaced artifact is the accepted next action

Generation should serve the project.

---

# When Not To Generate Yet

Do not generate a full artifact yet when:

- the user is only exploring
- project type is unclear
- identity is too unstable
- parent context is missing
- knowledge gaps are high-stakes and unresolved
- the user asked for discussion, not output
- the artifact would create false maturity
- several incompatible directions remain open
- the artifact belongs to a project instance that does not exist and the user has not accepted creating one
- a small patch would be safer than full regeneration

In these cases, produce a summary, question, plan, or provisional map instead.

---

# Artifact Type Selection

Before generating, choose the artifact type based on purpose.

## Standard

Use when a rule should govern future work.

## Identity Or Objective Document

Use when the project needs a durable definition of what it is and why it exists.

## Structure Index

Use when navigation or dynamic discovery matters.

## Knowledge Map

Use when domain knowledge, sources, terminology, or research gaps matter.

## Decision Log

Use when accepted choices must persist.

## Roadmap

Use when sequencing matters.

## Parent Artifact

Use when a broad area needs context and child roadmap.

## Child Artifact

Use when a focused branch needs detailed treatment.

## Workflow

Use when process, handoff, sequence, or lifecycle matters.

## State/Event Model

Use when transitions, triggers, states, and effects matter.

## Research Artifact

Use when evidence, sources, claims, or findings matter.

## Learning Artifact

Use when teaching, skill progression, or curriculum matters.

## Implementation Note

Use when technical execution details matter.

Do not choose artifact type by habit.

Choose it by project need.

---

# Artifact Placement

Every artifact must belong somewhere.

Placement depends on layer ownership.

## Cognitive Runtime

Only behavior, synchronization, evidence, output safety, intent, and memory rules belong here.

## Project Orchestration

Only general project-building methods belong here.

## Project Instance

Project-specific standards and artifacts belong here.

## Project Content Branches

Detailed project content may live in non-numbered folders after the project instance numbered tunnel.

The model must not place project-specific artifacts in general orchestration.

The model must not place general methods inside project-specific artifacts unless clearly framed as local adoption.

---

# Artifact Generation From Raw Input

When generating from raw input:

1. preserve original user intent
2. identify work type
3. identify artifact type
4. separate accepted from tentative ideas
5. identify missing context
6. decide whether output should be provisional
7. generate only the level of structure justified by input
8. preserve open questions
9. avoid over-polishing away meaning
10. recommend next refinement step if needed

Raw input can become an artifact, but raw input should not be falsely treated as final requirements.

---

# Artifact Generation From Project Standards

When generating from project standards:

1. account for the project instance numbered tunnel
2. identify relevant standards
3. identify relevant parent, structure, knowledge, decisions, and roadmap
4. apply project-specific terminology
5. preserve local rules
6. avoid generic assumptions that conflict with project truth
7. generate at the correct artifact level
8. mark open questions when standards are incomplete
9. update or suggest standard changes if the artifact reveals a gap

Project standards should guide artifacts.

Artifacts should not silently override standards.

---

# Artifact Generation From Existing Artifact

When generating from an existing artifact:

1. classify artifact intent
2. identify whether it is raw, draft, mature, placeholder, scaffold, outdated, or conflicting
3. preserve useful content
4. identify what must change
5. identify what must remain
6. decide patch versus full replacement
7. avoid losing accepted terminology
8. avoid changing unrelated structure
9. preserve or improve traceability
10. output safely

Do not rewrite an accepted artifact as if it were new unless the user asks for full replacement or the artifact is structurally unsalvageable.

---

# Patch Versus Full Replacement

Choose revision method carefully.

## Use Patch When

- the artifact is mostly accepted
- the requested change is small
- exact preservation matters
- the current baseline is available
- the user asks for insertion or correction
- full regeneration would increase review burden
- only one section needs updating

## Use Full Replacement When

- the user asks for complete file
- the architecture changed
- the artifact is being created for the first time
- the existing artifact is misplaced or structurally wrong
- the artifact is a generated proposal not yet accepted
- the user is rebuilding a layer
- patching would create inconsistency

Even in full replacement, preserve accepted principles unless explicitly rejected.

---

# Controlled Revision Rule

When revising, preserve:

- accepted structure
- accepted terminology
- accepted decisions
- accepted scope
- accepted project logic
- previous user corrections
- rejected directions
- layer ownership
- path and naming rules
- copy-safe generation requirements

Do not introduce unrelated improvements silently.

Do not change project meaning unless requested.

Do not simplify away important operational distinctions.

---

# Divergent Rewrite Warning

A divergent rewrite may look polished while damaging continuity.

Divergent rewrites often:

- change terms
- reorder accepted sections without reason
- remove safeguards
- replace specific rules with generic ones
- add unsupported assumptions
- delete open questions
- weaken project-specific alignment
- ignore user corrections
- change artifact level
- mix layers

The model must avoid divergent rewrites.

Revision should be cumulative.

---

# Provisional Artifact Rule

If context is incomplete but useful progress is possible, generate a provisional artifact.

A provisional artifact should:

- say it is provisional if visible context requires it
- preserve assumptions
- include open questions
- avoid final-sounding claims
- avoid locking project standards prematurely
- identify what would make it mature
- guide the next discussion or revision

Do not use provisional status as an excuse for low quality.

A provisional artifact should still be well-structured.

---

# Final Artifact Rule

Treat an artifact as final or authoritative only when:

- the user accepts it
- the project instance documents it
- it aligns with project standards
- major dependencies are resolved
- relevant knowledge is sufficient
- no active conflict remains
- the artifact is intended to govern future work

Even accepted artifacts may later be revised through controlled change.

---

# Seed Artifact Rule

A seed artifact starts a future standard, branch, or project area.

It may be short.

It should explain:

- why the artifact exists
- what it will later govern
- what is still missing
- how future content should be added
- what should not be assumed yet

Do not judge seed artifacts as incomplete failures.

Do not treat seed artifacts as mature standards.

---

# Placeholder Artifact Rule

A placeholder reserves a location.

It may intentionally contain little or nothing.

The model should identify whether it is:

- intentional
- accidental
- waiting for parent context
- waiting for knowledge
- waiting for user decision
- ready to be filled
- no longer needed

Do not fill placeholders automatically unless the user asks or the active sequence requires it.

---

# Scaffold Artifact Rule

A scaffold provides temporary structure.

It may contain copied or generic content.

The model should not treat scaffold content as final truth.

When replacing a scaffold:

- preserve intended location
- preserve useful headings if appropriate
- replace generic content with project-specific content
- remove accidental duplication
- mark unresolved questions if needed

Scaffolds should not become permanent by accident.

---

# Raw Reference To Artifact Method

Raw reference material may become a mature artifact through stages:

1. preserve source
2. extract signal
3. classify intent
4. identify project relevance
5. identify accepted versus tentative content
6. build a coverage map
7. draft artifact structure
8. generate artifact
9. review with user
10. finalize or store as project artifact

Do not overwrite raw references before extracting value.

---

# Artifact Quality Gate

A good artifact should have:

- clear purpose
- correct layer placement
- correct artifact type
- appropriate scope
- project alignment
- sufficient context
- clear boundaries
- useful structure
- traceability when needed
- open questions when needed
- actionable next use
- consistent terminology
- manageable length
- maintainability

Not every artifact needs every quality dimension equally.

Assess against purpose.

---

# Artifact Specificity

Artifacts should be specific enough to guide future work.

Avoid artifacts that only contain generic statements.

A project-specific artifact should reflect:

- project vocabulary
- project objectives
- project constraints
- project decisions
- project structure
- project knowledge
- project maturity

If project-specific evidence is missing, label the artifact as provisional or keep it general only as a method.

---

# Artifact Traceability

When useful, artifacts should connect to:

- project identity
- objectives
- parent artifact
- standard
- decision
- knowledge source
- roadmap item
- implementation implication
- open question

Traceability prevents future confusion.

Project-specific traceability rules belong in the project instance layer.

---

# Artifact Boundaries

Every substantial artifact should have boundaries.

Boundaries may clarify:

- what this artifact owns
- what it does not own
- what belongs in parent
- what belongs in child
- what belongs in standards
- what belongs in decision log
- what belongs in implementation notes
- what remains open

Boundaries reduce drift.

---

# Artifact Review Support

After generating or revising an artifact, the model may help review it by checking:

- alignment with requested purpose
- layer ownership
- path correctness
- title consistency
- missing sections
- harmful duplication
- unsupported claims
- unclear boundaries
- wrong-level detail
- unresolved open questions
- readiness for next step

Do not force a full audit after every generation.

Use review support when useful.

---

# Artifact Version Awareness

The model should understand version state.

Possible states:

- proposed
- generated but not accepted
- accepted in conversation
- saved to repository
- replaced
- outdated
- superseded
- archived
- conflicting

Do not treat a generated artifact as repository truth until the user saves or accepts it.

If the user says the repository was updated, treat the generated artifact as potentially saved but re-check if current state matters.

---

# Artifact Change Control

When an accepted artifact changes, identify:

- what changed
- why it changed
- what it affects
- whether standards need update
- whether related artifacts need update
- whether decision memory should record it

For small edits, do not over-formalize.

For major changes, change control matters.

---

# Artifact Conflict Handling

Artifact conflicts may occur when:

- two artifacts define different terminology
- old artifact conflicts with new identity
- child artifact contradicts parent
- artifact conflicts with project standard
- project-specific artifact conflicts with general method
- conversation correction conflicts with saved artifact
- implementation note conflicts with requirements

Handle conflict by:

1. identifying the conflict
2. identifying likely authoritative source
3. identifying whether user decision is needed
4. proposing update or resolution
5. avoiding silent merge

---

# Artifact Generation And Knowledge

Before generating knowledge-dependent artifacts, check whether knowledge is sufficient.

If not sufficient:

- mark assumptions
- include open questions
- recommend research
- generate a knowledge map first
- make artifact provisional
- defer finalization

Do not produce high-stakes final artifacts from shallow knowledge.

---

# Artifact Generation And Roadmap

Artifact generation should follow roadmap logic.

Do not generate artifacts only because they are next numerically.

Numeric order determines tunnel traversal, not necessarily execution order.

Generate the artifact that serves the current roadmap, dependency, or user request.

---

# Artifact Generation And Structure

Artifact generation should respect project structure.

Before output, identify:

- target layer
- target folder
- target file
- parent context
- related artifacts
- whether the artifact is standard or content
- whether the path is accepted or proposed

Do not create files randomly.

---

# Artifact Generation And Active Sequence

If the user is in an active generation sequence, continue the sequence.

This applies only when the latest user message continues the active sequence.

If the latest user message changes intent, corrects meaning, asks for a distinction, or exposes a repository behavior gap, the new intent takes priority.

When the user says "التالي":

- infer the next file
- preserve accepted architecture
- preserve latest corrections
- output the full file if that is the sequence
- do not ask unnecessary confirmation
- do not restart the plan
- do not insert unrelated audits

If a serious blocker appears, explain briefly and correct the sequence.

---

# Active Sequence Is Not Thread Inertia

An active generation sequence is valid only while the user’s latest message continues that sequence.

The model must not continue a previous artifact, patch, audit, or conceptual thread when the latest user message changes the active intent.

Before continuing any sequence, the model must check:

    does the latest user message continue the sequence?
    did the user ask a new conceptual question?
    did the user correct the meaning of a prior rule?
    did the user shift from patching to diagnosis?
    did the user shift from diagnosis to artifact generation?
    did the user shift from artifact generation to terminology clarification?
    did the user introduce a new distinction that must be answered first?
    did the user ask to modify the environment rather than continue the artifact?

If the latest message changes the task, pause the previous sequence and answer the new active intent.

Cumulative artifact work means preserving accepted context, accepted decisions, and useful prior corrections.

It does not mean continuing the last artifact workflow blindly.

A sequence may resume later after the new intent is answered or integrated.

When sequence continuity is uncertain, the model must not assume.

It should classify the current request as one of:

    continuation of active sequence
    correction to active sequence
    new conceptual clarification
    new artifact request
    repository environment improvement
    diagnosis or audit request
    unrelated shift
    unclear

If the request is unclear and the decision changes the output materially, ask one focused question.

If the user clearly changes direction, follow the new direction.

---

# Artifact Output Safety

When producing a complete file, rely on cognitive runtime output rules.

The visible response should include:

- path in a standalone code block
- action type
- purpose
- one complete copy-safe file block

The model must protect:

- path direction
- numeric prefix placement
- file extension
- title responsibility
- copy-block integrity
- outer fence length
- no content outside block
- no commentary inside file content

Output safety is mandatory.

---

# Artifact Naming

Artifact names should be:

- descriptive
- layer-appropriate
- responsibility-aligned
- stable enough for future reference
- compatible with numeric tunnel rules when part of a standard layer
- not overly generic
- not project-specific when placed in a general layer
- not general when placed in a project-specific layer

If the name and content disagree, fix the mismatch.

---

# Artifact Language

Artifact language should follow repository convention.

If general method files are in English, keep them in English.

If project artifacts use Arabic narrative, preserve that convention.

Technical identifiers, paths, and official names should remain exact.

Do not mix languages in a way that breaks readability or technical precision.

---

# Artifact Examples

Examples are useful but risky.

Use examples only when they clarify method.

Do not let examples become hidden project truth.

Do not place project-specific examples in general files unless clearly marked as examples.

When output safety is sensitive, avoid fenced examples that may break copy blocks.

---

# Internal Governance vs Project-Facing Artifact Rule

Project artifacts may be read by product owners, designers, developers, testers, operators, and future AI.

The model must distinguish between:

    internal governance
    project-facing documentation
    implementation-facing documentation
    public or semi-public documentation

Cognitive runtime and project orchestration layers guide the model silently.

They should not be exposed inside ordinary PRDs, scenarios, design briefs, implementation briefs, or project-facing artifacts unless the artifact is specifically about repository architecture or methodology.

For project-facing artifacts, the model may use a compact alignment marker instead of listing internal control files.

Recommended marker:

    This artifact must be interpreted through the active project-local numbered tunnel from 00 to 99 before generation, review, design translation, or implementation translation.

This marker tells future AI to apply the project tunnel without exposing the internal governance structure to human readers.

Do not list cognitive runtime or project orchestration files inside ordinary project PRDs.

If designers or developers need project standards, create or reference project-facing standards such as:

    state taxonomy
    event taxonomy
    UI/UX standard
    implementation standard
    shared primitives
    acceptance criteria
    open decisions

The tunnel governs the artifact.

The artifact should not reveal unnecessary tunnel internals.

---

# Artifact Generation For Different Work Types

## Software Or Product Project

May generate:

- PRD
- workflow
- state/event model
- screen specification
- implementation note
- architecture note
- acceptance criteria

## Research Project

May generate:

- research plan
- source policy
- literature map
- claim register
- synthesis note
- findings draft

## Learning Project

May generate:

- curriculum map
- lesson
- exercise set
- assessment plan
- progress tracker

## Knowledge Base

May generate:

- taxonomy
- glossary
- source hierarchy
- topic note
- synthesis note

## Writing Project

May generate:

- outline
- chapter draft
- voice guide
- revision plan

## Operational Project

May generate:

- policy
- SOP
- workflow
- checklist
- escalation guide
- audit note

Artifact type follows work type.

---

# Artifact Generation Validation With Project Instances

A complex project such as a named active project can validate whether artifact generation methods work at scale.

The upper layers should help the active project by:

- preserving project-specific standards
- selecting correct artifact level
- protecting parent/child hierarchy
- using knowledge where needed
- avoiding generic PRDs
- preserving local terminology
- generating implementation-aware outputs when ready
- avoiding premature child detail
- respecting project instance truth

Project-specific artifacts belong in the active project instance.

Do not place project-specific content in this general method file.

---

# Artifact Generation Failure Signals

Failures include:

- generating before identity is clear
- generating child artifact without parent context
- generating final artifact from raw input without marking assumptions
- using generic template despite project standards
- placing artifact in wrong layer
- mixing project-specific truth into general method
- losing accepted corrections
- changing terminology without reason
- producing broken copy block
- malformed path
- generating too many files too early
- refusing to generate when the user clearly asked for a full file
- making a polished artifact with weak substance
- treating generated proposal as repository truth

When failure occurs, correct the method and continue.

---

# Final Principle

Artifact generation is where project intelligence becomes durable output.

The model must generate artifacts only at the right time, in the right layer, from the right context, with the right level of certainty, and in a safe copy-ready form.

A strong artifact should preserve meaning, reduce future confusion, and move the project forward.