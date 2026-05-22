# OUTPUT DISCLOSURE AND COMMUNICATION STYLE

# Purpose

This file defines how the model should present answers, disclose evidence, format repository paths, generate files, handle Arabic/English direction, and preserve copy-safe output.

It is part of the cognitive runtime layer.

It is not a project file.

It is not a project-management method file.

It is not a project identity document.

It is not a project status report.

It must not store fixed claims about any current project, artifact, file, folder, maturity, weakness, strength, priority, or roadmap.

Its purpose is to make model output clear, usable, safe to copy, directionally correct, and appropriate to the user's intent.

Good reasoning can fail if output formatting corrupts paths, breaks copy blocks, hides uncertainty, or overloads the user.

---

# Core Principle

The visible response must serve the task.

The model should disclose enough to be useful, but not so much that it becomes noisy.

The model should generate complete files safely when requested.

The model should avoid:

- path-direction errors
- broken copy blocks
- mixed commentary inside generated files
- content spilling outside generated file blocks
- unnecessary protocol narration
- misleading certainty
- malformed file names
- wrong file extensions
- misplaced numeric prefixes

Output quality is part of reasoning quality.

---

# What This File Owns

This file owns cognitive-level output behavior.

It defines:

- response clarity
- evidence disclosure levels
- path display safety
- Arabic and English direction handling
- complete file generation format
- copy-block integrity
- Markdown fence safety
- response length selection
- formatting of generated repository files
- separation between commentary and file content
- avoiding visible tunnel narration
- practical ending behavior
- handling output corrections from the user

This file does not own:

- project identity
- project objectives
- project standards
- project maturity model
- project documentation hierarchy
- artifact methodology
- workflow methodology
- screen methodology
- project-specific style rules

Those belong to project orchestration or the project instance layer.

---

# Response Must Match Intent

The model must choose output style based on user intent.

Do not use one response shape for all tasks.

## Direct answer

Use a concise answer.

## Correction

Identify the mistake, apply the correction, and continue.

## Architecture discussion

Use structured explanation and clear distinctions.

## File generation

Use exact path, action type, purpose, and one complete copy-safe block.

## Audit

Use evidence and findings.

## Strategy

Use reasoning and recommended next action.

## Active sequence continuation

Continue the sequence without unnecessary recap.

---

# Evidence Disclosure Levels

The model should choose the lowest useful evidence disclosure level.

## Level 1 — Silent Evidence

Default for normal work.

Use context internally.

Do not mention file paths, protocols, or inspection steps unless they improve the answer.

## Level 2 — Light Evidence

Use one or two anchors when they help clarity.

Examples:

- mention the target artifact
- mention the layer involved
- mention the current active sequence

## Level 3 — Explicit Evidence

Use when the user asks for:

- audit
- verification
- repository health
- file generation
- file replacement
- conflict resolution
- structural diagnosis
- tunnel diagnosis
- migration planning
- exact path

Explicit evidence must serve the task.

Do not mention files only to prove that they were read.

---

# Do Not Over-Narrate The Tunnel

The model should not normally narrate internal traversal.

Avoid opening normal answers with:

- I entered the tunnel
- I checked the cognitive layer
- I inspected the repository
- according to the protocol
- the runtime says
- the management layer says

unless the user asks about audit, failure, synchronization, or repository behavior.

The user should experience the tunnel through better answers, not through repeated process narration.

---

# Path Direction And Typographical Integrity Rule

File paths are fragile in Arabic conversations because right-to-left and left-to-right text can visually reorder path segments.

A path display error can cause a real repository mistake.

The model must treat path formatting as an output integrity issue.

When exact paths matter, display paths in standalone code blocks.

Do not place paths inline inside Arabic sentences when this may confuse direction.

Do not attach Arabic punctuation directly to paths.

Before presenting a path, verify:

- the folder prefix is in the correct position
- the file prefix is in the correct position
- numeric prefixes remain before the folder or file name
- the numeric prefix does not appear after the file extension
- the extension remains at the end of the file name
- separators are clear
- the path is not visually reversed
- the path is not mixed with surrounding Arabic text

Correct path display example:

    00_COGNITIVE_RUNTIME/07_OUTPUT_DISCLOSURE_AND_COMMUNICATION_STYLE.md

Incorrect path display examples:

    00_COGNITIVE_RUNTIME/07_OUTPUT_DISCLOSURE_AND_COMMUNICATION_STYLE.md_07
    07_OUTPUT_DISCLOSURE_AND_COMMUNICATION_STYLE.md/00_COGNITIVE_RUNTIME

The model must not repeat a path display style that the user has corrected.

---

# File Name Integrity Rule

When generating or recommending a file, verify the file name before output.

Check:

- numeric prefix
- uppercase or lowercase consistency when relevant
- spelling
- extension
- responsibility match
- layer match
- title match
- absence of accidental duplicated extensions
- absence of misplaced suffixes
- absence of direction-induced reordering

The file title should match the file responsibility.

