# V8 Tool Control Center and Adapter Layer

Status: required V8 infrastructure  
Purpose: ensure the model sees tools as a controlled operating keyboard, not as scattered commands it may forget.

---

## 1. Tool Control Center

The Tool Control Center is the runtime's tool registry, dispatcher, and safety policy.

It stores:

```text
tool id
command/API endpoint
purpose
input contract
output contract
risk level
mutates filesystem?
default mode: read-only / dry-run / apply
allowed scopes
required preconditions
required postconditions
related gates
failure handling
```

---

## 2. Tool keyboard returned to model

The Entry Gate must return a compact tool keyboard for each operation.

Example:

```text
For runtime improvement:
- route
- plug-fast/runtime
- file-matrix query runtime
- impact-scan runtime
- write-plan
- doctor
- runtime-audit
- golden-suite
- maintenance receipt
```

The model should not need to remember every tool. The operating packet supplies the right subset.

---

## 3. Adapter types

Required adapters:

```text
FileSystemAdapter
TextSearchAdapter
SemanticSearchAdapter
ASTAdapter
LSPAdapter
GraphAdapter
GitAdapter
ValidationAdapter
FrameworkAdapter
DatabaseAdapter
SecurityAdapter
ReceiptAdapter
```

Adapters prevent the architecture from depending directly on one implementation.

---

## 4. Safety defaults

1. Read-only by default.
2. Dry-run before apply.
3. Write scope must be explicit.
4. Generated outputs must be marked generated.
5. Project files and runtime files must never be confused.
6. Destructive operations require explicit apply gates.
7. Any tool failure must produce a typed failure packet, not silent fallback.

---

## 5. Tool doctor

`tool-doctor` must check:

- registry entries match callable commands,
- command signatures match contracts,
- generated outputs have metadata,
- mutating tools default to dry-run,
- scope boundaries are enforced,
- tool outputs are parseable,
- runtime commands do not contain active-project coupling.

