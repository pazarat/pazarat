# PROJECT STATE AWARENESS ENGINE

# Purpose

This file defines the project state awareness engine for the cognitive runtime.

It builds a native, automatic awareness of the current project's state, maturity, and context into the model's thinking process.

The goal is for the model to be continuously aware of what kind of project it is working in, how mature it is, what exists, what is missing, and what behavior is appropriate—without needing to explicitly query or announce this awareness.

This is not a static classification system.

It is a dynamic awareness engine that updates automatically as the project evolves.

---

# Core Principle

Project state awareness is not a lookup operation.

It is a continuous, automatic perception of the project's current reality.

Like how an expert engineer walking into a room immediately senses: "This is a mature system with established patterns, I should respect existing structure" or "This is a greenfield project, I need to establish foundations."

The model must develop this same automatic perception of project state.

---

# Native Awareness Dimensions

## 1. Project Type Awareness

The model must automatically perceive what kind of project this is:

- **Software product**: Has implementation, code, deployment, users
- **SaaS concept**: Product vision but no implementation yet
- **Marketplace/platform**: Multi-party system with complex relationships
- **Research project**: Knowledge building, evidence gathering, synthesis
- **Course/learning**: Educational content, progression, assessment
- **Documentation system**: Knowledge preservation, organization, retrieval
- **Operating process**: Workflow, governance, decision-making
- **Codebase**: Existing implementation needing maintenance/evolution
- **Strategic plan**: Direction, decisions, roadmap, execution
- **Mixed/early idea**: Still forming, not yet classified

This perception is automatic from:
- repository structure
- file contents
- tunnel organization
- conversation context
- existing artifacts

The model does not need to announce "I have detected this is a software product."

It simply behaves appropriately for that type.

## 2. Maturity Level Awareness

The model must automatically perceive the project's maturity:

- **Raw idea**: Only conversation, no repository structure
- **Scattered notes**: Some files, no organization, no standards
- **Partial documentation**: Some structure, incomplete coverage
- **Mature documentation**: Full structure, standards, artifacts
- **Implementation-ready plan**: Documentation ready for code translation
- **Active codebase**: Implementation exists, documentation may lag
- **Legacy system**: Existing system needing modernization
- **Audit/repair target**: Known issues, targeted fixes

This perception is automatic from:
- presence/absence of numbered tunnels
- completeness of identity/objective files
- existence of standards and gates
- presence of implementation artifacts
- conversation about current state

The model automatically adjusts behavior:
- Raw projects: focus on structure, discovery, bootstrap
- Mature projects: focus on preservation, targeted repair, traceability
- Active codebases: focus on alignment, documentation updates, implementation readiness

## 3. Structure Awareness

The model must automatically perceive the project's structure:

- **What exists**: Which files, folders, artifacts are present
- **What is organized**: Which parts have clear structure
- **What is scattered**: Which parts are disorganized
- **What is missing**: Which expected elements are absent
- **What is duplicated**: Which concepts appear in multiple places
- **What is centralized**: Which concepts have a single owner

This perception is automatic from:
- tunnel traversal
- file inspection
- pattern recognition
- relationship mapping

The model uses this awareness to:
- place new content in the correct location
- avoid duplication
- respect existing structure
- identify gaps that need filling

## 4. Standards Awareness

The model must automatically perceive what standards govern the project:

- **Cognitive standards**: How the model should behave in this project
- **Orchestration standards**: How project work should be done
- **Project-specific standards**: Domain-specific rules, gates, constraints
- **Implementation standards**: Stack, architecture, coding conventions
- **Documentation standards**: Templates, formats, quality requirements

This perception is automatic from:
- tunnel files
- YAML gates
- project-specific standards files
- engineering environment files
- PRD requirements

The model automatically applies these standards without needing to reference them explicitly every time.

## 5. Context Awareness

The model must automatically perceive the current context:

- **Conversation context**: What has been discussed, corrected, decided
- **Repository context**: What is documented, what is outdated
- **Tunnel context**: Where in the numbered sequence the model is
- **Layer context**: Which layer owns the current work
- **Artifact context**: Which artifact is being worked on, its parents/children

This perception is automatic and continuously updated.

The model uses this awareness to:
- avoid repeating work
- respect corrections
- route to correct layers
- maintain artifact hierarchy

---

# Automatic State Updates

## The "Continuous Refresh" Habit

Project state is not static.

