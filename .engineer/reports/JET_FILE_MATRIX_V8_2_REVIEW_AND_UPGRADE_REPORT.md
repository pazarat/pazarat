# Jet File Matrix v8.2 Review and Upgrade Report

## Verdict
v8.1 implemented a real local file-matrix kernel, but it did not yet satisfy every ambition discussed in the conversation. It provided inventory, SQLite FTS, broad symbol extraction, relation hints, freshness, context packs, and doctor checks. It did not yet provide true AST/LSP, dense semantic vectors, ripgrep as an active retrieval lens, deep chunk retrieval, or resolved import/reference graphing.

v8.2 strengthens the executable center without replacing the governance core.

## Conversation requirements checked

| Requirement | v8.1 state | v8.2 state |
|---|---:|---:|
| Mandatory file entry gate for model | present | strengthened through contract and plug guidance |
| Local fast index | present | strengthened with schema v2 and composite scope/path keys |
| Auto discovery | present | broadened framework/language markers |
| Fast text search | SQLite FTS present | SQLite FTS + active ripgrep lens |
| One-page neural surface | present | preserved |
| Chunk-level retrieval | missing | added chunks + chunk FTS |
| Semantic search | not real vector; only terms/signals | semantic-lite chunks added; dense vectors remain adapter extension |
| Code language coverage | partial | broadened language/file detection and symbol patterns |
| Symbol extraction | partial regex | broadened parser patterns and normalized symbols |
| Import/dependency resolution | shallow target only | target_path resolver added for local imports where possible |
| Symbol reference graph | missing | added symbol_reference relation pass |
| Incoming/outgoing graph neighbors | outgoing only | incoming + outgoing graph expansion |
| Cache/freshness discipline | present | preserved with schema migration |
| Doctor | present | preserved and now validates richer index state |
| AST/LSP | not implemented | still extension adapters; not bundled as hard dependencies |
| Dense semantic vectors | not implemented | still extension adapter; semantic-lite provided locally |

## Honest boundary
v8.2 is much stronger, but it is not yet a full IDE-grade engine. A fully maximal version still requires optional adapters:

1. Tree-sitter for real AST across languages.
2. LSP bridge for go-to-definition, references, diagnostics, and types.
3. Dense embedding/vector store for true semantic retrieval.
4. Framework-specific extractors for Next/Nest/Laravel/Django/Prisma/etc.
5. A graph backend if the project becomes very large.

The architecture now supports these without redesigning the center.

## Implementation changes

- Version bumped to `8.2.0`.
- File Matrix schema bumped to `2` with disposable generated-state migration.
- Added `chunks` and `chunk_fts` for focused retrieval.
- Added active `ripgrep` lens when `rg` is available.
- Added semantic-lite chunk lens based on terms/signals/chunk FTS.
- Added broader file extension and language recognition.
- Added broader symbol extraction for JS/TS, Python, Go, Rust, PHP, Ruby, Java/C#, Kotlin, Swift, GraphQL, Protobuf, Prisma, SQL, framework route decorators.
- Added local import target resolution where possible.
- Added symbol-reference relation pass.
- Added incoming and outgoing graph neighbor expansion.
- Updated `file_matrix_contract.yaml` to reflect v8.2 capabilities and honest extension boundaries.

## Non-breaking rule
No governance core files were removed. v8.2 upgrades the executable file-matrix body while preserving the old philosophy: files remain source of truth; generated state is acceleration only.
