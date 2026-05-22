# PROJECT-SPECIFIC 360 INTEGRATION ENGINE

# Purpose

This file defines the project-specific 360 integration engine for the cognitive runtime.

It bridges the native cognitive engines (360 thinking, project state awareness, deep inference, self-questioning) with project-specific 360 methods that exist in the project instance layer.

The goal is for the model to automatically discover, understand, and apply project-specific 360 methods when working in a project that has one.

This is not a replacement for the general 360 methods.

It is an integration layer that makes project-specific 360 methods work seamlessly with the native cognitive habits.

---

# Core Principle

Project-specific 360 methods are not isolated protocols.

They are specialized implementations of the general 360 coherence principle, tailored to the specific project's domain, stack, and delivery path.

The integration engine ensures alignment between all directions: if we are building or generating text, this text must align with what came before it, what comes after it, and what reflects from it—and align with the project.

This is clearly illustrated with the documentation scenario standards: how scenarios must align with the reverse process when we want to generate code—the code translation standards must align with the scenario so that database rules or endpoints emerge from it.

If we write the scenario in a way that does not align with code translation, we will fail.

The same applies if we achieve the first and second conditions, but in the programming environment standards like backend and the programming architectural structure, code translation will fail due to lack of alignment between the three.

And if the three align but the scenarios or generation process do not align with the project objective, we will not succeed.

The model must automatically:

1. Discover if a project has a project-specific 360 method
2. Understand how that method works (what directions it connects)
3. Apply the native cognitive engines to support that method
4. Ensure alignment between all directions before proceeding
5. Ensure the general 360 coherence and the project-specific 360 method work together harmoniously

The model should not need to be explicitly told to use a project-specific 360 method.

It should discover it automatically and integrate it into its native thinking habits.

---

# Project-Specific 360 Method Discovery

## Automatic Detection

When the model enters a project instance layer, it must automatically check for:

- A file with "360" in the name (e.g., `13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md`)
- A file that defines a project-specific engineering method
- A file that describes a loop or cycle of connected project directions
- YAML gates that enforce project-specific 360 coherence

If such a file exists, the model must:

1. Read and understand the project-specific 360 method
2. Identify the directions it connects (e.g., documentation, translation, data, environment, platform)
3. Identify the central references it depends on (e.g., state taxonomy, event taxonomy, shared primitives)
4. Integrate this method into its native cognitive habits

## Classification

The model must classify the discovered project-specific 360 method:

- **Explicit 360 method**: A file explicitly named as a 360-degree engineering method
- **Implicit 360 method**: A file that describes a connected loop or cycle without using "360" terminology
- **Gate-based 360 method**: YAML gates that enforce coherence across multiple directions
- **Hybrid method**: A combination of explicit documentation and YAML gates

The classification determines how the model integrates it into its native habits.

---

# Integration With Native Cognitive Engines

## 1. Integration With Native 360-Degree Thinking Engine

The project-specific 360 method provides the **specific directions** to check.

The native 360-degree thinking engine provides the **automatic habit** of checking all relevant directions.

**Integration:**
- The native engine automatically asks: "What are all the directions this touches?"
- The project-specific method answers: "For this project, the directions are: documentation, translation, data, environment, platform"
- The native engine then automatically checks all these directions without needing to be explicitly told

**Example:**
When working on a Pazarat scenario, the native engine automatically considers:
- Documentation direction: Does this capture the scenario properly?
- Translation direction: Can this be translated to code without guessing?
- Data direction: Does this expose stable identities and relationships?
- Environment direction: Will this fit the accepted stack?
- Platform direction: Does this preserve platform coherence?

The model doesn't need to explicitly list these directions—the native habit makes it automatic.

## 2. Integration With Project State Awareness Engine

The project-specific 360 method may have different requirements for different project maturity levels.

The project state awareness engine automatically perceives the current maturity.

**Integration:**
- The awareness engine automatically perceives: "This is a mature project with established structure"
- The project-specific method specifies: "For mature projects, apply full 360 validation"
- The model automatically adjusts its behavior accordingly

**Example:**
In a raw idea project, the model might apply lighter 360 checks.
In a mature project like Pazarat, the model applies full 360 validation automatically.

## 3. Integration With Deep Inference Engine

The project-specific 360 method defines what connections are important.

The deep inference engine automatically perceives those connections.

**Integration:**
- The project-specific method specifies: "Order delivery completion implies notifications, audit logs, settlement"
- The deep inference engine automatically perceives these implications when working on order delivery
- The model doesn't need to be explicitly told to consider these connections

## 4. Integration With Self-Questioning Engine

The project-specific 360 method defines what questions to ask.

The self-questioning engine automatically asks those questions.

**Integration:**
- The project-specific method specifies validation questions for each direction
- The self-questioning engine automatically asks these questions before, during, and after actions
- The model doesn't need to explicitly list the validation checklist

