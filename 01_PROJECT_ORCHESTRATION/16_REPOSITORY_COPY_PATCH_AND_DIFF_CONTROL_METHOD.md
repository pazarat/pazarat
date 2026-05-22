# REPOSITORY COPY PATCH AND DIFF CONTROL METHOD

# Purpose

This file defines how the model should modify an existing repository, project folder, document set, codebase, or packaged artifact without accidentally losing, regenerating, mixing, or rewriting unrelated content.

It is part of the project orchestration layer.

It is not a project instance file.

It is not a project-specific change log.

It is not a replacement for project-local standards.

It must not store fixed claims about any current project, artifact, folder, file, maturity, weakness, strength, priority, or roadmap.

Its purpose is to define the controlled repository editing method: preserve the existing baseline, apply only the intended patch, compare the result against the original, and report the exact changed surface.

---

# Core Principle

When an existing repository or folder is provided, the model must treat it as the source baseline.

The model must not simulate the repository from memory.

The model must not regenerate the repository merely to add a small change.

The safe method is:

1. copy or extract the current repository exactly as the working baseline,
2. apply a bounded patch to the intended location,
3. compare the patched version against the original baseline,
4. verify that only intended files changed,
5. package or return the patched result.

This method protects continuity, accepted decisions, local standards, hidden dependencies, file ordering, wording, and project-specific truth.

---

# What This File Owns

This file owns the general method for controlled repository patching.

It defines:

- copy-before-edit discipline
- baseline preservation
- patch scope declaration
- targeted file editing
- no-regeneration protection
- repository diff review
- changed file reporting
- unexpected-change rejection
- validation before packaging
- safe delivery of modified repositories
- limitations of practical guarantees

This file does not own:

- the content of a specific project file
- the decision to accept a specific change
- the project-specific change log
- code style rules for a specific application
- the actual test suite of a specific codebase
- the final release approval of a specific repository

Those belong in the relevant project instance, project-local standards, implementation artifacts, or user approval flow.

---

# Copy Before Edit Rule

For any request that modifies an existing repository, the model must use the provided repository as the starting point.

The model should operate on a copied or extracted working directory, not on a reconstructed approximation.

The model must preserve every file that is not intentionally modified.

The model must not rewrite unrelated files to make the repository look cleaner.

The model must not normalize formatting, line endings, names, or ordering unless that is part of the requested change.

The model must not replace accepted content with a newly generated version when a localized patch is sufficient.

---

# No Repository Regeneration Rule

A repository patch is not repository regeneration.

The model must not:

- read the repository and then generate a similar new repository from memory
- infer missing files and silently replace existing ones
- collapse multiple files into a new structure unless explicitly requested
- rewrite mature files just because the model can produce cleaner wording
- change file names or folder placement without a layer or project-standard reason
- treat a zip package as a prompt to rebuild everything from scratch

The model may generate a new repository only when the user explicitly asks for a new scaffold, full replacement, migration, or generated application.

Even then, accepted source material and project standards must be preserved or explicitly mapped.

---

# Patch Scope Declaration Rule

Before or during a repository patch, the model should identify the intended patch scope.

The scope may include:

- files to add
- files to modify
- files to delete
- files to move
- sections to insert
- sections to replace
- expected validation checks
- files that must remain untouched

If the exact scope is not known at the start, the model should keep the patch narrow, inspect the repository, and expand only when repository evidence justifies it.

A broad patch requires stronger verification than a narrow patch.

---

# Targeted Editing Rule

When editing files, the model should prefer the smallest sufficient operation:

1. insert a new section,
2. replace one section,
3. append a reinforcement note,
4. add a new file,
5. update a narrow reference,
6. only then consider a full file rewrite.

Full file rewrites are allowed only when:

- the file is being created for the first time,
- the user requested full replacement,
- the existing file is structurally broken,
- patching would create contradiction,
- the architecture decision requires replacement,
- or the file is generated code/artifact where regeneration is the safest route.

Even in these cases, accepted meaning must be preserved unless explicitly rejected.

---

# Trivial Edit Exception Rule

Not every repository correction requires a full archive regeneration or full delivery cycle.

For very small, low-risk edits such as one spelling correction, one wording correction, one sentence insertion, or one local paragraph adjustment, the model may provide an exact patch instruction, replacement text, or targeted file snippet instead of repackaging the entire repository, unless the user explicitly asks for a modified archive.

A trivial edit remains safe only when all of the following are true:

