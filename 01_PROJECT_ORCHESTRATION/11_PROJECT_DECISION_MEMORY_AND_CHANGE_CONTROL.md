# PROJECT DECISION MEMORY AND CHANGE CONTROL

# Purpose

This file defines how the model should identify, preserve, organize, and apply project decisions and controlled changes.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific decision log.

It is not a static project status report.

It is not a change history for any current project.

It must not store fixed claims about any current project, artifact, folder, file, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for deciding when conversation input becomes a project decision, where decisions should be stored, how changes should be controlled, and how future work should respect accepted decisions.

The project orchestration layer defines the method.

The project instance layer stores actual project-specific decisions and change records.

---

# Core Principle

Projects drift when decisions are not remembered.

A decision may appear in conversation, repository files, artifact revisions, naming changes, architecture choices, roadmap changes, or user corrections.

The model must identify decisions that affect future work and route them to the correct memory location.

Not every idea is a decision.

Not every decision needs a formal log.

But decisions that govern future outputs must not disappear.

---

# What This File Owns

This file owns the project-orchestration method for decision memory and change control.

It defines:

- how to identify project decisions
- how to distinguish decisions from ideas, proposals, questions, and assumptions
- how to preserve user decisions
- how to handle accepted, rejected, deferred, and superseded decisions
- how to decide when a decision log is needed
- how to connect decisions to standards, artifacts, roadmap, and structure
- how to control changes to accepted project standards
- how to avoid silent drift
- how to update project artifacts safely
- how to preserve rationale when useful
- how to route actual decisions into the project instance layer

This file does not own:

- the decisions of a specific project
- a specific project’s decision log
- a specific project’s change history
- a specific project’s accepted roadmap
- a specific project’s artifact status
- a specific project’s current priorities
- a specific project’s implementation plan

Those belong in the project instance layer or current project response when explicitly assessed.

---

# Decision Definition

A decision is a choice that should guide future work.

A decision may define:

- project identity
- project objective
- project type
- project scope
- project non-scope
- architecture
- folder structure
- naming
- artifact hierarchy
- standard layer design
- knowledge policy
- roadmap sequence
- implementation approach
- accepted terminology
- rejected direction
- migration path
- output format
- review rule
- governance rule

A decision becomes important when future outputs should respect it.

---

# Non-Decision Definition

Not every statement is a decision.

The following may not be decisions yet:

- raw ideas
- brainstorming options
- questions
- examples
- tentative thoughts
- temporary notes
- emotional emphasis
- model proposals not accepted
- possible future directions
- assumptions not confirmed
- unverified interpretations

The model must not harden every raw input into a decision.

---

# Decision Signals

The model should detect decision signals.

Signals include:

- the user says yes, approved, اعتمد, تم, صحيح, نكمل
- the user applies a generated file to the repository
- the user says the repository was updated
- the user chooses one architecture over another
- the user rejects an alternative
- the user corrects a repeated behavior
- the user states a rule should be enforced
- the user continues a sequence based on the previous output
- the user asks to generate the next file in an accepted structure
- the user says a point is very important
- the user says not to repeat a mistake

Decision signals should be interpreted in context.

A casual “yes” may confirm a small action.

A repeated correction may define a durable rule.

---

# Decision Categories

Classify decisions by type.

## Identity Decision

Defines what the project is.

## Objective Decision

Defines what the project aims to achieve.

## Scope Decision

Defines what belongs or does not belong.

## Architecture Decision

Defines layer, folder, system, or structural approach.

## Method Decision

Defines how work should be performed.

## Standard Decision

Defines a project-specific governing rule.

## Artifact Decision

Defines what artifact should exist, where, and why.

## Naming Decision

Defines names, paths, prefixes, or terminology.

## Roadmap Decision

Defines sequence or priority.

## Knowledge Decision

Defines source policy, evidence hierarchy, terminology, or accepted domain understanding.

## Rejection Decision

