# V8 Implementation Roadmap

Status: staged non-destructive plan  
Purpose: upgrade the runtime without losing V7 governance or workshop philosophy.

---

## Stage 0 — Preserve

Actions:

- do not delete V7 files,
- do not rewrite governance principles,
- keep workshop boundary,
- keep active project truth boundary,
- keep runtime neutrality tests,
- add V8 as architecture overlay.

Exit criteria:

```text
V7 doctor passes
runtime index fresh
no active-project term is hardcoded into new runtime architecture
```

---

## Stage 1 — File Matrix Kernel specification

Actions:

- define File Matrix contracts,
- define storage schema,
- define search lenses,
- define freshness rules,
- define file-matrix doctor.

Exit criteria:

```text
file-matrix enter/query/doctor contracts exist
all cache outputs have metadata requirements
all write operations route through impact gate
```

---

## Stage 2 — Tool Control Center upgrade

Actions:

- split tool registry into typed contracts,
- add adapter interfaces,
- add tool-doctor,
- ensure Entry Gate returns operation-specific tool keyboard.

Exit criteria:

```text
all tools have risk/mutation/scope/pre/post metadata
doctor verifies registry-callable sync
```

---

## Stage 3 — Strategy Kernel

Actions:

- add problem framing contract,
- add root-cause classifier,
- add anti-patching gate,
- add best-fit comparator output format,
- add decision-record contract.

Exit criteria:

```text
runtime can distinguish patch vs repair vs local-standard need
execution cannot proceed without acceptance criteria for high-impact work
```

---

## Stage 4 — Code Intelligence adapters

Actions:

- add AST adapter,
- add language-server adapter contract,
- add symbol/reference index,
- add dependency graph tables,
- add test/build/lint discovery.

Exit criteria:

```text
software projects activate code lenses automatically
non-software projects do not receive software assumptions
```

---

## Stage 5 — Evaluation and self-maintenance

Actions:

- add file-matrix-doctor,
- add strategy-doctor,
- add behavioral evaluation suite,
- add runtime upgrade receipts,
- add performance/latency metrics.

Exit criteria:

```text
runtime can inspect its own search/matrix/strategy health
behavioral tests catch direct-answer, patching, no-evidence, and runtime leakage failures
```

---

## Stage 6 — Integration hardening

Actions:

- connect Entry Gate to File Matrix and Strategy Kernel,
- ensure compact operating packets,
- keep deep reads only for high-impact work,
- add regression suite for active-project empty/non-empty states.

Exit criteria:

```text
model enters through one operating packet
packet includes boundary awareness, tool keyboard, evidence requirements, and next gate
```

