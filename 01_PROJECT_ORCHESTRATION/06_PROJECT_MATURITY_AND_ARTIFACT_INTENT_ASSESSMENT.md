# PROJECT MATURITY AND ARTIFACT INTENT ASSESSMENT

# Purpose

This file defines how the model should assess project maturity, artifact maturity, artifact intent, readiness, gaps, and next actions.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific audit report.

It is not a static maturity snapshot.

It is not a project identity document.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define a general method for evaluating the condition and intent of project work without making shallow judgments from file names, folder existence, length, or old assumptions.

Maturity must be inferred dynamically from current evidence.

Artifact intent must be classified before judging quality.

---

# Core Principle

Do not judge a project artifact before understanding its intent.

A file may be short because it is weak.

A file may be short because it is intentionally a route marker.

A file may be empty because it is a placeholder.

A file may be duplicated because it is a scaffold awaiting replacement.

A file may be rough because it is raw user source.

A file may be long but still immature.

A file may be polished but wrong for the project.

The model must classify intent, inspect content when possible, compare with context, then assess maturity.

---

# What This File Owns

This file owns the project-orchestration method for maturity and artifact intent assessment.

It defines:

- how to classify artifact intent
- how to assess project maturity dynamically
- how to assess artifact maturity dynamically
- how to distinguish empty, raw, scaffold, mature, outdated, and conflicting files
- how to avoid judging by file existence alone
- how to avoid judging by file name alone
- how to identify readiness
- how to identify missing context
- how to recommend next actions
- how to avoid storing static status in general layers
- how to prevent old maturity conclusions from becoming stale assumptions

This file does not own:

- the current maturity of a specific project
- the current status of a specific artifact
- the current roadmap of a specific project
- project-specific audit findings
- project-specific decisions
- project-specific artifacts

Those belong in the project instance layer or current response when explicitly assessed.

---

# Dynamic Maturity Rule

Maturity is a live inference.

It must be based on current evidence.

Do not hardcode maturity statements in general orchestration files.

Do not repeat old maturity conclusions after the repository changes.

Do not say a file is empty, strong, weak, complete, or outdated unless current evidence supports it.

If inspection is unavailable and maturity matters, state the limitation.

If the user asks for a proposed assessment without current files, label it as proposed or limited.

---

# Artifact Intent Before Artifact Quality

Before judging quality, classify the artifact’s likely intent.

Artifact intent may be:

- authentic artifact
- mature draft
- raw reference
- user-provided source
- placeholder
- route marker
- empty structural node
- duplicated scaffold
- template seed
- example
- old version
- migration artifact
- outdated artifact
- conflicting artifact
- local standard
- project standard
- generated artifact awaiting review
- implementation note
- knowledge note
- decision record

The same file can have more than one intent.

Example:

A file may be both a route marker and a placeholder.

A file may be both a raw reference and user-provided source.

The model should classify enough to choose the next action.

---

# Artifact Intent Categories

## Authentic Artifact

A document that appears accepted, useful, and aligned with the project’s current standards.

It may still improve, but it is not merely raw or temporary.

## Mature Draft

A mostly developed artifact that can guide work but may need refinement, consistency checks, or project-specific alignment.

## Raw Reference

Material intentionally placed as source material for discussion, extraction, transformation, or later rewriting.

Do not judge it as final.

## User-Provided Source

Material supplied by the user that may be rough, partial, mixed, or exploratory.

It may contain valuable project truth even if not polished.

## Placeholder

A file reserved for future content.

It may intentionally contain little or nothing.

Do not treat it as failed documentation unless it was expected to be final.

## Route Marker

A file or folder that marks a future branch, child artifact, workflow, topic, or project area.

It indicates structure more than content.

## Empty Structural Node

An empty file or folder that exists to preserve a required place in the structure.

It should be recognized, not overinterpreted.

## Duplicated Scaffold

Copied or repeated content used temporarily to preserve structure until a unique artifact is written.

It may need replacement, but it is not automatically an error.

## Template Seed

A starting pattern intended to be adapted.

It should not be confused with project-specific truth until filled.

## Example

Illustrative content.

Examples are not automatically current project truth.

## Old Version

A previous version retained for history, migration, or comparison.

Do not treat it as current without evidence.

## Migration Artifact

A temporary artifact created during restructuring.

It may be useful but should not be treated as stable final content.

## Outdated Artifact

An artifact contradicted by newer repository content, newer conversation decisions, or accepted project changes.

## Conflicting Artifact

An artifact that disagrees with another active source and requires resolution.

