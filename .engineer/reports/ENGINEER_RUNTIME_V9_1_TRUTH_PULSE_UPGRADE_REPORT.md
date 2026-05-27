# Engineer Runtime v9.1 Truth Pulse Upgrade Report

## Scope

This upgrade applies the post-v9 observations to the successful v9.0 architecture. It does not downgrade the package to v8.x. It upgrades v9.0 into v9.1 by making the File Matrix Truth Pulse a mandatory nervous-system touch inside the Neural OS lifecycle.

## What changed

- Added `file-matrix-pulse` as a first-class CLI command.
- Integrated Truth Pulse into `plug-fast`, `goal-closure`, and `factory-cycle`.
- Added Truth Pulse to `tool_registry.yaml`.
- Upgraded `truth_grounded_goal_closure.yaml` to require pulse before strong answers, plans, and writes.
- Updated factory health to verify the pulse command.
- Kept v9 workshop/project boundary: `02_WORKSHOP` contains `_WORKSHOP_SYSTEM` and `ACTIVE_PROJECT`; access remains through the central runtime/matrix.

## Purpose

The pulse prevents blind truth by distinguishing:

- surface truth: file/folder exists;
- content truth: current file body contains meaningful content;
- incomplete truth: thin, placeholder, or draft surfaces;
- drift/contradiction candidates: files whose content has low alignment with the parent truth spine and must be reviewed before being treated as aligned truth.

## Operating rule

A model must not choose a project starting point from one file name, size, or superficial scan. It must use the pulse summary: truth spine, high-value content surfaces, incomplete truth candidates, drift candidates, and requested intent.

## Remaining production adapters

The following are still extension adapters, not bundled engines:

- Tree-sitter AST
- LSP bridge
- dense vector semantic index
- framework-specific extractors

They are explicitly reported by `file-matrix-doctor` so the system does not pretend they are complete.
