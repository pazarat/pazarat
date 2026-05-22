# PROJECT REFERENCING NAMING AND TRACEABILITY METHOD

# Purpose

This file defines the general method for naming, referencing, linking, and tracing project artifacts, standards, folders, decisions, parent-child relationships, and generated outputs.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific naming standard.

It is not a static map of any current project.

It must not store fixed claims about any current project, artifact, folder, file, maturity, priority, or roadmap.

Its purpose is to help the model produce clear, stable, navigable, and traceable project outputs without relying on fragile memory, ambiguous names, malformed paths, or undocumented relationships.

Project orchestration defines the general method.

The project instance layer stores the actual project-specific naming, referencing, traceability rules, and canonical artifact paths.

---

# Core Principle

A project becomes easier to understand when every artifact can be referenced clearly.

The model must know when to use:

- a full path
- a short reference
- an artifact title
- an artifact code
- a parent reference
- a child reference
- a branch reference
- a decision reference
- a local context reference
- a proposed path
- an existing documented path

References must reduce ambiguity.

They must not create false certainty.

A reference is useful only when it points to the right layer, the right artifact, and the right level of authority.

---

# What This File Owns

This file owns the general project-orchestration method for:

- file and folder referencing
- artifact naming
- canonical path usage
- short reference usage
- parent-child traceability
- local branch traceability
- decision traceability
- knowledge traceability
- roadmap traceability
- generated artifact traceability
- proposed versus existing path distinction
- naming conflict detection
- reference update discipline
- avoiding stale references after migration
- avoiding path-direction corruption in Arabic contexts

This file does not own:

- actual project-specific file names
- actual project-specific folder names
- actual project-specific artifact codes
- actual project-specific PRD conventions
- actual project-specific branch maps
- actual project-specific decision IDs
- actual current repository state

Those belong in the project instance layer or current project response when explicitly inspected.

---

# Reference Types

The model should distinguish reference types.

## Full Path Reference

A full path identifies the exact location of a file or folder.

Use when precision matters.

Examples of when full path is useful:

- file generation
- file replacement
- repository migration
- audit
- conflict resolution
- renaming
- path-sensitive instructions
- user copy action
- traceability from one artifact to another

Full paths must be shown in standalone code blocks when exact copying matters.

## Short Reference

A short reference names the artifact without full path.

Use when the path is already clear or when readability matters.

Examples:

- "User Management PRD"
- "active project structure index"
- "project identity file"
- "decision log"
- "state taxonomy"

Short references are useful in discussion but should not replace full paths when exact file operation is needed.

## Artifact Title

The human-readable title inside the artifact.

The title should match responsibility.

If file name and title conflict, identify the mismatch.

## Artifact Code

A compact project-specific code or label used for traceability.

Examples may include module codes, branch codes, dashboard codes, scenario codes, or decision IDs.

Artifact codes belong in the project instance if project-specific.

## Parent Reference

A reference to the artifact that governs or frames another artifact.

Use when generating child artifacts, workflows, screen documents, research subnotes, lessons, or implementation notes.

## Child Reference

A reference to a focused artifact under a parent.

Use when mapping coverage, roadmap, scenario expansion, or local detail.

## Branch Reference

A reference to a project area or folder.

Use when discussing a module, domain, dashboard, product surface, research area, or knowledge branch.

## Decision Reference

A reference to an accepted decision that governs future work.

Use when a change, naming choice, architecture choice, or artifact sequence must remain traceable.

## Knowledge Reference

A reference to domain knowledge, source policy, evidence hierarchy, glossary, or research note.

Use when artifacts depend on knowledge.

## Proposed Reference

A path, name, code, or relationship suggested by the model but not yet accepted or saved.

Must be labeled as proposed.

---

# Full Path Rule

Use a full path when ambiguity or execution risk exists.

A full path is required or strongly preferred when:

- generating a complete file
- replacing a file
- renaming a file
- moving a file
- updating references
- auditing repository structure
- diagnosing path conflicts
- distinguishing old and new architecture
- pointing to a target artifact
- telling the user where to save content
- comparing actual structure with expected structure

The model must not use a vague short reference when the user needs to act on a file.

---

# Full Path Display Safety

When exact paths matter, display the path in a standalone code block.