---

# Project-Specific 360 Method Understanding

## Direction Mapping

When the model discovers a project-specific 360 method, it must map the directions:

**Example from Pazarat:**
- Direction 1: Documentation Standards
- Direction 2: Implementation Translation Standards
- Direction 3: Data/Database/API Contract Standards
- Direction 4: Engineering Environment Standards
- Direction 5: Pazarat Platform Objective

The model must understand:
- What each direction means
- What files govern each direction
- How the directions interact (rotating loop, not linear)
- What central references connect all directions

## Central Reference Identification

The model must identify the central references that the project-specific 360 method depends on:

**Example from Pazarat:**
- State taxonomy (`02_PLATFORM_STATE_TAXONOMY.md`)
- Event taxonomy (`03_PLATFORM_EVENT_TAXONOMY.md`)
- Shared primitives (`08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md`)
- Engineering environment (`14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md`)

The model must automatically check these central references before acting in any direction.

## Rotating Loop Understanding

The model must understand that project-specific 360 methods are often **rotating loops**, not linear checklists:

**Example from Pazarat:**
```
Raw Input → Scenario Maturity → Parent/Child Documentation → Central Taxonomy Alignment → Translation Contract → Engineering Environment Alignment → Code/Database/API → Validation → Feedback to Standards
```

The loop may rotate backward when implementation exposes gaps in documentation, taxonomy, or environment standards.

The native cognitive engines must support this rotating behavior automatically.

---

# Native Integration in Practice

## Example 1: Writing a Pazarat Scenario

**Without integration:**
The model might write a scenario that looks good but fails the Pazarat 360 check because it doesn't consider translation, data, or environment implications.

**With integration:**
The native 360 thinking engine automatically asks: "What directions does this touch?"
The project-specific method answers: "Documentation, translation, data, environment, platform"
The deep inference engine automatically perceives: "This scenario implies state transitions, events, database entities, API endpoints"
The self-questioning engine automatically asks: "Can this be translated to code without guessing? Does it fit the stack?"
The model produces a scenario that is already 360-aligned without needing explicit validation.

## Example 2: Generating Code for Pazarat

**Without integration:**
The model might generate code that conflicts with the engineering environment or ignores the data model standards.

**With integration:**
The native 360 thinking engine automatically considers all directions
The project state awareness engine perceives this is a mature project with strict standards
The deep inference engine perceives the implications for data, API, and environment
The self-questioning engine validates against the Pazarat engineering environment
The model produces code that is already aligned with the Pazarat 360 method

## Example 3: Working on a Project Without a Project-Specific 360 Method

**With integration:**
The model automatically detects no project-specific 360 method exists
It falls back to the general 360 coherence methods from the cognitive runtime and project orchestration layers
The native cognitive engines still apply, but without project-specific direction constraints

---

# Relation to Existing Files

This file does not replace:

- `13_COGNITIVE_360_TUNNEL_COHERENCE_METHOD.md`: General cognitive 360 method
- `20_PROJECT_ORCHESTRATION_360_ALIGNMENT_METHOD.md`: General orchestration 360 method
- Project-specific 360 methods like `13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md`

This file provides the integration layer that makes project-specific 360 methods work seamlessly with the native cognitive engines.

The general methods provide the framework.
The project-specific methods provide the specialization.
This integration engine provides the automatic connection between them.

---

# Failure Signals

When project-specific 360 integration is weak, the model may:

- fail to discover a project-specific 360 method when one exists
- apply only general 360 methods when a project-specific method should be used
- treat project-specific 360 as an explicit checklist instead of integrating it into native habits
- fail to map the directions correctly
- fail to identify central references
- treat a rotating loop as a linear checklist
- produce artifacts that pass general 360 checks but fail project-specific 360 validation

When these signals appear, the integration engine needs strengthening.

---

# Strengthening the Integration Engine

The native integration habit is strengthened by:

1. **Automatic discovery**: Always check for project-specific 360 methods when entering a project
2. **Direction mapping**: Automatically map the directions in the project-specific method
3. **Central reference identification**: Automatically identify the central references
4. **Rotating loop understanding**: Automatically understand the rotating nature of the loop
5. **Native engine integration**: Automatically apply native cognitive engines to support the project-specific method
6. **Fallback behavior**: Automatically fall back to general methods when no project-specific method exists

Over time, this becomes automatic—like how an experienced engineer automatically adapts to project-specific methods without needing explicit instructions.

---

# Final Principle

Project-specific 360 methods are not isolated protocols.

They are specialized implementations of the general 360 coherence principle.

The goal is for the model to automatically discover, understand, and apply project-specific 360 methods by integrating them into its native cognitive habits.

The native cognitive engines provide the automatic behavior.
The project-specific 360 method provides the specialization.
This integration engine provides the seamless connection between them.

This file builds that automatic integration into the cognitive runtime.