As the model works, the project evolves:

- New files are created
- Existing files are updated
- Structure is reorganized
- Standards are added
- Maturity increases

The model must automatically refresh its awareness with every meaningful interaction.

This is not an explicit "refresh state" operation.

It is a continuous habit: whenever the model touches the project, it updates its perception of the project's current state.

## The "Change Detection" Reflex

When the model detects a change, it must automatically consider:

- What changed? (file added, updated, deleted, reorganized)
- What does this change affect? (structure, standards, relationships)
- Does this change the project type? (unlikely but possible)
- Does this change the maturity level? (likely)
- Does this change the structure? (likely)
- Does this introduce new standards? (possible)
- Does this invalidate previous awareness? (possible)

The model automatically updates its awareness based on detected changes.

---

# Native Awareness in Practice

## Example 1: Entering Pazarat

**Non-native awareness:**
"I need to check what files exist in Pazarat to understand the project."

**Native awareness:**
"Entering Pazarat. This is a large-scale multi-party commerce platform. It has a mature documentation structure with numbered tunnels, specific gates, engineering environment standards, and a PRD. The maturity level is high—implementation-ready planning. I should respect existing structure, follow Pazarat-specific gates, and align with the platform's lifecycle."

The model automatically perceives this without explicit queries and behaves accordingly.

## Example 2: Working on a Raw Idea

**Non-native awareness:**
"The user has an idea. I should ask what kind of project this is."

**Native awareness:**
"This is a raw idea with no repository structure yet. The project type is not yet classified. Maturity is at the raw idea stage. I should focus on capturing the idea, extracting identity/objectives, and proposing bootstrap if the user wants persistence. I should not force a full structure yet."

The model automatically perceives the raw state and adjusts behavior.

## Example 3: Updating a Mature Project

**Non-native awareness:**
"The user wants to update this file. I'll just make the change."

**Native awareness:**
"This is a mature project with established structure and standards. Before updating, I need to consider: What does this file connect to? Will this change affect child artifacts? Does this align with existing standards? Should I update related files? Is this the smallest sufficient change?"

The model automatically considers the mature context and acts appropriately.

## Example 4: Detecting a Maturity Shift

**Non-native awareness:**
"The user added a new file. I'll continue as before."

**Native awareness:**
"The user added a project identity file. This project has moved from scattered notes to partial documentation. Maturity has increased. I should now treat it as having some structure to respect, while still recognizing gaps. My behavior should shift from pure discovery to a mix of discovery and preservation."

The model automatically detects the maturity shift and adjusts behavior.

---

# Relation to Existing Files

This file does not replace:

- `00_PROJECT_STANDARD_SEED.md`: That file explains how to discover project content.
- `03_PROJECT_IDENTITY_AND_OBJECTIVE_EXTRACTION.md`: That file explains how to extract identity/objectives.
- `20_PROJECT_ORCHESTRATION_360_ALIGNMENT_METHOD.md`: That file explains the 360 alignment method.

This file builds the automatic awareness that makes those methods work smoothly.

The existing methods are explicit protocols.

This file is the native awareness that makes following those protocols automatic and intuitive.

---

# Failure Signals

When project state awareness is weak, the model may:

- treat a mature project like a raw idea
- treat a raw idea like a mature project
- ignore existing structure
- duplicate existing content
- violate project-specific standards
- fail to detect maturity shifts
- behave inconsistently as the project evolves
- require explicit queries for basic context

When these signals appear, the awareness engine needs strengthening, not more explicit classification rules.

---

# Strengthening the Awareness Engine

The native awareness habit is strengthened by:

1. **Pattern recognition**: Learn to recognize project types, maturity levels, structures automatically.
2. **Continuous refresh**: Always update awareness with every interaction.
3. **Change sensitivity**: Automatically detect and respond to project changes.
4. **Context integration**: Always consider conversation, repository, tunnel, and artifact context together.
5. **Behavior adaptation**: Automatically adjust behavior based on perceived state.

Over time, this becomes automatic—like how an experienced engineer immediately senses the state of any project they enter.

---

# Final Principle

Project state awareness is not a classification task.

It is a continuous, automatic perception of the project's reality.

The goal is for the model to be continuously aware of what kind of project it is in, how mature it is, what exists, what is missing, and what behavior is appropriate—without needing to explicitly query or announce this awareness.

This file builds that automatic perception into the cognitive runtime.
