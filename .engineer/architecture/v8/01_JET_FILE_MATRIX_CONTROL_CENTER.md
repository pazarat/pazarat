# V8 Jet File Matrix Control Center

Status: required V8 kernel  
Purpose: give the model fast, controlled, project-neutral access to complex file trees without relying on manual maps or random search.

---

## 1. Core principle

The model must not enter the active project directly.

It enters the File Matrix through a control center that returns an operating packet:

```text
operation type
scope
project profile
freshness status
available indexes
selected lenses
owner candidates
related files
risk gates
required validations
```

The File Matrix is not a single search command. It is a multi-engine file intelligence kernel.

---

## 2. Full layer map

```text
Jet File Matrix Control Center
│
├─ Entry Adapter
├─ Query / Intent Planner
├─ Auto Discovery Engine
├─ File Inventory Engine
├─ Multi-Index Layer
├─ Search Lenses Layer
├─ Code Intelligence Layer
├─ Relationship Graph Engine
├─ Context Pack Builder
├─ Cache & Freshness Manager
├─ Change Tracker
├─ Write Impact Gate
├─ Validation Bridge
├─ Storage Layer
└─ Tool Adapters
```

---

## 3. Auto Discovery Engine

Discovers the active project without a hand-written tree.

Detects:

- project type,
- languages,
- frameworks,
- package managers,
- build tools,
- test runners,
- database tools,
- API contracts,
- generated/vendor folders,
- entrypoints,
- configuration roots.

Examples of signals:

```text
package.json       → Node/JavaScript/TypeScript ecosystem
pyproject.toml     → Python ecosystem
Cargo.toml         → Rust ecosystem
go.mod             → Go ecosystem
composer.json      → PHP ecosystem
prisma/schema      → Prisma data layer
docker-compose     → service topology
openapi.yaml       → API contract
```

Output: `Project Profile`.

---

## 4. File Inventory Engine

Creates a local, generated inventory of all relevant files.

Each file entry stores:

```text
path
extension
size
mtime
hash
language
role
status
is_source
is_test
is_config
is_contract
is_generated
is_vendor
is_binary
is_large
sensitivity_candidate
```

This makes repeated scans fast and makes change detection possible.

---

## 5. Multi-Index Layer

Required indexes:

1. Path Index — names and locations.
2. Text Index — fast full-text / regex search.
3. Semantic Index — concept-level retrieval.
4. Symbol Index — functions, classes, interfaces, imports, exports.
5. Structure Index — folders, domains, modules, ownership candidates.
6. Config Index — runtime/build/env/config contracts.
7. Test Index — tests mapped to implementation surfaces.
8. Change Index — changed files and invalidated regions.
9. Governance Index — source-truth, standards, policies, gates.
10. Runtime Index — engineer environment files and tool contracts.

Indexes are generated artifacts, not truth.

---

## 6. Search Lenses

The matrix must support multiple search lenses because file work is not one kind of search.

Required lenses:

| Lens | Purpose |
|---|---|
| Filename Lens | likely paths and modules |
| Text Lens | exact text / phrase search |
| Regex Lens | structured pattern matching |
| Semantic Lens | meaning-based retrieval |
| Symbol Lens | definitions, declarations, exports |
| Reference Lens | usages and callers |
| Dependency Lens | imports, dependents, parents |
| Config Lens | configuration and environment impact |
| API Lens | routes, endpoints, contracts |
| Database Lens | schema, migrations, models, queries |
| Event Lens | events, listeners, jobs, queues |
| Permission Lens | roles, policies, guards, access |
| Test Lens | related tests and coverage candidates |
| Change Lens | diffs and modified surfaces |
| Governance Lens | standards and source-truth constraints |

The Query Planner chooses lenses automatically by operation type.

---

## 7. Code Intelligence Layer

For software projects, file search must upgrade into code intelligence.

Required capabilities:

- AST parsing,
- symbol extraction,
- import/export graph,
- route extraction,
- schema extraction,
- call graph candidates,
- language-server bridge,
- static diagnostics,
- test runner integration.

Preferred adapters:

```text
tree-sitter        → AST parsing
ripgrep            → fast text search
language servers   → definition/reference/diagnostics
framework extractors → routes, ORM schemas, migrations
static analyzers   → lint/type/test/build signals
```

---

## 8. Relationship Graph Engine

The graph connects facts across files.

Graph edge types:

```text
file imports file
file defines symbol
symbol references symbol
route handled_by function
handler calls service
service uses repository
repository touches schema
module governed_by standard
artifact has_child artifact
requirement covered_by test
change impacts dependent
```

The graph is the main anti-randomness layer: it lets the model see relationships, not just files.

---

## 9. Cache and Freshness Manager

Cache is allowed only as navigation memory.

Every generated cache/index entry must include:

```text
scope
source files
file hashes
content fingerprint
generated_at
tool version
index version
freshness state
invalidation reason
```

Freshness states:

```text
fresh
partial
stale
invalid
requires_rebuild
```

If a related source file changes, the affected index region is invalidated.

---

## 10. Write Impact Gate

Before any write:

```text
duplicate scan
owner detection
impact scan
relationship graph query
truth maturity check
write-plan
safe-write dry run
validation plan
```

A write is not valid because a model can produce code. It is valid only when the write fits the project graph and passes validation.

---

## 11. Storage policy

Storage is local runtime state, not an external project dependency.

Recommended levels:

```text
JSONL         → receipts and ledgers
SQLite        → inventory, symbols, relationships, freshness
ripgrep       → direct fast text search
Vector store  → semantic index when needed
Graph store   → optional when relationships exceed SQLite graph tables
```

The architecture must use storage adapters so backends can evolve without changing the control center.

---

## 12. Required commands / tool contracts

Minimum command family:

```text
file-matrix enter
file-matrix discover
file-matrix inventory
file-matrix index
file-matrix query
file-matrix lenses
file-matrix graph
file-matrix impact
file-matrix context-pack
file-matrix freshness
file-matrix doctor
file-matrix validate-change
```

These may be exposed as CLI commands, MCP tools, or local APIs.

---

## 13. Doctor requirements

`file-matrix-doctor` must check:

- inventory freshness,
- index freshness,
- broken file references,
- ignored folder correctness,
- generated cache metadata,
- relationship graph availability,
- AST parser availability,
- LSP adapter availability when applicable,
- query latency budget,
- write gate integration,
- validation bridge integration.

