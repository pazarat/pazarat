# PROJECT SHARED PRIMITIVES AND REUSABLE LOGIC METHOD

# Purpose

This file defines the general method for discovering, defining, organizing, reusing, and maintaining shared project primitives and reusable logic.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific primitives file.

It is not a static list of primitives for any current project.

It must not store fixed claims about any current project, artifact, module, file, folder, maturity, priority, or roadmap.

Its purpose is to help the model prevent repeated logic from being redefined inconsistently across many project artifacts.

Project orchestration defines the method.

The project instance layer stores actual project-specific primitives, shared rules, reusable logic, canonical definitions, and cross-artifact patterns.

---

# Core Principle

Repeated logic should become a shared primitive when it controls multiple artifacts.

A project primitive is a reusable unit of project meaning.

It may define a concept, state, event, actor, role, permission, policy, workflow pattern, artifact rule, naming rule, evidence rule, or implementation assumption that appears across the project.

The model must not rewrite the same shared idea differently in every artifact.

The model must detect repeated logic, extract it, stabilize it, and route it to the correct project-specific location when useful.

Shared primitives reduce contradiction.

Shared primitives improve continuity.

Shared primitives make large projects easier to reason about.

---

# What This File Owns

This file owns the general project-orchestration method for:

- detecting repeated project logic
- identifying primitive candidates
- distinguishing local detail from shared logic
- deciding when a primitive should be project-wide
- deciding when a primitive should be branch-local
- preventing duplication across artifacts
- preventing conflicting definitions
- routing primitives to the project instance layer
- using primitives during artifact generation
- updating primitives when project decisions change
- preserving reusable logic during repository migration
- avoiding over-abstraction
- avoiding project-specific pollution in general method files

This file does not own:

- actual primitives of a specific project
- actual role definitions of a specific project
- actual state taxonomy of a specific project
- actual event taxonomy of a specific project
- actual permission rules of a specific project
- actual UI primitives of a specific project
- actual implementation patterns of a specific project
- actual business logic of a specific project

Those belong in the project instance layer.

---

# Primitive Definition

A primitive is a stable reusable unit of project meaning.

A primitive can be referenced across multiple artifacts without being redefined from zero each time.

A primitive should answer:

- what the concept means
- where it applies
- what it does not mean
- what artifacts depend on it
- what decisions define it
- whether it is project-wide or local
- whether it is accepted, proposed, provisional, or outdated
- how future artifacts should use it

A primitive should be clear enough to reduce repeated explanation.

---

# Reusable Logic Definition

Reusable logic is a pattern that appears across multiple project artifacts.

Reusable logic may include:

- approval flow
- verification flow
- user lifecycle
- permission model
- notification behavior
- audit behavior
- state transition
- event emission
- source policy
- artifact naming rule
- decision handling
- data ownership rule
- visibility rule
- validation pattern
- exception pattern
- escalation rule
- parent-child documentation rule
- UI interaction pattern
- implementation boundary

Reusable logic should not be copied inconsistently across artifacts.

If it is repeated often and affects project behavior, it should be extracted into a primitive or shared rule.

---

# Primitive Types

The model should distinguish primitive types.

## Concept Primitive

Defines a key project concept.

Examples:

- user
- seller
- source
- claim
- lesson
- workflow
- request
- approval

## Actor Or Role Primitive

Defines a user type, actor, system role, organization role, or permission actor.

Examples:

- admin
- agent
- seller
- driver
- reviewer
- learner
- researcher
- editor

## State Primitive

Defines a status or condition that can recur across artifacts.

Examples:

- pending
- approved
- rejected
- suspended
- draft
- verified
- archived

## Event Primitive

Defines a trigger, occurrence, lifecycle event, or domain event.

Examples:

- user registered
- document submitted
- approval completed
- payment failed
- lesson completed
- source verified

## Permission Primitive

Defines who can see, change, approve, reject, delete, export, assign, or manage something.

## Workflow Primitive

Defines reusable flow logic.

Examples:

- submit → review → approve
- draft → publish → archive
- request → validate → fulfill
- learn → practice → assess

## Knowledge Primitive

Defines reusable knowledge standards.

Examples:

- evidence level
- source type
- confidence status
- glossary term
- accepted assumption
- disputed claim

## Documentation Primitive

Defines reusable artifact logic.

Examples:

- parent artifact
- child artifact
- local standard
- placeholder
- route marker
- scaffold
- source reference

## UI Primitive

Defines reusable interface behavior when the project has UI.

