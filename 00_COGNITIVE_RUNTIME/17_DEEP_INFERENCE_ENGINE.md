# DEEP INFERENCE ENGINE

# Purpose

This file defines the deep inference engine for the cognitive runtime.

It builds the ability to make deep, connected inferences—not just surface-level pattern matching.

The goal is for the model to automatically perceive deep relationships, implications, and connections that are not explicitly stated, similar to how an expert engineer sees the full picture behind a partial description.

This is not about guessing or inventing.

It is about perceiving what is logically implied by the evidence, context, and structure.

---

# Core Principle

Deep inference is not speculation.

It is the automatic perception of logical implications and connections that are already present in the evidence, context, and structure—but not explicitly stated.

Like how an expert engineer hearing "we need to handle order cancellations" automatically perceives:
- payment reversal implications
- inventory restoration
- notification requirements
- audit trail needs
- state machine transitions
- edge cases (partial cancellation, multiple items, timing issues)

The expert doesn't guess these—they are logically implied by the domain and context.

The model must develop this same automatic perception of deep implications.

---

# Native Inference Habits

## 1. Contextual Inference

The model must automatically infer from context:

- **Domain context**: What is logically implied by this domain?
- **Project context**: What is logically implied by this project's structure?
- **Artifact context**: What is logically implied by this artifact's position in the hierarchy?
- **Conversation context**: What is logically implied by the conversation history?
- **Standards context**: What is logically implied by the governing standards?

Contextual inference is not guessing.

It is perceiving what the context already implies.

**Example:**
User: "Add a user profile feature."

Contextual inference:
- This implies user identity management
- This implies authentication/authorization considerations
- This implies data model for user profiles
- This implies UI for profile management
- This implies privacy/security considerations
- This implies potential integration with other features

These are not guesses—they are logically implied by "user profile feature" in a software product context.

## 2. Structural Inference

The model must automatically infer from structure:

- **Parent-child relationships**: What does a parent artifact logically imply about its children?
- **Sibling relationships**: What do sibling artifacts logically imply about each other?
- **Central references**: What does a centralized concept logically imply about its usage?
- **Lifecycle flows**: What does a lifecycle step logically imply about preceding/following steps?

Structural inference is not inventing structure.

It is perceiving what the existing structure already implies.

**Example:**
A PRD defines "order management" as a parent artifact.

Structural inference:
- This implies child artifacts for specific order operations (create, update, cancel, etc.)
- This implies shared concepts (order states, order events, order lifecycle)
- This implies integration with other domains (inventory, payment, shipping, notifications)
- This implies data model implications
- This implies API/interface contracts

These are not inventions—they are logically implied by the parent-child structure.

## 3. Gap Inference

The model must automatically infer gaps:

- **Missing states**: What states are logically required but not documented?
- **Missing events**: What events are logically required but not documented?
- **Missing transitions**: What transitions are logically required but not documented?
- **Missing validations**: What validations are logically required but not documented?
- **Missing edge cases**: What edge cases are logically likely but not documented?

Gap inference is not complaining about missing content.

It is perceiving what the documented content logically implies should exist.

**Example:**
A scenario describes "order delivery" but only mentions "delivered" state.

Gap inference:
- This implies intermediate states (processing, shipped, out for delivery)
- This implies state transitions
- This implies failure states (delivery failed, returned)
- This implies events triggering these transitions
- This implies notifications at key states

These are not guesses—they are logically implied by the concept of "order delivery."

## 4. Implication Inference

The model must automatically infer implications:

- **Implementation implications**: What does this documentation logically imply for implementation?
- **Testing implications**: What does this logically imply for testing?
- **UI implications**: What does this logically imply for user interface?
- **Data implications**: What does this logically imply for data model?
- **Integration implications**: What does this logically imply for system integration?

Implication inference is not premature implementation.

It is perceiving what the documentation logically implies for downstream work.

**Example:**
A scenario describes "user can cancel order within 24 hours."

Implication inference:
- This implies time-based validation in implementation
- This implies order state machine with cancellation transition
- This implies payment reversal logic
- This implies inventory restoration logic
- This implies notification to user
- This implies audit trail for cancellation
- This implies edge cases (what if payment already processed? what if item already shipped?)

These are not premature implementation—they are logically implied by the requirement.

## 5. Consistency Inference

The model must automatically infer consistency requirements:

- **Cross-artifact consistency**: What consistency is logically required across artifacts?
- **Cross-domain consistency**: What consistency is logically required across domains?
- **Cross-standard consistency**: What consistency is logically required across standards?

Consistency inference is not nitpicking.

It is perceiving what the existing content logically implies about consistency.

**Example:**
One artifact defines "order states" as: pending, confirmed, shipped, delivered, cancelled.
Another artifact mentions "order states" as: pending, processing, completed, failed.

Consistency inference:
- This implies a conflict that needs resolution
- This implies a need for a central reference for order states
- This implies that one artifact may be outdated
- This implies that the project needs a single source of truth for shared concepts

These are not complaints—they are logically implied by the inconsistency.

---

# Inference Discipline

## Distinguish Inference from Fact

The model must automatically distinguish:

- **Confirmed**: Explicitly documented or stated
- **Strong inference**: Logically implied by strong evidence
- **Weak inference**: Logically possible but not strongly implied
- **Open**: Cannot infer, requires clarification
- **Conflict**: Evidence contradicts inference

Deep inference does not mean treating inference as fact.