## Local Standard

A standard that governs a specific branch, module, domain, section, or artifact family.

## Project Standard

A standard that governs the whole project instance.

## Generated Artifact Awaiting Review

An artifact produced by the model but not yet accepted or saved.

It should be treated as proposed until accepted.

---

# Project Maturity Dimensions

Project maturity is multi-dimensional.

Do not reduce it to a single number unless the user asks for a simple score.

Assess maturity across dimensions:

## Identity Maturity

Is the project identity clear?

Does the project have a stable purpose, audience, and boundaries?

## Objective Maturity

Are goals and outcomes clear?

Are objectives distinct from features and files?

## Standard Layer Maturity

Does the project have project-specific standards?

Are they usable, current, and followed?

## Structure Maturity

Is the project structure discoverable?

Do folders and files have clear responsibilities?

## Knowledge Maturity

Does the project capture required domain knowledge?

Are gaps visible?

## Artifact Maturity

Are key artifacts present and useful?

Are they raw, placeholders, mature drafts, or accepted artifacts?

## Decision Maturity

Are major decisions recorded?

Are open questions visible?

## Execution Maturity

Can the project support implementation, publication, research, learning, or delivery?

## Continuity Maturity

Can future work continue without repeated re-explanation?

## Consistency Maturity

Do files, terminology, standards, and artifacts agree?

---

# Artifact Maturity Dimensions

Artifact maturity may be assessed through:

## Purpose Clarity

Does the artifact explain why it exists?

## Scope Clarity

Does it define what it covers and what it does not cover?

## Layer Fit

Does it belong in the correct layer?

## Project Fit

Does it align with project identity and objectives?

## Content Completeness

Does it contain enough substance for its purpose?

## Structure Quality

Is it organized in a usable way?

## Traceability

Does it connect to parent standards, decisions, or artifacts when needed?

## Specificity

Is it specific enough to guide future work?

## Stability

Is it accepted, provisional, or still exploratory?

## Consistency

Does it agree with related artifacts?

## Actionability

Can it guide next work?

## Maintainability

Can it be updated without confusion?

---

# Do Not Judge By Length Alone

Long does not mean mature.

Short does not mean weak.

A mature reinforcement file may be short.

A raw source file may be long.

A route marker may intentionally be minimal.

A placeholder may be correct at its stage.

Assess by purpose and context.

---

# Do Not Judge By File Existence Alone

File existence only proves that a path or artifact exists.

It does not prove:

- maturity
- correctness
- acceptance
- completeness
- relevance
- currentness
- implementation readiness

A file may exist as a placeholder, scaffold, old version, or raw reference.

Use content and context to assess maturity.

---

# Do Not Judge By Folder Existence Alone

Folder existence only proves structure recognition.

It does not prove:

- content maturity
- project readiness
- artifact completeness
- implementation progress
- documentation quality

Use folder existence as structural evidence only.

---

# Do Not Judge By File Name Alone

File name suggests responsibility.

Content confirms actual responsibility.

A file named as a PRD may be raw.

A file named as notes may contain accepted decisions.

A file named as standard may be only a seed.

A file named as draft may be mature enough for current use.

Inspect content when the answer depends on it.

---

# Contextual Assessment

Maturity depends on project stage.

A seed-only project instance may be mature for bootstrap stage.

A complex project with many artifacts may still be immature if standards conflict.

A raw reference may be perfectly valid before reconstruction.

A placeholder may be acceptable if the project is intentionally mapping future branches.

The model must assess relative to intent and stage.

---

# Maturity Stages

Use maturity stages cautiously and dynamically.

## Not Started

No meaningful content exists for the target.

## Seeded

A place or initial standard exists, but content is minimal.

## Raw

Material exists but is unstructured or source-like.

## Emerging

Core ideas are present but not stable.

## Draft

The artifact has structure and usable content.

## Developed

The artifact is mostly complete for its current purpose.

## Mature

The artifact is aligned, specific, actionable, and integrated with related context.

## Accepted

The user or repository clearly treats the artifact as authoritative.

## Outdated

The artifact is superseded by newer context.

## Conflicting

The artifact disagrees with active sources and needs resolution.

Do not store these stages permanently unless creating a specific audit artifact in the project instance.

---

# Project Instance Stage Awareness

A project instance may be:

## Missing

No project instance layer exists.

## Minimal

Seed and reinforcement exist.

## Emerging

Identity, objectives, or standards are forming.

## Basic

Identity, objectives, and some structure exist.

## Structured

Standards, structure, and artifacts exist.

## Developed

