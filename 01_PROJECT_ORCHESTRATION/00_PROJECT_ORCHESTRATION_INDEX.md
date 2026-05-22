# PROJECT ORCHESTRATION INDEX

## Purpose

This file documents the active file structure and responsibility map for the `01_PROJECT_ORCHESTRATION` layer.
It is intended to make this layer easier to maintain, improve, and navigate without altering the existing project orchestration method.

## Layer role

`01_PROJECT_ORCHESTRATION` is the general project-building method layer.
It owns how raw input becomes project work, how project work is classified, how project standards are proposed, and how project-local truth is discovered and handed off.
It is not a specific project layer, not a project identity layer, and not a project-specific implementation layer.

## Files and responsibilities

- `00_PROJECT_ORCHESTRATION_ENTRY.md`
  - entry behavior for the project orchestration layer; defines what the layer owns and what it must not own.

- `01_RAW_INPUT_UNDERSTANDING_AND_IDEA_CAPTURE.md`
  - raw idea reception, input preservation, and early signal extraction.

- `02_PROJECT_OR_NON_PROJECT_CLASSIFICATION.md`
  - decides whether the work is project-related or non-project-related and selects the right processing path.

- `03_PROJECT_IDENTITY_AND_OBJECTIVE_EXTRACTION.md`
  - general method for extracting and validating project identity and objectives from evidence.

- `04_PROJECT_STANDARD_LAYER_FACTORY.md`
  - method for proposing and bootstrapping a project-specific standard layer.

- `05_PROJECT_SCOPE_STRUCTURE_AND_DOMAIN_MODELING.md`
  - scope, structure, and domain modeling methodology.

- `06_PROJECT_MATURITY_AND_ARTIFACT_INTENT_ASSESSMENT.md`
  - maturity evaluation and artifact intent assessment.

- `07_PROJECT_KNOWLEDGE_DISCOVERY_AND_LEARNING_MAP.md`
  - identifies knowledge needs, gaps, and learning/research requirements.

- `08_PROJECT_PLANNING_STRATEGY_AND_ROADMAP_METHOD.md`
  - planning, strategy, and roadmap sequencing method.

- `09_PROJECT_DOCUMENTATION_ARCHITECTURE_AND_HIERARCHY.md`
  - documentation architecture, artifact hierarchy, and parent/child artifact design.

- `10_PROJECT_ARTIFACT_GENERATION_AND_REVISION_METHOD.md`
  - artifact generation and revision method across project work.

- `11_PROJECT_DECISION_MEMORY_AND_CHANGE_CONTROL.md`
  - decision memory, change control, and decision routing.

- `12_PROJECT_INSTANCE_HANDOFF_AND_DYNAMIC_DISCOVERY.md`
  - handoff from general method to the active project instance and dynamic discovery behavior.

- `13_PROJECT_REFERENCING_NAMING_AND_TRACEABILITY_METHOD.md`
  - naming, referencing, traceability, and stable artifact references.

- `14_PROJECT_SHARED_PRIMITIVES_AND_REUSABLE_LOGIC_METHOD.md`
  - shared primitive detection, reusable logic, and cross-artifact continuity.

- `15_UNIVERSAL_KNOWLEDGE_REFERENCE_LIBRARY_METHOD.md`
  - how to activate domain knowledge reference alphabets when needed.

- `16_REPOSITORY_COPY_PATCH_AND_DIFF_CONTROL_METHOD.md`
  - safe repository patching, baseline preservation, and diff discipline.

- `17_EXPERT_METHOD_SELECTION_AND_ARCHITECTURE_OPTIMIZATION.md`
  - expert method selection and architecture optimization rules.

- `18_PROJECT_EXECUTION_GATES.yaml`
  - project orchestration command board for runtime activation and routing.

- `19_EXPERT_PROJECT_ENGINEER_OPERATING_ROLE.md`
  - defines the expert project engineer role used inside project orchestration.

- `20_PROJECT_ORCHESTRATION_360_ALIGNMENT_METHOD.md`
  - project-level 360-degree coherence method.

- `21_PROJECT_REALITY_CALIBRATION_AND_GOLDEN_SYNTHESIS_METHOD.md`
  - calibrates raw input, scenarios, artifacts, and repairs against current project reality so mature output is synthesized from user intent, domain knowledge, existing structure, lifecycle, and project-local standards.

- `22_REPOSITORY_STRUCTURAL_TRANSFORMATION_AND_CODEBASE_INTEGRATION_GATE.md`
  - mandatory gate for repository-level structural transformations, codebase integration, documentation/code routing, root preservation, and migration-map validation.

- `99_PROJECT_ORCHESTRATION_REINFORCEMENT_MEMORY.md`
  - compact reinforcement memory for the project orchestration layer.

## Improvement goals

This index is intended to support:

1. faster layer review and refactoring,
2. easier detection of overlap or merge candidates,
3. clearer separation of general method vs specific project work,
4. direct alignment between YAML gates and file responsibility.
5. highlighting layer-boundary issues so project orchestration stays method-level only.
