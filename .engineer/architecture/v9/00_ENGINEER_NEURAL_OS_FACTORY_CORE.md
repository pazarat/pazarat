# Engineer Neural OS / Factory Core v9.1

## Purpose

This layer turns the engineer runtime from a set of tools into a stable operating factory. The factory serves the workshop, and the workshop contains the active project. New capabilities are added as engines, lenses, adapters, validators, or protocols inside the same lifecycle; they are not allowed to become isolated islands.

## Boundary Model

```text
Engineer Runtime / Factory Core
  ├─ central entry, routing, governance, matrix, tools, validation, ledger
  └─ 02_WORKSHOP
      ├─ _WORKSHOP_SYSTEM      # universal project standards, playbooks, maturity lenses
      └─ ACTIVE_PROJECT        # current project truth, may be empty or populated
```

The active project is inside the workshop boundary. The workshop is not a detached documentation folder; it is the method lens and project operating space served by the factory.

## Stable Core Loop

```text
intent_governance
→ central_entry
→ truth_surface_selection
→ truth_pulse_360
→ matrix_touch
→ workshop_lens
→ truth_grounded_goal_closure
→ strategy_simulation
→ missing_ring_scan
→ execution_readiness_gate
→ governed_execution
→ validation_doctor
→ maintenance_ledger
```

This loop is the factory lifecycle. Any future layer must attach to one or more lifecycle hooks.

## Capability Slots

1. Identity & Boundary
2. Intent Governance
3. Truth Access Matrix
4. Workshop Intelligence
5. Truth-Grounded Goal Closure
6. Strategy & Solution Simulation
7. Tool Orchestration
8. Execution Governance
9. Validation & Doctor
10. Ledger, Memory & Maintenance
11. Extension Layer

## Non-Negotiable Rules

- Intent is a compass, not executable truth, until grounded in current files.
- Current files outrank generated indexes, old reports, cache, and model memory.
- A solution is not accepted unless it closes the parent goal or is explicitly labeled partial.
- File Matrix Truth Pulse is the first nervous-system touch before strong project/runtime/workshop claims.
- File Matrix is the nervous access layer for workshop/project/runtime truth.
- No capability may be added as an island; it must register a slot, hook, doctor, and receipt.

## Operating Commands

- `neural-os`: return the stable factory architecture and slots.
- `file-matrix-pulse`: run the fast content-aware Truth Pulse before strong claims/plans.
- `factory-cycle`: run the neural operating loop for a request.
- `goal-closure`: convert a request into a truth-grounded goal contract and readiness verdict.
- `completion-audit`: test whether the parent goal is actually closed.
- `factory-health`: doctor for the factory layer.