Multiple artifacts and standards guide work.

## Mature

The project can support consistent future work with limited re-explanation.

## In Migration

Architecture or layers are being reorganized.

## Conflicting

Multiple active sources disagree.

Stage is dynamic.

Do not turn it into static truth in general files.

---


# Existing Project Intake And Adaptive Continuity

A project may arrive at any maturity level.

The model must not treat project orchestration as only a method for building new projects from zero.

Existing work may be:

- raw and scattered
- partially organized
- legacy documentation
- a code repository
- a research draft
- a course outline
- a business process
- a product specification
- a mature project with local standards
- a mixed project with strong sections and weak sections
- a project whose current method the user wants to preserve

Before recommending reconstruction, the model must classify the user’s intended relationship to the existing work:

## Preserve And Continue

The user wants to continue the existing method with minimal disruption.

The model should preserve terminology, structure, tone, and artifact strategy while correcting real errors and adding only necessary continuity.

## Repair In Place

The user wants fixes, clarification, cleanup, contradiction removal, or stronger wording without changing the project method.

The model should patch locally and avoid broad redesign.

## Upgrade Strategically

The user wants a quality leap, stronger standards, better architecture, professional documentation, or domain-aligned methodology.

The model should propose a staged upgrade path and explain what should change, why, and what should remain stable.

## Reorganize Or Migrate

The current structure blocks future work.

The model may propose a controlled migration, but must preserve source meaning, classify accepted truth, and avoid pretending the new structure already exists before it is accepted.

## Audit And Diagnose

The user wants understanding, weaknesses, contradictions, or readiness assessment.

The model should inspect before judging and separate evidence from recommendations.

## Translate To Execution

The user wants design, UI/UX, code, database, research protocol, operational procedure, or delivery output from existing documentation.

The model must verify that the source artifact contains enough domain, structural, and execution-relevant detail before translating.

---

# Improvement Without Forced Migration

The model should raise the quality of the user’s work, but must not force every old or weak project into the newest ideal method.

If the user wants a better professional standard, the model should guide the project toward stronger domain standards, clearer artifacts, and better execution readiness.

If the user wants only continuation under the old method, the model should work inside that method while still flagging genuine errors, contradictions, missing evidence, safety issues, or implementation blockers.

The model must distinguish:

- error that should be corrected
- weakness that should be recommended for improvement
- style difference that may be preserved
- project-local convention that should not be overwritten
- missing standard that may be proposed
- accepted project truth that must be protected

The goal is adaptive expert help, not rigid template enforcement.

---

# Assessment Source Priority

For maturity assessment, use:

1. current project instance files
2. project-specific numbered standards
3. target artifact content
4. related parent, child, sibling, or local context
5. current conversation and user corrections
6. project orchestration method
7. inference from structure
8. general knowledge

Do not rely on general knowledge when project evidence exists.

Do not rely on old memory when files changed.

---

# Artifact Role In Hierarchy

An artifact’s maturity depends on its role.

A parent artifact should define direction, boundaries, and child roadmap.

A child artifact should detail a focused branch.

A decision log should preserve decisions, not narrate everything.

A knowledge map should identify domains and gaps, not become the full research corpus.

A seed file should initiate standards, not contain every standard.

A reinforcement file should be compact, not replace full standards.

Assess maturity against role.

---

# Missing Artifact Does Not Always Mean Problem

An artifact may be missing because:

- the project is early
- the artifact is not needed
- the project type does not require it
- the user has not requested it
- it belongs to future phase
- a different artifact covers the need
- the project has not reached that level

Recommend missing artifacts only when they solve a real problem.

---

# Empty Artifact Does Not Always Mean Problem

An empty artifact may be:

- placeholder
- route marker
- empty structural node
- accidental empty file
- unfinished draft
- expected future artifact

Classify before judging.

If the empty artifact is part of a known planned branch, it may be fine.

If it was expected to guide work now, it is a gap.

---

# Duplicate Content Does Not Always Mean Problem

Duplicate or repeated content may be:

- harmful duplication
- intentional reinforcement
- copied scaffold
- migration residue
- temporary placeholder
- repeated standard for emphasis
- accidental copy

Classify before recommending deletion.

Useful reinforcement may remain.

Harmful duplication should be consolidated or relocated.

---

# Raw Artifact Handling

When an artifact is raw:

- preserve useful signal
- do not polish away meaning
- classify it as source or draft
- identify what can be extracted
- propose transformation path
- avoid treating it as final
- avoid deleting it before extracting value

Raw material can be valuable.

---

# Placeholder Handling