Do not place exact paths inline inside Arabic text when direction may distort the path.

Do not attach Arabic punctuation directly to the path.

Before outputting a path, verify:

- folder order
- numeric prefix
- file name
- extension
- extension at the end
- no duplicated extension
- no misplaced suffix
- no old architecture path
- correct project instance layer
- correct discovered project folder if relevant

Path display errors are project safety defects.

---

# Short Reference Rule

Use a short reference when:

- the target is already clear
- the user does not need to copy the path
- the conversation is conceptual
- the full path would reduce readability
- the artifact is being discussed broadly
- the current section already established the path

A short reference must not hide ambiguity.

If there are multiple artifacts with similar names, use full path or add context.

---

# Existing Versus Proposed Reference

The model must distinguish whether a referenced path or artifact exists, is proposed, or is unknown.

## Existing

Use only when current evidence confirms the file or folder exists.

## Proposed

Use when the model recommends creating, renaming, or moving something.

## Expected

Use when the architecture expects something, but current existence is not verified.

## Missing

Use when inspection indicates it is absent.

## Unknown

Use when current repository state is unavailable.

Do not present a proposed path as existing.

Do not present an expected path as verified.

---

# Canonical Path Rule

A canonical path is the accepted current location of an artifact.

Canonical paths should be used in:

- generated file headers
- structure indexes
- migration notes
- artifact references
- decision impact notes
- parent-child maps
- audit findings

If old paths remain after migration, update them or classify them as legacy references.

Do not keep using old paths casually after the project adopts a new structure.

---

# Legacy Path Handling

Legacy paths may appear during migration.

Examples of legacy architecture patterns may include older cognitive runtime folders, old active project folders, or previous project root names.

When a legacy path appears:

1. determine whether it is historical, still active, or stale
2. do not automatically treat it as current
3. replace it in project-specific files if the project has migrated
4. preserve it only if it is intentionally documented as legacy
5. avoid allowing legacy paths to confuse tunnel traversal

Legacy compatibility belongs in general method only when clearly framed as legacy behavior.

Project-specific files should normally use current canonical project paths.

---

# Naming Consistency Rule

Names should be stable, descriptive, and responsibility-aligned.

A good artifact or folder name should:

- identify its purpose
- match its content
- match the project’s naming style
- avoid accidental suffixes
- avoid duplicated words
- avoid unclear abbreviations unless project-approved
- avoid changing case inconsistently when case matters
- avoid misleading maturity claims
- avoid generic names that collide with other artifacts

If a name and content disagree, identify the mismatch before generating or updating.

---

# Numeric Prefix Rule

Numbered files and folders are special.

A numeric prefix usually indicates tunnel order, local standards, sequence, or structured artifact order.

The model must treat numeric prefixes carefully.

Rules:

- numeric prefix belongs before the file or folder name
- numeric prefix must not appear after the extension
- numeric prefix determines tunnel traversal order when used in root numbered files
- numeric prefix does not automatically mean execution priority
- missing numbers do not break the tunnel
- newly added numbered files may become part of the local tunnel
- content confirms purpose

Do not reorder numbered files without a reason.

Do not treat every numbered file as mature.

---

# Artifact Code Rule

A project may use artifact codes.

Artifact codes can help trace:

- branches
- modules
- dashboards
- scenarios
- PRDs
- workflows
- screens
- decisions
- roadmap items
- implementation notes

The project instance should define project-specific artifact code conventions if needed.

General examples:

- dashboard code
- module code
- scenario code
- decision code
- roadmap item code
- research note code
- lesson code

Artifact codes should improve traceability.

They should not become decorative complexity.

---

# Parent-Child Traceability

Parent-child relationships must be explicit when they affect understanding.

A child artifact should be traceable to its parent.

A parent artifact may list or describe its children.

A child artifact should not redefine the parent’s purpose unless the parent is outdated or wrong.

When generating a child artifact, identify:

- parent artifact
- inherited scope
- local scope
- sibling context when relevant
- child-specific decisions
- open questions
- affected shared primitives
- related workflow or implementation implications

Do not create orphan child artifacts.

---

# Branch Traceability

A branch is a project area such as a dashboard, module, research domain, knowledge area, chapter, workflow family, or implementation surface.

When referencing a branch, clarify:

- branch name
- branch role
- parent branch if relevant
- local standards if present
- main artifacts
- child artifacts
- whether branch content is mature, raw, placeholder, or mixed if assessed

Branch traceability helps dynamic discovery.

Do not treat branch existence as maturity.

---

# Decision Traceability

Important project decisions should be traceable.

A decision reference should clarify:

- what was decided
- whether it is accepted, proposed, deferred, rejected, superseded, or conflicting
- what files or artifacts it affects
- whether it changes naming, structure, scope, roadmap, or standards
- whether related references must be updated

If a decision changes a path or name, update references.

Do not let old names and new names coexist without explanation.

---

# Knowledge Traceability

Knowledge-dependent artifacts should trace to relevant knowledge context.

This may include:

- source policy
- knowledge map
- glossary
- domain taxonomy
- evidence hierarchy
- research note
- accepted assumption
- open question
- high-stakes caution

If project output depends on knowledge that is missing or uncertain, mark it.

Do not treat general knowledge as accepted project knowledge unless the project accepts it.

---

# Roadmap Traceability

Roadmap items should trace to objectives, standards, decisions, or dependencies.

A roadmap reference should clarify:

- what stage or item it belongs to
- what it depends on
- what it unlocks
- whether it is active, deferred, proposed, or completed
- what artifact or decision it affects

Do not confuse numeric tunnel order with roadmap order.

---

# Generated Artifact Traceability

When generating a new artifact, the model should know:

- target path
- artifact type
- parent artifact
- relevant standards
- relevant decisions
- relevant knowledge
- intended maturity
- assumptions
- open questions
- whether the artifact is proposed or accepted

Generated content is proposed until accepted or saved by the user.

If the user says the repository was updated, treat it as likely saved but verify if exact current content matters.

---

# Reference Update Discipline

When a file or folder is renamed or moved, update references.

Reference updates may be needed in:

- structure index
- parent artifact
- child artifact
- decision log
- roadmap
- knowledge map
- local standards
- implementation notes
- README-like files
- generated examples
- old migration notes

Do not rename a file and leave the structure map pointing to the old name.

Do not update references outside the relevant project scope unless necessary.

---

# Naming Conflict Detection

A naming conflict may exist when:

- two files have nearly identical names
- file name and title disagree
- path says one thing and content says another
- old and new names coexist
- case differences are meaningful but inconsistent
- a plural and singular form are both used without reason
- a typo appears in canonical path
- numeric prefix is misplaced
- extension is duplicated or malformed
- project-specific terminology conflicts with general terminology

When a conflict matters, classify it and recommend correction.

---

# Path Migration Discipline

During architecture migration, the model must distinguish:

- old path
- new path
- canonical path
- migration target
- archived path
- stale reference
- proposed path

A migration should include reference replacement when needed.

Do not claim migration is complete if old project-specific paths still remain in active project files.

---

# Traceability In Audits

When auditing project structure, include traceability findings when useful.

Check:

- whether root standards reference current project paths
- whether structure index matches actual files
- whether parent artifacts list current children
- whether child artifacts reference correct parent
- whether old paths remain after migration
- whether decisions affecting names are recorded
- whether project terminology is consistent
- whether placeholders are clearly classified
- whether local standards are discoverable

Do not perform full traceability audit for every small question.

Use depth appropriate to intent.

---

# Traceability In File Generation

When generating complete files, visible response should include:

- path
- action type
- purpose
- complete file content

Inside the generated file, include traceability sections only if useful for that artifact type.

Do not overload every file with traceability metadata.

For standards and indexes, traceability is often important.

For small content artifacts, minimal traceability may be enough.

---

# Reference Granularity

Use the right amount of reference detail.

Too little reference:

- creates ambiguity
- makes updates risky
- loses parent context
- hides affected files

Too much reference:

- creates noise
- makes files hard to read
- increases maintenance
- overfits to current structure

Reference detail should match artifact importance and change risk.

---

# Portable Project Files

Project-specific files should be locally understandable.

They should not need to repeat exact paths to upper cognitive or orchestration layers.

The upper layers route the model into the project.

The project files should define local project truth.

Avoid polluting project files with upper-layer paths unless the project itself is about those layers.

This makes project folders portable.

---

# Local Canonical Names

