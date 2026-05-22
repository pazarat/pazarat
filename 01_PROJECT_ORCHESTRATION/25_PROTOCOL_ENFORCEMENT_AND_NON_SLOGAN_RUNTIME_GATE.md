# PROTOCOL ENFORCEMENT AND NON-SLOGAN RUNTIME GATE

# Purpose

This gate ensures repository standards operate as enforceable task controls, not inspirational text.

A protocol is valid only when it can route behavior, constrain output, produce evidence, and detect failure.

This file is general to all projects.

---

# Core Rule

Any instruction that affects project execution must be converted into an operational gate.

A standard that only says what is important, without defining trigger, required action, evidence, validation, and failure handling, is incomplete.

---

# Protocol Completeness Test

Every binding protocol should answer:

1. When is this protocol triggered?
2. What must the model do before execution?
3. What must the model not do?
4. Which layer owns the truth?
5. What file, output, path, ledger, or report proves compliance?
6. What validation checks confirm success?
7. What failure requires stop, repair, or escalation?
8. How does this protocol connect to command boards or project-local gates?

If a protocol fails this test and the weakness affects current work, repair the owning protocol before or during the task.

---

# Required Enforcement Forms

Use one or more of these enforcement forms depending on task type:

- YAML command board gate;
- numbered Markdown standard with mandatory trigger and failure behavior;
- task execution plan;
- delivery conformance report;
- routing manifest;
- registry entry;
- traceability map;
- validation script;
- checklist with pass/fail items;
- decision record for accepted exceptions.

---

# Anti-Slogan Patterns

Repair these patterns:

- phrases such as "must be aligned" without saying how alignment is checked;
- "apply 360" without naming the surfaces to rotate through;
- "be careful" without forbidden paths or stop conditions;
- "validate" without specific checks;
- "document and code must connect" without routing or traceability files;
- "expert engineer" role without a task plan and delivery conformance gate;
- "repository integrity" without a script or manifest that can fail.

---

# Layer Enforcement

General layers own reusable behavior and enforcement mechanics.

Project-local layers own project-specific truth, stack, routes, domains, and artifact ownership.

If a project-specific example is needed to explain a general rule, abstract it or move it to the project instance layer.

---

# Runtime Behavior

When the model detects that a request exposes a gap between a written standard and enforceable behavior, it must classify the gap as one of:

- missing command-board gate;
- missing task plan;
- missing routing/traceability;
- missing validation script;
- project-local standard gap;
- misplaced project-specific truth;
- ambiguous ownership;
- incomplete delivery conformance.

Then it must repair the smallest correct owner.

---

# Delivery Rule

For any generated artifact or repository output, the model must not present the output as fully successful unless there is evidence of enforcement:

- a plan exists;
- a topology or artifact contract exists when relevant;
- validations ran or limitations are stated;
- delivery conformance was checked.

This rule is binding. It is not style guidance.
