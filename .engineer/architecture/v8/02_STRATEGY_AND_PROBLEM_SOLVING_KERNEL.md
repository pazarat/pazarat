# V8 Strategy & Problem-Solving Kernel

Status: required V8 kernel  
Purpose: prevent random solutions, patching loops, and generic advice by forcing a disciplined engineering method before execution.

---

## 1. Why this kernel is required

File intelligence can tell the model where things are. It does not by itself teach the model how to solve problems well.

The Strategy Kernel gives the model a controlled method for:

- understanding intent,
- framing the problem,
- detecting root cause,
- comparing solution paths,
- selecting best fit,
- defining acceptance criteria,
- refusing patching when the cause is architectural,
- validating whether the result solved the cause or only the symptom.

---

## 2. Strategy stack

```text
Strategy & Problem-Solving Kernel
│
├─ Intent Understanding Engine
├─ Problem Framing Engine
├─ Reality Mapping Engine
├─ Root Cause Engine
├─ Option Generation Engine
├─ Best-Fit Comparator
├─ Anti-Patching Gate
├─ Acceptance Criteria Engine
├─ Execution Playbook Selector
├─ Decision Record Engine
└─ Post-Action Review Engine
```

---

## 3. Intent Understanding Engine

Extracts:

```text
user goal
operation type
expected output
scope
urgency
risk level
implicit constraints
whether the request targets runtime, workshop, or active project
```

Hard rule: runtime, workshop, and active project must never be confused.

---

## 4. Problem Framing Engine

Before solving, it produces a frame:

```text
what is the observed issue?
what is the desired state?
what evidence exists?
what is unknown?
what is the impacted lifecycle area?
what would count as success?
```

---

## 5. Reality Mapping Engine

Maps the current project/runtime reality using File Matrix and Workshop lenses.

It separates:

```text
observed facts
inferred gaps
assumptions
user preferences
external practices
local project truth
```

---

## 6. Root Cause Engine

Prevents symptom-level work.

Classification types:

```text
missing truth
thin owner file
duplicated concept
weak standard
broken navigation
missing validation
incomplete implementation contract
architecture mismatch
tooling gap
runtime coupling
project-local decision needed
```

---

## 7. Option Generation Engine

Generates multiple valid paths when the problem is not trivial.

Each option must include:

```text
owner file
required evidence
risk
impact surface
validation method
why this is or is not best fit
```

---

## 8. Best-Fit Comparator

Chooses based on project reality, not generic ideals.

Comparison axes:

```text
fit to active project truth
fit to workshop maturity rules
fit to scale
fit to lifecycle risk
fit to maintainability
fit to testability
fit to existing architecture
migration cost
risk if ignored
```

---

## 9. Anti-Patching Gate

Blocks patching when:

- the cause is missing source truth,
- multiple files disagree,
- an owner file is thin,
- the requested edit creates parallel logic,
- validation cannot prove correctness,
- a local standard is missing,
- the model has only a symptom and no cause.

Output states:

```text
patch_allowed
repair_owner_first
design_decision_required
local_standard_required
deep_scan_required
execution_blocked
```

---

## 10. Acceptance Criteria Engine

Every execution plan must define acceptance criteria before implementation.

Examples:

```text
which files must change?
which files must not change?
which tests must pass?
which contradiction must disappear?
which claim must become evidence-backed?
which runtime command must pass?
```

---

## 11. Execution Playbook Selector

Selects a playbook based on operation type.

Required playbooks:

```text
runtime improvement
project formation
project assessment
new feature
bug repair
refactor
architecture repair
PRD maturation
implementation translation
migration
security review
performance review
documentation reconciliation
codebase onboarding
post-change validation
```

---

## 12. Decision Record Engine

Any non-trivial strategy choice creates a decision packet:

```text
decision
options considered
selected option
reason
rejected options
source evidence
risks
validation gate
future revisit condition
```

---

## 13. Post-Action Review Engine

After action, it checks:

```text
did we solve the root cause?
did we introduce duplication?
did validation pass?
did we update the correct owner?
did the runtime learn anything?
was a follow-up gate required?
```