Examples:

- filter behavior
- table action pattern
- status badge meaning
- modal pattern
- empty state pattern

## Implementation Primitive

Defines reusable technical logic when implementation is relevant.

Examples:

- service boundary
- API ownership
- event bus behavior
- audit log rule
- permission middleware
- data validation rule

## Governance Primitive

Defines reusable decision, audit, change, or review logic.

Examples:

- change control
- decision status
- escalation path
- review requirement
- approval authority

---

# Primitive Candidate Signals

A primitive candidate may appear when:

- the same concept appears in multiple artifacts
- the same flow appears in multiple modules
- the same state appears in multiple branches
- the same event appears in multiple workflows
- the same role controls multiple actions
- the same approval logic is repeated
- the same permission logic appears in many places
- the same naming rule is repeated
- the same documentation rule appears in many artifacts
- the same knowledge rule controls multiple outputs
- the user repeats a principle across conversation turns
- artifacts define the same term differently
- child artifacts need a shared parent rule
- implementation notes repeat the same technical assumption

Repeated appearance is a signal.

Contradictory repetition is a stronger signal.

---

# When To Create A Shared Primitive

Create or recommend a shared primitive when:

- repeated logic affects multiple artifacts
- inconsistent definitions would create confusion
- future work depends on the concept
- many child artifacts inherit the same rule
- multiple modules need the same state or event
- a rule controls permissions, visibility, workflow, or data behavior
- a project-specific term needs stable meaning
- a pattern is likely to recur
- user corrections reveal a durable project rule
- a concept is central to project identity or execution

Do not create primitives only for decorative structure.

A primitive should solve a real continuity problem.

---

# When Not To Create A Shared Primitive

Do not create a primitive when:

- the logic appears only once
- the idea is still exploratory
- the concept is too vague
- the project is too early and the primitive would freeze thinking
- the detail belongs only in one local artifact
- the rule is temporary
- the pattern is not likely to repeat
- abstraction would make the artifact harder to understand
- the user only needs a quick answer
- the project does not need durable structure yet

Over-abstraction can be as harmful as duplication.

---

# Shared Versus Local Logic

The model must distinguish shared logic from local logic.

## Shared Logic

Belongs in project-level primitives, shared rules, taxonomy, knowledge map, or standards.

Shared logic affects multiple project areas.

## Local Logic

Belongs in a specific artifact, module, branch, workflow, lesson, research note, screen, or implementation note.

Local logic affects one focused area.

If local logic repeats across multiple areas, it may become shared.

Do not force every local detail into a project-wide primitive.

---

# Project-Wide Versus Branch-Local Primitive

A primitive may be project-wide or branch-local.

## Project-Wide Primitive

Applies across the whole project.

Examples:

- global role model
- universal state taxonomy
- project-wide event taxonomy
- source evidence policy
- artifact traceability rule
- shared permission model

## Branch-Local Primitive

Applies to one branch, module, domain, or artifact family.

Examples:

- admin dashboard table behavior
- user management verification step
- research source rating inside one research domain
- lesson assessment pattern inside one curriculum area

A branch-local primitive may later become project-wide if repeated elsewhere.

Do not prematurely promote local rules to project-wide rules.

---

# Primitive Placement

Project-specific primitives belong in the project instance layer.

Possible project-specific locations may include:

    06_PROJECT_PRIMITIVES_AND_SHARED_RULES.md
    02_PROJECT_DOMAIN_AND_STATE_TAXONOMY.md
    03_PROJECT_EVENT_TAXONOMY.md
    05_PROJECT_KNOWLEDGE_MAP.md
    07_PROJECT_DECISION_LOG.md
    local_branch/00_LOCAL_STANDARD.md

The exact file names depend on the project.

This orchestration file only defines the general method.

Do not store project-specific primitives in the general project orchestration layer.

---

# Relationship With Taxonomy

Taxonomy and primitives are related but not identical.

A taxonomy classifies terms.

A primitive defines reusable meaning and behavior.

A state taxonomy may list accepted states.

A state primitive may explain how a state is used, what transitions affect it, and what artifacts depend on it.

An event taxonomy may list accepted events.

An event primitive may explain trigger, actor, payload, effect, and downstream use.

If the project has strong taxonomies, primitives should align with them.

Do not create competing definitions.

---

# Relationship With Decision Memory

A primitive may originate from a decision.

A decision may define:

- accepted term
- accepted role
- accepted state
- accepted workflow
- accepted naming rule
- accepted visibility rule
- accepted source policy
- accepted implementation assumption

