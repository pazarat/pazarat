# Engineer Runtime v6.12 — Central Operating Core Maturation Report

## Purpose

This release focuses on the central runtime core: navigation, jet matrix inspection, search, governed writing, and mandatory operating context.

The goal is not to add more guidance text. The goal is to make the runtime behave like an operating system entry point: a model plugs into one command and receives the route, protocol stack, tool keyboard, evidence gates, concept matrix, hard blocks, and receipt required for the current task.

## Added

- `plug` command as the default one-touch central operating entry.
- `cycle` now delegates to `plug` instead of running a minimal partial sequence.
- richer `matrix` output with concept buckets and mandatory read hints.
- `central_operating_core.yaml` governance contract.
- `one_touch_matrix_operating_cycle.md` protocol.
- `jet_matrix_navigation.md` protocol.
- v6.12 reference notes.
- tests for plug/cycle/matrix/write-gate behavior.

## Strengthened

- Route detection for central OS, plug, matrix, navigation, and environment maturation requests.
- Tool contract now treats `plug` as the default entry command.
- Tool registry includes `plug` and marks it as operating context, not a passive report.
- Runtime audit verifies the central plug command and core governance file.
- Runtime fingerprint excludes generated runtime outputs for both repository and runtime scopes to prevent self-stale cache warnings.

## Operating semantics

`plug <request>` returns:

- route and scope
- inspection depth
- tool keyboard
- protocol stack
- context pack summary
- evidence gates
- concept matrix
- mandatory next actions
- hard blocks
- fallback policy
- operation receipt

This output is a steering contract. The model should operate under it before answering, writing, or making high-impact claims.

## Verification performed

- `runtime-audit`: pass
- `doctor`: pass
- registry vs CLI commands: 36/36
- `tests/test_v612_central_operating_core.py`: 5 passed
- route checks for runtime, plug/matrix, write, research, and implementation translation requests

## Remaining design note

The runtime can enforce this path only when the host agent executes the internal tools. The repository now defines the mandatory path, but external hosts must still wire `plug` as the entry command or follow the protocol manually.
