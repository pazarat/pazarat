# Engineer Runtime v6.16 — Jet Surface Lens & Actionable Matrix Maturation

## Purpose

This release is a surgical maturation of v6.15 focused on observed model behavior during a project-surface prompt. The goal is to keep the central plug mandatory while making the first answer faster, richer, and less raw-evidence driven.

## Problem Observed

A project-surface prompt such as "who are you, what is your role, how do you handle my project, what is the current state, and what is the first step" triggered the correct operating path but still produced a weak answer in some host-model runs:

- It could take too long if the host model read too much plug output.
- The answer could dump raw evidence snippets instead of forming a strong engineering assessment.
- Maturity grouping was too coarse because the whole active project could collapse into the root project folder.
- The relationship graph could overmatch generic Arabic request words instead of surfacing actionable project domains.

## Changes

### 1. Project Surface Lens

Added a fast project-surface lens used by `answer` and exposed through `plug`:

- project identity
- root truth sources
- category counts
- strongest actionable domain
- visible child gaps
- implementation status
- first-step candidate

Command:

```bash
python .engineer/commands/engineer.py project-lens --scope project
```

### 2. Stronger Natural Project Answer

`answer` now uses the project lens instead of raw evidence snippets. It produces a structured engineering answer that includes:

- role/identity of the engineer
- project identity
- evidence-based current state
- source-truth entry points
- strongest actionable domain
- visible gaps
- first step

### 3. More Actionable Maturity Grouping

`maturity-map` no longer collapses the whole active project into a single broad project key. It identifies actionable artifact domains such as:

- `business/User_Management`
- `governance/country_context`
- `system/...`

Root truth and cognitive tunnel remain visible but are excluded from the “first implementation slice” decision.

### 4. Better Surface Relationship Graph

For project-surface identity/status prompts, `relationship-graph` now uses a canonical surface-lens query rather than generic user wording. This prevents matches on words like “who/what/current/step” and increases the chance of surfacing true owner candidates.

### 5. Project-Surface Plug Improvement

`plug` compact output now includes `project_surface_lens` for surface prompts. This allows a host model to answer strongly without reading a large raw context pack.

### 6. Runtime Integrity Kept Clean

Static runtime neutrality was preserved: runtime files do not hard-code project-specific names or terms. Tests use split strings where needed to avoid turning test fixtures into runtime truth leaks.

## Verification

Observed checks:

- `doctor`: pass
- `runtime-audit`: pass
- parser/registry alignment: 43 / 43
- `tests/test_v616_jet_surface_lens.py`: 5 passed
- `answer` for the target project-surface prompt: about 2 seconds locally, about 4 KB output
- `plug` compact for the same prompt: about 4–5 seconds locally, includes project lens and first-step candidate

## Current Engineering Judgment

v6.16 improves the “first touch” experience: the central plug still forces operating awareness, but the answer path has a compressed project lens so the host model is less likely to behave like a generic assistant or dump raw evidence.

The next high-value step remains deeper graph indexing and modularization, but v6.16 intentionally avoids broad refactors to preserve stability.
