# COGNITIVE RUNTIME INDEX

## Purpose

This file documents the active file structure and responsibility map for the `00_COGNITIVE_RUNTIME` layer.
It is intended to make this layer easier to maintain, inspect, and improve without changing the existing runtime method.

## Layer role

`00_COGNITIVE_RUNTIME` is the repository’s cognitive behavior layer.
It owns model-level synchronization, intent detection, evidence discipline, conversation memory, failure correction, output behavior, tunnel discovery, and operational validation.
It is not a project layer, not a project identity layer, and not a project-specific standard layer.

## Files and responsibilities

- `00_COGNITIVE_ENTRY_AND_CONTEXT_SYNCHRONIZATION.md`
  - highest-level entry behavior; defines how the model synchronizes conversation, repository, numbered tunnel, and response mode.

- `01_USER_INTERACTION_AND_BEHAVIOR_DIRECTIVES.md`
  - interaction behavior, tone, correction handling, language rules, and specialist collaboration rules.

- `02_NUMBERED_TUNNEL_DISCOVERY_AND_LAYER_HANDOFF.md`
  - discovers numbered folders and routes from cognitive runtime into project orchestration and project instance layers.

- `03_CONVERSATION_MEMORY_AND_CONTEXT_SYNTHESIS.md`
  - preserves live conversation context, compares it with repository evidence, and balances it before responding.

- `04_INTENT_INFERENCE_AND_RESPONSE_MODE_SELECTION.md`
  - infers the actual user intent, chooses the correct response mode, and avoids mode collapse.

- `05_EVIDENCE_UNCERTAINTY_AND_TRUST_DISCIPLINE.md`
  - evidence classification, uncertainty handling, trust discipline, and prevent inference from becoming fact.

- `06_KNOWLEDGE_REASONING_AND_RESEARCH_DISCIPLINE.md`
  - uses knowledge intelligently, distinguishes general vs project-specific knowledge, and avoids shallow confidence.

- `07_OUTPUT_DISCLOSURE_AND_COMMUNICATION_STYLE.md`
  - output formatting, evidence disclosure levels, copy-safe generation, and path handling.

- `08_FAILURE_RECOVERY_AND_BEHAVIOR_CORRECTION.md`
  - failure classification, correction behavior, regression prevention, and recovery after mistakes.

- `09_CONVERSATION_ARTIFACT_REVISION_MEMORY.md`
  - cumulative artifact revision memory, baseline preservation, and safe iterative updates.

- `10_TUNNEL_PERFORMANCE_ENGINEERING_AND_SELF_IMPROVEMENT.md`
  - tunnel-performance diagnosis, repair strategy, and improvement of the repository operating route.

- `11_HYBRID_TUNNEL_RUNTIME_AND_EXECUTION_COMMANDS.md`
  - governs the hybrid use of Markdown standards and YAML command gates.

- `12_OPERATING_IDENTITY_AND_REPOSITORY_AWARENESS.md`
  - repository operating identity, generic assistant suppression, and repository-aware role behavior.

- `13_COGNITIVE_360_TUNNEL_COHERENCE_METHOD.md`
  - 360-degree coherence method for connected tunnel execution and integrated output.

- `14_DIRECT_COMMAND_PRECISION_AND_HARD_CONSTRAINT_EXECUTION.md`
  - hard constraint handling, direct command fidelity, and measurable execution discipline.

- `15_NATURAL_CONTEXTUAL_OUTPUT_AND_SILENT_MECHANICS_BOUNDARY.md`
  - boundary between internal mechanics and public answers; keeps tunnel mechanics silent unless relevant.

- `99_COGNITIVE_RUNTIME_REINFORCEMENT_MEMORY.md`
  - compact reinforcement memory for the cognitive runtime layer.

## Improvement goals

This index is intended to support three improvements:

1. Make the layer easier to review and refactor by showing file roles in one place.
2. Make it easier to detect overlaps and merge similar responsibilities when needed.
3. Preserve the existing runtime method while enabling targeted maintenance.
4. Highlight layer-boundary and natural behavior gaps so the cognitive runtime remains a clean reasoning layer.