When an artifact is placeholder:

- identify what future artifact it marks
- determine whether it is needed now
- determine whether it should remain empty
- determine whether it needs a seed note
- determine whether it should be generated next
- avoid treating it as failure by default

A placeholder can be useful structure.

---

# Scaffold Handling

When an artifact is scaffold:

- identify whether content is copied from another artifact
- determine whether it is intentionally waiting for unique content
- decide whether to replace, keep temporarily, or mark as scaffold
- avoid assuming duplication is accidental without evidence
- avoid using scaffold content as project truth

Scaffolds should not become permanent by accident.

---

# Outdated Artifact Handling

When an artifact appears outdated:

- identify the newer source
- identify what changed
- identify affected files
- recommend update, archive, or replacement
- avoid merging old and new logic silently

Outdated does not always mean useless.

It may be useful for history or migration.

---

# Conflicting Artifact Handling

When artifacts conflict:

- identify the conflict
- identify likely authoritative source
- identify newer source
- identify layer ownership
- determine whether user decision is needed
- propose a resolution
- avoid silent compromise

Conflicts should become decisions or updates.

---

# Readiness Assessment

Readiness is different from maturity.

An artifact may be mature for discussion but not ready for implementation.

A project may be ready for planning but not ready for code.

Possible readiness types:

- ready for discussion
- ready for standardization
- ready for artifact generation
- ready for review
- ready for implementation planning
- ready for design
- ready for research
- ready for execution
- not ready because identity is unclear
- not ready because standards are missing
- not ready because conflicts exist

State readiness relative to the next action.

---

# Next Action From Maturity

Maturity assessment should lead to action.

Possible next actions:

- continue discussion
- ask focused question
- create seed file
- create identity file
- create structure index
- create knowledge map
- rewrite raw artifact
- replace scaffold
- fill placeholder
- resolve conflict
- update outdated artifact
- generate child artifact
- perform audit
- defer until parent standard is stable

Do not assess maturity without a purpose.

---

# Maturity Output Patterns

Use different output patterns depending on user intent.

## Quick Assessment

Use when the user asks if something is okay.

Include short conclusion and next action.

## Artifact Classification

Use when the artifact’s role is unclear.

Include intent, maturity, issue, next step.

## Project Health Assessment

Use when auditing a project.

Include major strengths, risks, gaps, and recommended fixes.

## Replacement Decision

Use when deciding whether to keep, rename, rewrite, merge, or delete.

Include rationale and safe action.

## File Generation

Use when the next action is to generate the missing or replacement artifact.

---

# Avoid Static Status Storage

This file must not store current findings such as:

- this project is Mode 4
- this section is strongest
- this file is empty
- this branch is next priority
- this repository is ready

Those findings belong in current responses or project instance audit files if the user wants persistent audit records.

The method is general.

The status is dynamic.

---

# Maturity And Repository Migration

During architecture migration, assess whether old files are:

- still useful
- misplaced
- obsolete
- raw source
- duplicated
- migrated
- needing rewrite
- needing relocation
- project-specific
- general method
- cognitive behavior

Do not delete useful standards.

Move or reframe them.

---

# Maturity And Layer Ownership

Layer ownership affects maturity.

A strong rule is immature if it is placed in the wrong layer.

A project-specific standard in a general layer creates pollution.

A general method in a project instance creates confusion.

A cognitive output rule in project content may be misplaced.

Assess whether the artifact is mature for its layer.

---

# Maturity And Project Instances

A real project instance may have large, complex, uneven maturity.

The upper layers should help assess it without weakening it.

Project-specific findings belong in the active project instance or current audit response, not in this general orchestration file.

Use the active project only as local evidence for whether the method works in practice.

Do not make the active project’s specific structure universal.

---

# Failure Signals

Maturity assessment failures include:

- judging by file existence
- judging by file length
- judging by folder existence
- judging by file name alone
- treating placeholders as failures
- treating raw references as final
- treating copied scaffolds as accepted truth
- deleting useful content because it is misplaced
- storing static current state in general method files
- repeating old maturity findings after repository update
- ignoring user explanation of artifact intent
- failing to classify before judging
- generating next files from immature parent context without warning
- treating a minimal project instance as broken

When failure occurs, correct the classification and reassess.

---

# Final Principle

Maturity is not appearance.

Maturity is alignment between intent, content, context, layer, and next action.

The model must understand what an artifact is trying to be before deciding whether it is good, weak, missing, misplaced, outdated, or ready.

A strong maturity assessment protects the project from both overbuilding and underbuilding.