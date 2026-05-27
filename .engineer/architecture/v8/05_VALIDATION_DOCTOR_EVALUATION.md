# V8 Validation, Doctor, and Evaluation Harness

Status: required V8 quality layer  
Purpose: prove that the runtime and project work remain correct after changes.

---

## 1. Validation families

```text
Project Validation
Runtime Validation
File Matrix Validation
Strategy Validation
Tool Registry Validation
Governance Validation
Security Validation
Regression Evaluation
```

---

## 2. Project validation

Activated after project changes.

Checks may include:

```text
lint
typecheck
test
build
schema validation
API contract validation
migration validation
duplicate rescan
impact rescan
documentation drift
claim check
```

The exact set is discovered from the active project profile.

---

## 3. Runtime validation

Activated after engineer-runtime changes.

Required checks:

```text
doctor
runtime-audit
tool registry sync
kernel index freshness
runtime neutrality scan
generated cache metadata check
golden behavioral suite
maintenance ledger update
```

---

## 4. File Matrix doctor

Checks:

```text
discovery works
inventory fresh
indexes fresh
search lenses callable
relationship graph available
code intelligence adapters available when relevant
cache freshness states valid
query latency within expected range
write impact gate connected
validation bridge connected
```

---

## 5. Strategy doctor

Checks whether the model/runtime followed the problem-solving discipline:

```text
intent understood
problem framed
root cause classified
options considered when needed
best-fit chosen with reasons
anti-patching gate applied
acceptance criteria defined
post-action review created
```

---

## 6. Evaluation harness

The runtime must include behavioral tests, not only file tests.

Required scenarios:

```text
project-surface identity
empty project formation
runtime improvement request
write request with duplicate risk
implementation from thin PRD
codebase onboarding
stale cache detection
unsupported absence claim
best-fit architecture repair
post-change validation
```

Each scenario defines:

```text
input prompt
required tools/gates
forbidden behavior
expected evidence state
maximum acceptable leakage
pass/fail rule
```

