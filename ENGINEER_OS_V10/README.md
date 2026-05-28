# ENGINEER OS V10 (Standalone, Production-Oriented)

This is a **standalone architecture release** for a governed project-engineer runtime.

## Design goals
- Project-neutral runtime core.
- Strict separation: Runtime / Workshop / Active Project.
- 360° decision discipline.
- No unsupported claim promotion.
- No patchwork-style isolated fixes.
- Modular governance without regression drift.

## Top-level map
- `00_CORE/`: identity, role, startup contracts.
- `01_GOVERNANCE/`: module contracts + guardrails.
- `02_PIPELINE/`: canonical execution lifecycle.
- `03_MATRIX/`: file/code sensing and impact contracts.
- `04_DOCTORS/`: self-health and integrity checks.
- `05_WORKSHOP/`: universal project standards factory.
- `06_ACTIVE_PROJECT/`: project-local truth contract.
- `07_RUNTIME/`: runtime commands and adapter contracts.
- `08_SCHEMAS/`: schema contracts.
- `09_TESTS/`: maturity and invariants tests.
- `10_MIGRATION/`: migration map from legacy runtime.

## Cutover
Use `ENGINEER_OS_V10/ENTRYPOINT.yaml` as the startup anchor for this standalone release.