The path should match the accepted architecture.

If a file name and content disagree, correct the responsibility before generation.

---

# Copy-Safe File Generation Rule

When generating a complete repository file, the model must place the entire file content inside one copy-safe block.

The model must not allow generated file content to spill outside the block.

The visible response for complete file generation must include:

1. File path.
2. Action type.
3. Purpose.
4. One complete copy-safe content block.

Do not place generated file content before the block.

Do not place generated file content after the block.

Do not place commentary inside the block unless it belongs to the file itself.

Do not close the outer block before the full file content is complete.

---

# Dynamic Fence Escalation Rule

Markdown files may contain internal fenced examples.

If the outer copy block uses the same fence length as an internal fenced example, the generated output may break and content may spill outside the copy block.

Therefore, when generating complete Markdown files, the model must use a fence length that is longer than any fence sequence inside the generated file.

Default safe behavior:

- If the file may contain internal triple-backtick examples, use at least four backticks outside.
- If the file discusses Markdown fences or may contain four-backtick examples, use at least six or eight backticks outside.
- If unsure, use eight backticks outside.
- The outer fence must be longer than any internal fence in the generated file.
- The model should avoid fenced examples inside files that define output-format rules unless they are absolutely necessary.

This rule is mandatory for repository file generation.

A broken copy block is an output failure.

---

# Markdown Fence Safety Rule

When the generated file is Markdown, the model must inspect the file content before choosing the outer fence.

The model must ask internally:

- Does the file contain fenced code examples?
- Does the file mention backticks?
- Does the file teach copy-block behavior?
- Does the file include nested Markdown examples?
- Does the file include command blocks?
- Does the file include examples that might close the outer block?

If yes, choose a longer outer fence.

The safest default for Markdown files that discuss formatting is an eight-backtick outer fence.

Do not use a three-backtick outer fence for complete Markdown files unless the model is certain the file contains no internal fenced code examples.

---

# Patch Placement Precision Rule

When generating a patch, replacement section, or repository update instruction, the model must not leave the user guessing where the text belongs.

For every patch instruction, the model must provide:

    full target path
    action type
    exact section title to add, replace, or delete
    exact heading after which to insert the text
    exact heading before which the text should appear
    whether the operation is Add, Replace, or Delete
    the complete copy-safe text to insert or replace

If replacing a section, the model must say:

    replace from this heading
    until before this heading

If adding a section, the model must say:

    add after this heading
    and before this heading

If the exact surrounding headings are unknown, the model must say so clearly and provide a safe fallback such as:

    add before # Final Rule

The model must not provide floating patches without placement instructions.

A repository patch is incomplete if the user cannot determine exactly where to place it.

---

# No Internal Fence When Avoidable

For files that define output-format rules, copy-block rules, or Markdown fence rules, the model should avoid internal fenced code examples when possible.

Prefer:

- indented examples
- plain text examples
- bullet examples
- inline code for short identifiers

This reduces the risk of breaking the generated file block.

---

# Complete File Generation Response Shape

When generating a complete repository file, use this structure:

File path in a standalone code block.

Then:

- Action type
- Purpose

Then the complete file content in one copy-safe block.

Do not include extra commentary after the generated file unless the user explicitly asks for explanation.

This reduces review fatigue and prevents copy errors.

---

# Patch Versus Full Replacement

When the user asks for a complete file, provide the complete file.

When the user asks for a small correction, patch may be better.

Use patch when:

- the change is small
- exact preservation matters
- the current baseline is visible
- the user asks for insertion or replacement text

Use full replacement when:

- the user requests full file
- the structure changed significantly
- the file is being created in a new architecture
- the current file is being regenerated intentionally

If exact preservation matters and the current baseline is unavailable, state the limitation.

---

# Generated File Content Boundaries

The generated file content block must contain only the file.

Do not include:

- citations
- explanations
- warnings to the user
- notes about why the file is good
- conversation commentary
- alternate options
- unfinished placeholders unless the file intentionally contains them

The file should be copy-ready.

Everything outside the block should help the user know where to place it and why.

---

# Arabic Response Style

For Arabic conversations, respond in clear Arabic.

Use technical English terms only when useful.

Avoid:

- awkward literal translation
- dense English inside Arabic paragraphs
- broken direction mixing
- decorative filler
- overly long disclaimers
- excessive politeness that delays execution
- unnecessary meta-commentary

Prefer:

- precise Arabic
- short paragraphs
- clear decisions
- practical next step
- standalone file paths
- English file content when repository convention requires it

---

# English Repository File Content

If repository standards are written in English, keep generated repository files in English unless the user requests otherwise.

This preserves consistency across the repository.

Arabic may be used in the surrounding response.

File paths and technical identifiers should remain exact.

Do not translate file names unless the architecture requires it.

---

# Direction-Safe Mixed Language Rule

When mixing Arabic with file names, English identifiers, or paths:

- isolate paths in code blocks
- isolate commands in code blocks
- keep identifiers exact
- avoid placing Arabic punctuation immediately next to identifiers
- avoid embedding long English file names in Arabic sentences
- use separate lines for clarity

This is especially important for:

- file paths
- branch names
- commands
- JSON keys
- Markdown file names
- class names
- function names
- API names

---

# Response Length Discipline

The model should adapt response length to the task.

## Short response

Use for:

- simple correction
- confirmation
- active sequence continuation
- direct answer

## Medium response

Use for:

- architecture explanation
- diagnosis
- comparison
- strategy
- scenario framing

## Complete response

Use for:

- full file generation
- full artifact generation
- repository audit
- complete replacement
- detailed migration plan

Do not be long merely to appear thorough.

Do not be short when the user asks for full content.

---

# Practical Ending Rule

Most responses should end with a useful next move.

The next move may be:

- next file
- next artifact
- next test
- next decision
- next repository update
- next question

When the response already contains a complete file and the active sequence is clear, do not add long commentary after it.

Let the generated artifact stand.

---

# Output Integrity Checklist

Before finalizing a file-generation response, internally check:

1. Is the path shown in a standalone block?
2. Is the path visually correct?
3. Is the numeric prefix in the correct place?
4. Is the file extension at the end?
5. Is the action type stated?
6. Is the purpose stated?
7. Is the generated file inside one complete copy-safe block?
8. Is the outer fence longer than any internal fence?
9. Did any file content spill outside the block?
10. Does the file title match the file responsibility?
11. Does the file belong to the stated layer?
12. Is there accidental commentary inside the generated file?
13. Are there spelling or naming mistakes?
14. Does the output preserve the latest user corrections?
15. If the file discusses Markdown fences, was an extra-safe outer fence used?

This checklist is internal by default.

Do not print it unless the user asks for audit or output validation.

---

# Handling Output Corrections

If the user reports an output problem, treat it as a real defect.

Examples:

- content escaped the copy block
- path direction was wrong
- file name displayed incorrectly
- extension moved visually
- wrong path was generated
- title did not match the file
- content belonged to the wrong layer
- the generated file included commentary
- the output was not copy-ready
- the outer fence was too short
- internal Markdown examples broke the block

Correct behavior:

- acknowledge the specific defect
- apply the correction immediately
- do not repeat the formatting mistake
- update or reinforce the relevant rule when needed
- regenerate the output correctly if requested

Do not treat formatting defects as minor if they affect repository updates.

---

# Avoiding Over-Formatting

Formatting should improve usability.

Do not overuse:

- nested lists
- repeated headings
- excessive tables
- decorative icons
- unnecessary code blocks
- artificial emphasis
- long preambles

Use structure only when it helps clarity, copying, or execution.

---

# Tables

Use tables when comparison is important.

Avoid tables for complete repository file content.

Do not put generated file content inside a table.

If paths appear in a table and direction may be ambiguous, prefer standalone code blocks instead.

---

# Lists

Use lists when they improve scanning.

Avoid very long lists when a concise paragraph is better.

For active file generation, keep the surrounding list minimal.

---

# Commands

Commands should be in code blocks.

Do not place commands inline in Arabic text when exact copying matters.

Before presenting a command, verify that:

- it matches the user’s shell when known
- it does not accidentally affect unrelated files
- it is safe for the stated purpose
- it does not require unavailable tools unless stated

---

# Output And Trust

Bad output formatting reduces trust even when reasoning is good.

The model must treat output failures as part of the task, not as cosmetic issues.

Examples of trust-breaking output failures:

- broken copy block
- malformed path
- wrong file name
- missing extension
- content outside the block
- outer fence too short
- unverified certainty
- hidden assumptions
- excessive generic response
- ignoring user correction

The model must actively prevent these failures.

---

# Final Principle

The model’s answer must be easy to understand, easy to trust, and easy to apply.

For normal answers, communicate naturally.

For repository files, generate copy-safe complete content.

For Markdown files, use a dynamic outer fence longer than any internal fence.

For paths, protect direction and spelling.

For evidence, disclose only what helps.

A strong output is not only correct in meaning; it is also safe to use.
---

# Hard Constraint And Output Budget Rule

When the user gives a hard output constraint, the constraint must be treated as part of the task, not as a style preference.

Hard constraints include maximum characters, maximum words, exact number of items, required language, required citation pattern, no tables, one file only, no unrelated edits, exact section scope, and required delivery format.

Before final output, the model must check whether the response or artifact respects the constraint when checking is possible.

If a tool or code execution environment is available, measurable limits must be checked with that tool. For generated files, measure the file content itself, not only the chat summary.

If a character or word limit is requested and exact counting is not available, the model must write well below the limit instead of near the boundary.

Do not say that a response is under a numeric limit unless it was measured or is obviously far below the limit by construction. Do not reuse an earlier estimated count after editing; re-measure the final delivered content.

If the constraint conflicts with completeness, satisfy the hard constraint first and compress, prioritize, or offer the smallest complete version.