Defines what should not be used or repeated.

## Migration Decision

Defines how old structure moves to new structure.

## Output Decision

Defines format, copy safety, language, or response requirements.

Different decisions belong in different places.

---

# Decision Ownership By Layer

A decision must be stored or applied in the correct layer.

## Cognitive Runtime Decision

Applies to model behavior across all work.

Examples:

- output must be copy-safe
- paths must appear in standalone blocks
- current conversation corrections must be preserved
- tunnel traversal must not be skipped
- evidence must not be overstated

These belong in cognitive runtime.

## Project Orchestration Decision

Applies to general project-building method.

Examples:

- raw ideas should not be forced into PRDs
- project standard layers should be tailored by project type
- project maturity must be inferred dynamically
- project-specific standards belong in the project instance
- artifact generation must respect readiness

These belong in project orchestration.

## Project Instance Decision

Applies to one specific project.

Examples:

- this project’s identity
- this project’s objectives
- this project’s taxonomy
- this project’s folder structure
- this project’s roadmap
- this project’s artifact naming
- this project’s product decisions
- this project’s research methodology

These belong in the project instance.

Do not place project-instance decisions in general layers.

---

# Decision Log

A decision log is a project-specific artifact that preserves important accepted decisions.

It may include:

- decision title
- date or sequence context
- decision type
- decision statement
- rationale
- alternatives considered
- affected files or artifacts
- status
- follow-up actions
- superseded decisions
- open questions

A decision log belongs in the project instance layer.

Possible path:

    02_MY_PROJECT/07_PROJECT_DECISION_LOG.md

or a project-specific equivalent.

The exact name depends on the project architecture.

---

# When A Decision Log Is Needed

Recommend a decision log when:

- decisions are accumulating
- architecture is changing
- standards are being accepted
- project scope is evolving
- artifact sequence matters
- multiple alternatives were considered
- future work depends on past choices
- repeated user corrections define durable rules
- the project has many contributors or tools
- project memory must survive across sessions
- conflicting artifacts need resolution
- migration is underway

Do not create a decision log for every small one-time task.

---

# Minimal Decision Memory

For early or small projects, decision memory may be lightweight.

It may be enough to preserve:

- accepted identity
- accepted objective
- accepted next step
- accepted architecture
- rejected options
- open questions

A minimal project instance may not need a full decision log immediately.

But if decisions begin to guide future work, a decision log becomes useful.

---

# Decision Status

A decision may have a status.

Possible statuses:

## Proposed

Suggested but not accepted.

## Accepted

Approved or clearly adopted by the user.

## Active

Currently governing future work.

## Deferred

Recognized but postponed.

## Rejected

Explicitly not chosen.

## Superseded

Replaced by a newer decision.

## Conflicting

Disagrees with another active source.

## Needs Review

May be outdated or unclear.

Use status to avoid treating old or proposed decisions as active truth.

---

# Accepted Decision Handling

When a decision is accepted:

- apply it immediately
- preserve it in conversation memory
- route it to the correct layer if it should persist
- use it in future outputs
- do not ask the user to reconfirm it unnecessarily
- do not silently contradict it later
- update affected artifacts if requested

If the decision affects future repository behavior, recommend or generate the relevant file update.

---

# Rejected Decision Handling

When the user rejects an option:

- do not repeat it as a recommendation
- preserve the rejection when it matters
- record it if the project needs decision memory
- explain only if useful
- avoid reintroducing the rejected option under a new name unless the user reopens it

Rejected directions can be as important as accepted directions.

They define boundaries.

---

# Deferred Decision Handling

A deferred decision is not rejected.

It is postponed.

When a decision is deferred:

- preserve it as future consideration
- do not let it block unrelated progress
- do not treat it as accepted
- do not forget it if it affects future planning
- place it in roadmap or decision log when appropriate

Deferral protects momentum without losing future options.

---

# Superseded Decision Handling