- the target file and location are clear,
- the edit affects only one narrow location,
- the edit does not change architecture, accepted terminology, cross-file references, numbered tunnel behavior, code execution, schema, state taxonomy, event taxonomy, or project-local truth,
- the user can reasonably apply or review the change directly,
- no multi-file consistency risk exists.

When an edit is scattered, repeated, structural, multi-file, architecture-level, code-level, standard-level, terminology-changing, or likely to affect repository behavior, the model must use the controlled copy-patch-diff workflow.

The model must not use the trivial edit exception to avoid verification for meaningful repository changes.

---

# Single File Controlled Patch Rule

When the requested change targets one existing file and is more than a trivial edit, the model should use a file-level copy-patch-diff workflow rather than regenerating the entire repository.

The model must:

1. read the current target file as the source baseline,
2. preserve the file text exactly outside the intended edit surface,
3. apply only the requested local additions, removals, terminology changes, wording improvements, or paragraph replacements,
4. compare the patched file against the original file,
5. verify that the changed regions match the user's intent,
6. return the patched file, exact replacement block, or unified diff instead of repackaging the whole repository unless the user asks for an archive or the change creates cross-file obligations.

This rule is especially important for mature scenario files, PRDs, standards, user-management scenarios, workflows, state/event documentation, and other cumulative artifacts where regenerating the whole file from memory may introduce drift, wording changes, hidden deletions, or conceptual mixing.

The model must not rewrite the whole target file from memory merely because the requested change affects the meaning of one paragraph, removes filler, improves weak wording, changes a term, adds one line, or deletes a narrow section.

If the target file needs a full-file replacement, the model must state that explicitly and justify why localized patching is insufficient.

---

# File-Level Delivery Rule

When a controlled patch changes only one existing file, the default delivery should be the updated file itself, an exact patch instruction, or a focused diff.

The model should not return a full repository archive for a one-file change unless:

- the user explicitly requests a zip or full repository package,
- the one-file change requires index, memory, changelog, routing, or cross-reference updates elsewhere,
- the patch is part of a larger repository migration,
- validation requires preserving surrounding repository structure,
- or the edited file cannot be safely delivered independently.

For one-file delivery, the report should include:

- target file path,
- kind of edit performed,
- whether the rest of the file was preserved,
- changed section summary,
- validation performed,
- any cross-file risk not handled.

The model must not force full-archive delivery when a file-level artifact is safer, clearer, and lighter.

---

# New File Creation Delivery Rule

When the user asks for a new standalone file and no existing repository file must be modified, the model may create and return only the new file.

The model should not repackage the whole repository merely to deliver a new standalone file unless the new file must also be registered in an index, tunnel, memory file, project structure tree, build system, route table, or cross-file reference set.

If the new file belongs to a numbered tunnel, project hierarchy, or codebase that requires registration, the model must classify the task as a multi-file patch and use the repository-level controlled patch workflow.

---

# Semantic Revision Preservation Rule

When improving wording, removing filler, tightening prose, correcting terminology, or clarifying an existing scenario or PRD section, the model must preserve the accepted meaning and surrounding artifact structure.

The model must distinguish between:

- stylistic cleanup,
- terminology correction,
- filler removal,
- local paragraph replacement,
- semantic change,
- scope change,
- architecture change,
- project truth change.

Stylistic cleanup must not silently become semantic change.

Terminology correction must not silently rename project primitives, states, events, roles, screens, routes, permissions, or lifecycle concepts unless the user asked for that and the relevant standards allow it.

Filler removal must not remove accepted constraints, hidden dependencies, rationale, edge cases, traceability, or user decisions.

If the user asks to make a section clearer, the model should improve only that section and keep unrelated sections byte-for-byte or text-identical where tooling allows.

---

# Diff Verification Rule

After applying a repository patch, the model must compare the patched repository with the original baseline whenever tooling allows.

The comparison should identify:

- added files
- modified files
- deleted files
- moved or renamed files
- unexpected binary changes
- unintended formatting changes
- accidental line-ending changes when visible
- whether only intended paths changed

If the diff contains unexpected changes, the model must not present the result as clean.

The model should either repair the unintended changes or clearly report the issue.

---

# Content Preservation Guarantee Rule

The model may claim practical preservation only after comparing the original baseline with the patched copy.

Correct claim:

    All inspected repository contents are unchanged except the reported added or modified files.

Incorrect claim:

    It is guaranteed forever that no error is possible.

The strongest practical claim is content-level preservation verified by comparison.