A project may define local canonical names.

Examples:

- canonical project name
- canonical module name
- canonical dashboard name
- canonical role name
- canonical state name
- canonical event name
- canonical artifact family name

Use local canonical names once accepted.

If a file uses a non-canonical name, classify whether it is:

- typo
- legacy
- alias
- placeholder
- local variant
- old version
- conflict

Then recommend update if needed.

---

# Alias Handling

Some projects may need aliases.

An alias may be useful when:

- user-facing name differs from internal name
- old terminology still appears in legacy files
- Arabic and English names coexist
- business term differs from technical term
- short name differs from canonical name

Aliases should be documented in the project instance if they matter.

Do not silently treat aliases as separate concepts.

---

# Multi-Language Naming

Projects may use Arabic, English, or mixed naming.

Rules:

- preserve technical identifiers exactly
- preserve official project names
- avoid translating file names unless accepted
- avoid Arabic/English direction confusion in paths
- define glossary or aliases when terminology matters
- use clear Arabic explanation around exact English paths when needed

Exact paths should remain in standalone code blocks.

---

# Title And File Name Alignment

The file title should match the file responsibility.

Examples of mismatch:

- file name says identity, title says roadmap
- file name says PRD, content is raw notes
- file name says standard, content is implementation detail
- file name says dashboard, content describes unrelated module

When mismatch occurs:

- decide whether to rename file
- rewrite title
- move content
- classify as raw, scaffold, placeholder, or wrong file
- update references if renamed

Do not ignore title-name mismatch when it affects future navigation.

---

# Reference Confidence

Every important reference should have confidence.

## Confirmed

The file or relationship was inspected or documented.

## Inferred

Likely based on structure or naming.

## Proposed

Suggested by the model.

## Legacy

Belongs to older structure.

## Unknown

Cannot verify current state.

The model should not present inferred or proposed references as confirmed.

---

# Minimal Traceability For Early Projects

Early projects may not need complex traceability.

Minimum useful traceability may include:

- project root
- current active artifact
- parent artifact if any
- next intended artifact
- accepted decisions
- open questions

Do not overbuild traceability before the project needs it.

---

# Strong Traceability For Complex Projects

Complex projects may need stronger traceability.

Use stronger traceability when:

- many artifacts exist
- parent-child hierarchy matters
- implementation depends on documentation
- decisions affect many files
- project has multiple branches
- knowledge sources matter
- compliance or high-stakes decisions exist
- naming conflicts are common
- AI-assisted navigation is important

Strong traceability should improve work, not become bureaucracy.

---

# Project Instance Placement

Project-specific naming and reference standards should live in the project instance.

Possible project-specific files may include:

    06_PROJECT_PRIMITIVES_AND_SHARED_RULES.md
    09_PROJECT_DOCUMENTATION_STANDARD.md
    10_PROJECT_REFERENCING_AND_TRACEABILITY_STANDARD.md

Exact names depend on the project.

This orchestration file only defines the general method.

---

# Project Instance Application

A complex project instance may need strong referencing because it has:

- platform standards
- dashboard branches
- admin dashboard modules
- parent and child PRDs
- state taxonomy
- event taxonomy
- UI standards
- implementation standards
- placeholders and scaffolds
- many module files
- migration from old paths

For the active project, project-specific traceability rules belong inside the active project folder.

The general orchestration layer provides method only.

Do not make project-specific paths universal.

---

# Failure Signals

Referencing, naming, and traceability failures include:

- using old paths after migration
- presenting proposed paths as existing
- using short reference when full path is needed
- malformed path display in Arabic context
- numeric prefix appears after extension
- file name and title conflict
- parent-child relationship is unclear
- child artifact has no parent reference
- renamed file still referenced by old name
- structure index does not match actual repository
- general method files contain project-specific canonical paths
- project files depend unnecessarily on upper-layer paths
- decision changes are not reflected in references
- aliases are treated as separate concepts
- artifact codes are used without definition

When failure occurs, correct references before deeper artifact work.

---

# Final Principle

Clear references make project intelligence durable.

The model must name things consistently, reference the right level of context, distinguish existing from proposed paths, preserve parent-child traceability, and update references when structures change.

A strong referencing method prevents navigation errors, stale paths, orphan artifacts, and repeated confusion.