A decision becomes superseded when a newer accepted decision replaces it.

When superseding:

- identify the old decision
- identify the new decision
- identify what changed
- identify affected files or artifacts
- avoid mixing old and new logic
- update project instance if requested

Old decisions may remain useful history but should not govern current work.

---

# Decision Rationale

Some decisions need rationale.

Record rationale when:

- the decision affects many future outputs
- alternatives were plausible
- the decision prevents future confusion
- the decision may be challenged later
- the decision resolves conflict
- the decision changes project architecture
- the decision affects standards or implementation

Do not over-document trivial decisions.

---

# Decision Impact

Important decisions should identify impact.

Impact may affect:

- project standards
- project identity
- project scope
- folder structure
- artifacts
- roadmap
- knowledge map
- implementation notes
- naming
- terminology
- future generation rules
- migration plan

If impact is broad, change control is needed.

---

# Change Control Definition

Change control is the method for modifying accepted project structures, standards, artifacts, or decisions without causing drift.

A change may affect:

- identity
- objectives
- scope
- standards
- folder structure
- artifact hierarchy
- roadmap
- terminology
- taxonomies
- knowledge policy
- implementation assumptions
- output rules
- project-specific conventions

Change control does not mean bureaucracy.

It means deliberate updates.

---

# When Change Control Is Needed

Use change control when:

- accepted standards are modified
- project identity changes
- objectives change
- folder architecture changes
- artifact hierarchy changes
- naming conventions change
- project-specific taxonomy changes
- roadmap sequence changes
- old artifacts must be updated
- a conflict is resolved
- a project-specific rule moves layers
- migration is happening
- an accepted artifact is being replaced

For small wording fixes, lightweight change handling is enough.

---

# Lightweight Change Handling

Use lightweight handling for:

- typos
- formatting corrections
- path display fixes
- small wording clarification
- copy-block correction
- minor section improvement
- title alignment
- grammar cleanup

Lightweight changes may not need a formal decision log entry.

But they should still preserve accepted meaning.

---

# Controlled Change Handling

Use controlled handling for:

- changing identity
- changing objectives
- moving rules across layers
- changing file architecture
- replacing a mature artifact
- changing project-specific standards
- resolving conflicting artifacts
- creating a new standard layer
- changing roadmap sequence
- changing domain taxonomy

Controlled change should identify:

- what changes
- why
- affected artifacts
- whether old content is replaced, moved, or archived
- whether decision log update is needed

---

# Change Request Interpretation

The user may request a change directly or indirectly.

Direct signals:

- update this
- replace this
- rename this
- move this
- delete this
- adjust this
- regenerate this

Indirect signals:

- this caused confusion
- there is a conflict
- this belongs in another layer
- this should be general
- this should be project-specific
- this no longer fits
- the repository was updated

The model should interpret the change request at the correct layer.

---

# Change Scope

Before making a change, determine scope.

Possible scopes:

- wording only
- formatting only
- file path
- file name
- section
- full file
- layer ownership
- folder architecture
- project standard
- project artifact
- project roadmap
- project identity
- whole repository architecture

The response should match change scope.

Do not regenerate a whole file for a typo unless requested.

Do not patch a file when the architecture changed completely.

---

# Change Safety

A safe change preserves what should remain stable.

Before changing, identify:

- accepted decisions to preserve
- useful existing rules
- rejected directions to avoid
- affected layer
- affected project instance
- related artifacts
- migration implications
- whether the change introduces contradiction
- whether output must be full replacement or patch

Do not fix one issue by creating another.

---

# Change Traceability

Changes should be traceable when they matter.

Traceability may include:

- source correction
- reason for change
- affected file
- affected layer
- affected artifact
- old interpretation
- new interpretation
- unresolved follow-up

Not all changes need formal traceability.

But major project changes should not be invisible.

---

# Decision From Correction

A user correction may become a decision.

Examples:

- "Do not generate outside the copy block."
- "Use numbered folders as the tunnel."
- "Do not put project-specific standards in orchestration."
- "the active project should be a project instance test, not the general method."
- "Paths must appear in standalone blocks."
- "Preserve useful existing standards instead of rebuilding from zero."

These are not casual corrections.

They define future behavior and should be placed in the correct layer.

---

# Decision From Repetition

Repeated user emphasis may reveal a decision or principle.

When the user repeats a point many times, infer that it may be high priority.

Do not dismiss repetition as redundancy.

Repeated concerns may indicate:

- a fragile process
- previous model failure
- essential project principle
- standard that must be reinforced
- future risk

If repeated enough and clearly directional, preserve it.

---

# Decision From Repository Update

When the user says the repository was updated, this may mean a prior generated file or decision was accepted.

The model should treat this as a signal, not automatic proof of exact content.

If current repository access is available, inspect when needed.

If not available, proceed from the accepted conversation direction and avoid claiming current file content.

---

# Decision From Generated File Acceptance

If the user continues after a generated file without rejecting it, the file may be treated as provisionally accepted for the active sequence.

If the user says it was added to the repository, it may be treated as likely accepted.

Still, if exact current content matters, verify.

Do not assume every generated proposal became current truth unless the user indicates acceptance or repository evidence confirms it.

---

# Decision And Roadmap

Roadmap decisions should be preserved when they determine sequence.

Examples:

- generate cognitive runtime first
- then project orchestration
- then project instance seed
- then test with the active project
- do not return to project artifacts before upper layers are stable
- continue file generation when user says next

Roadmap decisions may belong in a project instance roadmap or decision log if persistent.

---

# Decision And Standards

Standard decisions are especially important.

When a standard is accepted:

- apply it consistently
- preserve it in the correct standard file
- identify affected artifacts if needed
- avoid changing it casually
- update it deliberately when user decides

Standards govern future generation.

They require stronger change control than ordinary notes.

---

# Decision And Artifact Revision

When revising an artifact based on a decision:

- preserve accepted baseline
- apply only relevant changes
- identify affected sections
- do not introduce unrelated changes
- update related standards if decision affects them
- record change if significant

Artifact revision should reflect decisions, not overwrite them.

---

# Decision And Knowledge

Knowledge decisions may include:

- accepted source hierarchy
- accepted terminology
- accepted domain definition
- accepted assumption
- accepted research method
- accepted evidence policy
- rejected source type

These belong in the project instance if project-specific.

Do not treat tentative knowledge as accepted decision.

---

# Decision And Layer Ownership

Layer decisions are critical during architecture redesign.

If a rule belongs to another layer:

- preserve the rule
- move or reframe it
- do not delete it
- do not leave it polluting the wrong layer
- update related files if necessary

Layer ownership decisions affect the whole repository.

---

# Decision And Migration

During migration, decisions may define:

- new folder names
- old-to-new mapping
- file renaming
- file relocation
- rule extraction
- rule preservation
- project instance placement
- legacy compatibility
- migration order

Migration decisions should be tracked enough to avoid confusion.

---

# Conflict Resolution As Decision

When a conflict is resolved, the resolution is a decision.

Record or preserve:

- conflict description
- chosen source of truth
- why it was chosen
- affected files
- old content handling
- new rule or standard
- remaining open issues

Do not resolve conflicts silently if they affect future work.

---

# Decision Log Entry Pattern

A project-specific decision log entry may include:

- Decision ID or sequence number
- Date or conversation marker
- Title
- Type
- Status
- Decision
- Rationale
- Alternatives
- Affected files
- Follow-up actions
- Supersedes
- Open questions

This is an example pattern.

The actual project decision log format belongs in the project instance.

Do not force this exact format on every project.

---

# Change Record Pattern

A project-specific change record may include:

- Change title
- Change type
- Reason
- Previous state
- New state
- Affected layer
- Affected files
- Migration action
- Validation needed
- Follow-up