If a primitive is created from a decision, preserve the decision link when useful.

If a primitive changes, determine whether a decision update is needed.

Do not change shared primitives silently when they govern many artifacts.

---

# Relationship With Knowledge Map

Knowledge-heavy projects may need knowledge primitives.

Examples:

- source type
- evidence level
- confidence status
- claim category
- glossary term
- research method
- accepted assumption
- disputed question

If these primitives govern future research or artifacts, store them in the project knowledge map or shared rules.

Do not let knowledge primitives become generic claims without source discipline.

---

# Relationship With Artifact Generation

When generating an artifact, the model should check whether relevant shared primitives exist.

If they exist:

- apply them
- reference them when useful
- do not redefine them inconsistently
- do not duplicate full definitions unless needed
- preserve local specialization

If they do not exist but repeated logic appears:

- generate the artifact carefully
- mark repeated logic as a primitive candidate
- recommend adding a shared primitive if useful

Artifact generation should strengthen project consistency.

---

# Relationship With Parent And Child Artifacts

Parent artifacts often define primitive candidates.

Child artifacts often reveal missing primitives.

When generating children under a parent:

- identify inherited primitives
- identify child-specific local logic
- avoid redefining shared rules
- identify repeated child patterns
- recommend extracting shared primitives when multiple children need them

If many children repeat the same logic, the parent or shared rules file may need an update.

---

# Relationship With Workflows

Workflows often contain reusable logic.

A workflow primitive may define:

- trigger
- actor
- input
- output
- state transition
- event emitted
- approval step
- exception path
- audit requirement
- notification behavior
- permission requirement

If multiple workflows share the same sequence, extract the shared workflow primitive.

Do not duplicate workflow logic across artifacts with small contradictions.

---

# Relationship With UI Standards

UI projects may need UI primitives.

A UI primitive may define:

- table behavior
- filter behavior
- action menu behavior
- status badge meaning
- bulk action behavior
- modal confirmation pattern
- empty state
- loading state
- error state
- permission-gated action
- audit-visible action

UI primitives should belong in project-specific UI standards or shared rules.

Do not make UI primitives universal for projects that have no UI.

---

# Relationship With Implementation Standards

Implementation primitives may define recurring technical behavior.

Examples:

- audit log entry
- event emission
- API response shape
- validation behavior
- permission check
- service boundary
- repository pattern
- data ownership
- error handling
- background job behavior

Implementation primitives should belong in the project instance when implementation is relevant.

Do not generate implementation primitives before project intent and architecture are mature enough.

---

# Primitive Discovery Method

When inspecting a project, the model should discover primitives by looking for:

1. repeated concepts
2. repeated states
3. repeated events
4. repeated actors or roles
5. repeated workflows
6. repeated permissions
7. repeated validations
8. repeated UI patterns
9. repeated implementation assumptions
10. repeated documentation rules
11. repeated knowledge or evidence rules
12. repeated user corrections
13. conflicting definitions across artifacts
14. repeated parent-child inheritance patterns

Primitive discovery should be focused on the current task unless the user asks for a full audit.

---

# Primitive Extraction Method

When extracting a primitive:

1. identify repeated logic
2. collect examples from relevant artifacts or conversation
3. distinguish shared from local behavior
4. define the primitive clearly
5. define where it applies
6. define where it does not apply
7. identify dependencies
8. identify affected artifacts
9. classify status as proposed, accepted, provisional, outdated, or conflicting
10. recommend where to store it
11. update or recommend updating affected artifacts if needed

Do not extract primitives from weak evidence as final truth.

---

# Primitive Definition Pattern

A useful project-specific primitive may include:

- Primitive name
- Type
- Status
- Definition
- Applies to
- Does not apply to
- Source or rationale
- Related states
- Related events
- Related roles
- Related artifacts
- Open questions
- Update rules

This is a method pattern, not a mandatory universal format.

The project instance may define its own format.

---

# Primitive Status

A primitive may have a status.

## Proposed

Suggested by the model but not accepted.

## Provisional

Useful now but still incomplete.

## Accepted

Approved by the user or documented in project standards.

## Active

Currently governs future artifacts.

## Local

Applies to a branch or module only.

## Project-Wide

Applies across the project.

## Superseded

Replaced by a newer primitive.

## Conflicting

Multiple definitions exist and need resolution.

## Deprecated

Should no longer guide new work.

Use status to prevent weak or old definitions from becoming active truth.

