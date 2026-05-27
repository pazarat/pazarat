# Engineer Runtime v6.17 — Surface Truth Gate Surgical Patch

## Purpose

This release patches a critical project-surface behavior: the runtime must not select a broad domain or first step from folder names, domain scores, or general signals alone.

## Problem Fixed

Earlier project-surface answers could identify a strong domain but fail to expose the evidence chain that justified it. That made the answer look like a broad guess even when the underlying files contained stronger evidence.

This patch reinforces two core rules:

- current project files are the binding truth;
- incomplete truth remains truth and must be repaired before execution, not treated as absence or guessed around.

## Main Patch

Added a surface owner/child truth gate inside `project-lens`:

- it identifies a content-bearing owner truth file;
- it records content status, word count, signal count, headings, and evidence excerpt;
- it separates owner truth from incomplete child truth;
- it blocks broad-domain-first-step behavior;
- it blocks implementation from project-surface lens alone.

## New Behavior

A first-surface answer now distinguishes:

- the owner file that actually carries the domain truth;
- child files that exist but are empty/thin and therefore represent incomplete truth;
- the first step as owner-read + incomplete-truth maturation, not broad-domain selection.

## Verification

- `runtime-audit`: pass
- `doctor`: pass
- parser/registry command count: 43 / 43
- `tests/test_v617_surface_truth_gate.py`: passed
- previous surface-lens and surgical tests: passed when executed individually

## Packaging Rule

Generated indexes and ledgers are not packaged as truth. They are runtime cache only.