This is a method example, not a mandatory universal file format.

---

# Minimal Decision Entry

For lightweight projects, a minimal entry may include only:

- decision
- reason
- status
- affected area

Do not over-formalize when simple memory is enough.

---

# Decision Granularity

Decisions should be granular enough to be useful.

Too large:

- hides important details
- makes future changes unclear

Too small:

- creates noise
- increases maintenance
- slows work

Record decisions that influence future outputs.

Do not record every sentence.

---

# Decision Review

Some decisions should be reviewed later.

Review may be needed when:

- project scope changes
- new evidence appears
- old assumptions become invalid
- implementation begins
- project type changes
- user priorities change
- external facts change
- a decision creates conflict
- artifacts no longer align

A decision log may include review status.

---

# Decision Expiry

Some decisions may expire.

Examples:

- temporary migration rule
- provisional naming
- current source policy pending research
- roadmap order for this phase only
- assumption made due to missing information

Mark temporary decisions clearly when needed.

Do not let temporary decisions become permanent accidentally.

---

# Decision Memory Without Repository

If no repository exists, the model can still preserve decisions within the current conversation.

It should not claim persistent repository memory.

If decisions are becoming important, suggest creating a project instance or decision log when useful.

---

# Decision Memory With Repository

If a repository exists, important decisions should be routed to the correct persistent location.

The model should identify whether the decision belongs in:

- cognitive runtime
- project orchestration
- project instance
- project decision log
- project roadmap
- project standard
- project artifact
- project knowledge map

Do not store all decisions in one place.

---

# Decision Memory And Active Sequence

In an active file-generation sequence, decisions include:

- accepted next file order
- accepted file paths
- accepted architecture
- accepted output formatting rules
- accepted layer ownership
- accepted correction patterns

When the user says "التالي", continue according to these decisions.

Do not ask unnecessary confirmation.

---

# Avoid Decision Drift

Decision drift occurs when later outputs slowly contradict accepted decisions.

Causes:

- forgetting prior corrections
- regenerating from generic template
- using old architecture
- ignoring accepted path rules
- mixing project-specific and general layers
- changing terminology silently
- treating proposal as accepted
- treating accepted decision as optional

The model must actively prevent decision drift.

---

# Avoid Decision Overload

Do not turn every detail into a formal decision.

Decision overload creates maintenance burden.

Only formalize decisions that:

- guide future work
- resolve ambiguity
- control standards
- affect multiple artifacts
- define architecture
- preserve important user intent
- prevent repeated mistakes
- influence roadmap or implementation

---

# Decision Output Patterns

Use different output patterns depending on intent.

## Quick Decision Recognition

Use when user confirms a direction.

Briefly acknowledge and proceed.

## Decision Summary

Use when multiple decisions were made.

List accepted decisions and next action.

## Decision Log Proposal

Use when decisions should persist.

Suggest adding a decision log entry.

## Change Control Note

Use when a major accepted artifact or standard changes.

Explain what changes and affected files.

## Decision Log File

Use when the user asks to generate the project-specific decision log.

Place it in the project instance layer.

---

# Failure Signals

Decision memory and change control failures include:

- losing accepted decisions
- treating proposals as accepted
- treating accepted decisions as optional
- forcing user to repeat decisions
- storing project-specific decisions in general layers
- changing standards silently
- overwriting accepted artifacts without change awareness
- failing to record major architecture changes
- treating temporary decisions as permanent
- creating excessive decision logs for trivial work
- not preserving rejected options
- silently resolving conflicts
- ignoring decisions implied by repository updates
- breaking active sequence after a decision was made

When failure occurs, restore the decision context and correct the output.

---

# Final Principle

Decision memory protects project continuity.

Change control protects project integrity.

The model must know when a user statement becomes a decision, where that decision belongs, how it affects future work, and how to change accepted project structures without drift.

A project that remembers its decisions becomes easier to trust, extend, and execute.