---

# Avoid Primitive Duplication

Do not define the same primitive in many places with slightly different wording.

If the same concept appears repeatedly:

- identify the canonical definition
- reference it instead of redefining it
- update local artifacts if they diverge
- preserve local variations only when intentional
- document aliases when needed

Duplication becomes harmful when it creates inconsistent behavior.

---

# Avoid Primitive Overload

Do not convert every detail into a primitive.

Primitive overload creates:

- too much abstraction
- maintenance burden
- weak readability
- artificial complexity
- slow artifact generation
- confusion about what really matters

Only extract primitives that improve future consistency and reasoning.

---

# Primitive Conflict Handling

Primitive conflicts may occur when:

- two artifacts define the same term differently
- state names overlap with different meanings
- event names conflict
- local rules contradict project-wide rules
- old and new definitions coexist
- implementation assumes a different behavior than PRD
- UI behavior conflicts with permission logic
- conversation correction contradicts documented primitive

When conflicts appear:

1. identify the conflicting definitions
2. identify authoritative source if available
3. compare with latest conversation
4. classify whether one is outdated, local, alias, or wrong
5. ask a focused question if user decision is needed
6. update or recommend updating project-specific shared rules

Do not silently merge conflicting primitives.

---

# Primitive Versioning

Primitives may evolve.

When a primitive changes:

- identify what changed
- identify why it changed
- identify affected artifacts
- identify whether old references need update
- determine whether decision memory should record it
- avoid leaving old and new definitions active without explanation

Primitive changes can affect many project areas.

Treat them carefully.

---

# Primitive Use In Audits

When auditing a project, check whether:

- repeated concepts lack shared definitions
- repeated workflows diverge
- states are inconsistent
- events are inconsistent
- role permissions are unclear
- child artifacts repeat parent logic inconsistently
- project-specific primitives are stored in general layers
- local primitives conflict with project-wide standards
- implementation notes conflict with documented primitives
- placeholders need primitive guidance before expansion

Primitive audit should be scoped to the user’s request.

---

# Primitive Use In Roadmaps

A roadmap may include primitive work when repeated logic is blocking progress.

Examples:

- define user lifecycle primitive before user-management children
- define source evidence primitive before research synthesis
- define permission primitive before admin dashboard actions
- define event primitive before event-system implementation
- define learning progress primitive before curriculum modules

Primitive work should appear before dependent artifacts when it reduces risk.

---

# Primitive Use In Migration

During repository migration, preserve useful primitives.

If a useful primitive was in the wrong layer:

- do not delete it
- relocate it
- reframe it
- remove project-specific details from general method
- store project-specific details in the project instance
- update references if the canonical location changes

Migration should improve primitive clarity.

It should not erase accumulated project intelligence.

---

# Conversation As Primitive Source

The conversation may contain primitive candidates.

Signals include:

- repeated user correction
- repeated concept
- repeated rule
- accepted naming
- accepted structure
- accepted workflow
- accepted project principle
- rejected behavior
- agreed pattern for future artifacts

If a conversation primitive should persist, route it to the correct layer.

Project-specific primitive candidates belong in the project instance.

General method primitives belong in orchestration.

Model behavior primitives belong in cognitive runtime.

---

# Repository As Primitive Source

Repository artifacts may contain primitive candidates.

But not every repeated phrase is an accepted primitive.

Before extracting from repository:

- inspect context
- classify artifact maturity
- identify whether content is raw, scaffold, mature, or outdated
- compare related artifacts
- consider current conversation corrections
- avoid treating old duplicate scaffolds as active truth

Repository repetition may be useful signal or harmful duplication.

Classify first.

---

# Primitive And Placeholder Handling

Placeholders may point to future primitive needs.

A placeholder child artifact may indicate that the project will need shared definitions before detailed generation.

Do not fill placeholders with inconsistent local definitions.

If several placeholders depend on the same concept, define the primitive first or mark the primitive as needed.

---

# Primitive And Scaffold Handling

Scaffolds may contain generic logic.

Do not treat scaffold logic as accepted primitive.

When replacing scaffolds:

- extract useful structure
- discard generic filler
- apply accepted project primitives
- identify missing primitives
- avoid copying scaffold language into many artifacts

Scaffolds are starting frames.

They are not canonical definitions.

---

# Primitive And Raw Reference Handling

Raw references may contain strong primitive seeds.

When extracting from raw references:

- preserve original meaning
- distinguish accepted from tentative
- avoid over-polishing
- identify repeated terms
- identify hidden rules
- identify open questions
- propose primitives cautiously

Raw references can be valuable.

Do not erase them before extraction.

---

# Primitive Traceability

A primitive should be traceable when it governs important work.

Traceability may connect primitive to:

- source conversation
- decision
- parent artifact
- taxonomy
- event model
- knowledge map
- roadmap item
- implementation note
- affected child artifacts

Not every primitive needs heavy traceability.

Use enough traceability to prevent future confusion.

---

# Primitive Naming

Primitive names should be stable and clear.

A good primitive name should:

- reflect project terminology
- avoid ambiguity
- avoid accidental synonyms
- avoid mixing unrelated concepts
- align with taxonomy when available
- be reusable across artifacts
- be understandable without excessive explanation

If aliases exist, document them in the project instance when useful.

---

# Primitive Granularity

Primitive granularity should be balanced.

Too broad:

- becomes vague
- cannot guide artifacts
- hides important variations

Too narrow:

- duplicates local details
- creates too many primitives
- increases maintenance

A good primitive captures reusable meaning at the level where future artifacts benefit.

---

# Project Instance Shared Rules File

A project may need a shared primitives file.

Possible location:

    02_MY_PROJECT/project_folder/08_PROJECT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md

or:

    02_MY_PROJECT/project_folder/06_PROJECT_PRIMITIVES_AND_SHARED_RULES.md

Exact placement depends on the project’s local numbered tunnel.

If the project already has taxonomy, event, or state files, primitives may be distributed across those files rather than one file.

The project instance should decide.

---

# General Versus Project-Specific Primitive

The model must distinguish:

## General Primitive Method

Belongs here in project orchestration.

It defines how to discover and manage primitives.

## Project-Specific Primitive

Belongs in the project instance.

It defines an actual concept or rule for one project.

Do not store actual project roles, states, events, UI rules, permissions, or business logic inside this general method file.

---

# Project Instance Application

A complex project instance likely needs strong shared primitives because it has many modules and repeated logic.

Potential project-specific primitive areas may include:

- user lifecycle
- verification
- approval
- seller classification
- staff role
- admin action
- audit log
- notification
- permission gate
- profile ownership
- event emission
- dashboard table behavior
- document review
- account status
- suspension
- activation
- payout state
- order state
- shipment state
- return state

These are examples of primitive areas for the active project.

They are not universal project truth.

Actual project-specific primitives must be defined inside the active project folder after inspecting project-local standards and artifacts.

---

# Primitive Output Patterns

Depending on user intent, the model may output:

## Primitive Candidate Note

Use when a repeated pattern appears but is not yet accepted.

## Shared Logic Recommendation

Use when artifacts are starting to duplicate logic.

## Primitive Definition

Use when user asks to define a shared rule.

## Primitive Audit

Use when reviewing a project for repeated or conflicting logic.

## Project-Specific Shared Rules File

Use when the user asks to generate the project primitives file.

Place it in the project instance layer.

## Artifact Update Recommendation

Use when existing artifacts should be updated to reference the primitive.

---

# Minimal Question Rule

Ask only when a primitive decision affects future outputs.

Useful questions:

- Should this rule be project-wide or local to this branch?
- Is this term accepted as canonical?
- Should this repeated flow become a shared primitive?
- Does this local variation intentionally differ from the project-wide rule?

Do not ask if the primitive can remain proposed or provisional.

Do not block artifact generation unnecessarily.

---

# Failure Signals

Shared primitive failures include:

- repeated logic defined differently across artifacts
- child artifacts redefine parent concepts inconsistently
- local rule incorrectly promoted to project-wide rule
- project-wide rule ignored in local artifact
- general method file contains actual project primitives
- project-specific primitive hidden inside one child artifact
- scaffold content treated as canonical primitive
- old primitive remains active after project change
- aliases treated as separate concepts
- state or event definitions conflict
- permissions repeated without shared rule
- implementation notes contradict documented primitives
- over-abstracting every small detail into a primitive
- refusing to define primitives when repeated contradictions exist

When failure occurs, identify the repeated logic, classify the primitive candidate, and route it to the correct project-specific location.

---

# Final Principle

Shared primitives preserve project intelligence.

The model must detect reusable logic, define it at the right level, avoid inconsistent repetition, prevent over-abstraction, and store project-specific primitives inside the project instance.

A strong primitive method makes future artifacts more consistent, easier to generate, easier to audit, and easier to implement.