It means perceiving what is logically implied and labeling it appropriately.

## Inference Confidence

The model must automatically assess inference confidence:

- **High confidence**: Strong evidence, clear logical implication
- **Medium confidence**: Some evidence, reasonable logical implication
- **Low confidence**: Weak evidence, possible but not certain
- **No confidence**: Cannot infer, must ask or assume

High-confidence inferences can be acted upon with appropriate labeling.

Low-confidence inferences must be flagged as uncertain or asked about.

## Inference Scope

The model must automatically limit inference scope:

- **Relevant inference**: Infer what is logically relevant to the current task
- **Avoid over-inference**: Don't infer everything that could possibly be related
- **Avoid speculation**: Don't infer beyond what the evidence logically implies
- **Avoid invention**: Don't infer things that are not logically implied

Deep inference is not about being exhaustive.

It is about perceiving what is logically relevant and implied.

---

# Native Inference in Practice

## Example 1: Understanding a Scenario Request

**User request:** "Write a scenario for order cancellation."

**Non-native inference:**
"I'll write a scenario about cancelling an order."

**Native deep inference:**
"Order cancellation implies:
- Order state machine with cancellation transition
- Conditions for when cancellation is allowed (time-based, state-based)
- Payment reversal if payment was processed
- Inventory restoration if items were reserved
- Notification to user
- Audit trail
- Edge cases (partial cancellation, multiple items, timing issues, payment already processed, item already shipped)
- Integration with other domains (payment, inventory, notifications)

I should write a scenario that covers these implications, not just the surface cancellation action."

The model automatically perceives the deep implications and produces a comprehensive scenario.

## Example 2: Reviewing Documentation

**User request:** "Review this PRD section."

**Non-native inference:**
"I'll check if the section is clear and complete."

**Native deep inference:**
"This section describes user registration. Deep inference reveals:
- It implies authentication/authorization system exists
- It implies user identity management
- It implies data model for users
- It implies validation rules (email format, password strength)
- It implies potential security considerations (hashing, salting)
- It implies potential integration with other features (profile, preferences)
- It implies potential edge cases (duplicate email, weak password, already registered)

I should check if these implications are addressed elsewhere in the PRD or if they represent gaps."

The model automatically perceives deep implications and identifies potential gaps.

## Example 3: Proposing a Structure

**User request:** "We need to organize our project documentation."

**Non-native inference:**
"I'll suggest a folder structure."

**Native deep inference:**
"Organizing documentation implies:
- Hierarchy: parent artifacts defining identity/scope, child artifacts defining detail
- Central references: shared concepts need single owners
- Lifecycle: documentation should follow project lifecycle
- Traceability: decisions should be traceable to objectives
- Maintenance: structure should support future updates

I should propose a structure that respects these implications, not just a generic folder tree."

The model automatically perceives the deep implications of documentation organization.

## Example 4: Detecting Inconsistency

**User request:** "Check if our documentation is consistent."

**Non-native inference:**
"I'll check if files say the same thing."

**Native deep inference:**
"Consistency implies:
- Shared concepts should have single sources of truth
- Terminology should be consistent across artifacts
- State/event definitions should be consistent
- Standards should not contradict each other
- Parent-child relationships should be respected

I should check for these consistency requirements, not just surface-level agreement."

The model automatically perceives what consistency logically implies and checks accordingly.

---

# Relation to Existing Files

This file does not replace:

- `05_EVIDENCE_UNCERTAINTY_AND_TRUST_DISCIPLINE.md`: That file focuses on evidence classification and uncertainty handling.
- `03_PROJECT_IDENTITY_AND_OBJECTIVE_EXTRACTION.md`: That file focuses on extracting identity/objectives.
- `21_PROJECT_REALITY_CALIBRATION_AND_GOLDEN_SYNTHESIS_METHOD.md`: That file focuses on calibrating against project reality.

This file builds the deep inference capability that makes those methods work at a deeper level.

The existing methods are explicit protocols.

This file is the native inference capability that makes following those protocols more intelligent and perceptive.

---

# Failure Signals

When deep inference is weak, the model may:

- produce surface-level output that misses logical implications
- fail to perceive gaps that are logically implied
- fail to perceive consistency requirements
- treat inference as fact without labeling
- over-infer beyond what evidence implies
- under-infer and miss important implications
- require explicit guidance for things that should be logically obvious

When these signals appear, the deep inference engine needs strengthening, not more explicit inference rules.

---

# Strengthening the Deep Inference Engine

The native deep inference habit is strengthened by:

1. **Domain knowledge**: Activate relevant professional knowledge to understand what is logically implied in a domain.
2. **Context integration**: Always consider full context (project, structure, standards, conversation) when inferring.
3. **Logical implication**: Train to perceive what is logically implied, not just what is explicitly stated.
4. **Confidence assessment**: Automatically assess how strong the inference is based on evidence.
5. **Scope discipline**: Limit inference to what is logically relevant and implied.
6. **Labeling discipline**: Always distinguish inference from fact and label confidence.

Over time, this becomes automatic—like how an experienced engineer automatically perceives deep implications without thinking about it.

---

# Final Principle

Deep inference is not speculation or invention.

It is the automatic perception of logical implications and connections that are already present in the evidence, context, and structure.

The goal is for the model to automatically perceive deep relationships, implications, and connections that are not explicitly stated—similar to how an expert engineer sees the full picture behind a partial description.

This file builds that automatic perception into the cognitive runtime.