A compressed archive may differ at the package binary level because compression metadata, ordering, or timestamps can change, even when the extracted file contents are preserved.

Therefore, verification should focus on extracted repository contents unless the user specifically requires byte-for-byte archive reproduction.

---

# Hash Manifest Rule

For high-precision repository work, the model should create or reason from a content manifest when possible.

A manifest may include:

- relative file path
- file size
- content hash
- binary or text classification

The model can compare before-and-after manifests to verify that untouched files remain identical.

This is especially useful when the repository is large, contains many files, or includes binary assets.

---

# Validation Rule

A repository patch should be validated at the level appropriate to the change.

Possible validation includes:

- file diff
- syntax check
- markdown structure review
- schema validation
- linting
- type checking
- test execution
- build execution
- link/path inspection
- tunnel consistency inspection
- project-local standard consistency review

The model must not claim that tests, builds, or linters passed unless they were actually run or the user provided evidence.

If validation is not available, the model should state that only structural or diff verification was performed.

---

# Repository Patch Report Rule

When returning a modified repository, the model should report the changed surface clearly.

The report should include:

- source baseline used
- added files
- modified files
- deleted files, if any
- moved files, if any
- purpose of each change
- section-level or paragraph-level operations when meaningful
- validation performed
- known limitations
- download link or exact patch text when applicable

The report should not include unnecessary internal tool details.

The report should help the user trust that the change was controlled, not randomly regenerated.

---

# Section-Level Change Ledger Rule

For meaningful repository, tunnel, documentation, scenario, standard, or PRD patches, file-level diff reporting is necessary but not always sufficient.

When a patch adds, deletes, moves, merges, or substantially rewrites sections or paragraphs, the model should include a section-level change ledger when practical.

The ledger should identify:

- sections added,
- paragraphs added,
- paragraphs or sections replaced,
- paragraphs or sections deleted,
- paragraphs or sections moved,
- duplicated objectives merged,
- objectives strengthened before deletion,
- filler removed,
- preserved areas that remained unchanged,
- and validation performed against the user intent.

A deletion must never be reported only as a reduction in length.

When deleting duplicate or weak text, the model must explain whether the useful objective was already preserved, strengthened elsewhere, moved to a better owner, or intentionally removed because it was harmful, obsolete, conflicting, or out of scope.

If two weak duplicate paragraphs both contain useful constraints, the model should first consolidate or strengthen the correct owner paragraph, then delete the duplicate.

The report must make it clear that deletion, movement, or consolidation was controlled and did not accidentally weaken the repository.

---

# Rejection And Recovery Rule

If the model detects unintended changes after a patch, it must treat that as a patch failure.

Correct recovery:

1. identify the unintended change,
2. restore the affected file from baseline when possible,
3. rerun the comparison,
4. report the final changed surface,
5. avoid packaging a contaminated result as clean.

If recovery is not possible, the model must say so plainly.

---

# Generated Code From Repository Rule

When the user asks the model to generate a new website, application, module, or code folder from an existing project repository, the model must distinguish between two different actions.

## Patch Existing Repository

Use this method when the user wants changes inside the same repository.

The model must preserve the existing repository and modify only intended paths.

## Generate New Derived Artifact

Use this method when the user wants a new folder, scaffold, application, prototype, or implementation derived from repository documentation.

The model may create a new generated folder, but it must use repository standards, project-local terminology, accepted states, accepted events, UI/UX rules, implementation rules, and reference profiles as governing inputs.

The generated artifact should include a README or notes explaining what source standards governed it when useful.

The model must not confuse a generated derived artifact with a patch to the source repository.

---

# Practical Limits Rule

Controlled patching can make repository modification highly accurate, but it is not a metaphysical guarantee against all possible errors.

Accuracy depends on:

- repository size
- file types
- available tooling
- clarity of requested change
- ability to compare before and after
- whether tests or builds can be run
- whether external dependencies are available
- whether the repository itself has contradictions

The model must be honest about what was verified and what was not verified.

The model should prefer verified precision over confident claims.

---

# Operating Summary

For existing repository edits, the model must work like this:

1. enter the repository through the entry map,
2. follow the required numbered tunnel,
3. classify whether the requested change is missing, weak, duplicated, misplaced, conflicting, or already sufficient,
4. copy or extract the baseline,
5. patch only the intended location,
6. compare the patched repository with the baseline,
7. reject or repair unintended changes,
8. validate at the appropriate level,
9. report the exact changed surface,
10. return the patched repository or exact patch.

This keeps repository evolution cumulative, traceable, and safe.
