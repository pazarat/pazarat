# Jet File Matrix Implementation v8.1

This layer implements the first executable File Matrix Kernel above the V8 architecture overlay.

## Implemented commands

- `file-matrix-build`: builds local SQLite/FTS file intelligence index.
- `file-matrix-touch`: returns a whole-project neural surface.
- `file-matrix-query`: runs multi-lens retrieval.
- `file-matrix-context`: produces the model handoff packet with targeted reads.
- `file-matrix-doctor`: checks health, freshness, FTS, latency, discovery, and tools.
- `file-matrix-status`: returns freshness without rebuild.

## Implemented engines

- Auto Discovery Engine
- File Inventory Engine
- Local SQLite Store
- SQLite FTS text lens
- Path/term/symbol/relation lenses
- Markdown heading symbol extraction
- Code symbol extraction by broad language regexes
- API/route and SQL/schema signal extraction
- Freshness fingerprint manager
- Query planner and context-pack builder
- File Matrix Doctor

## Extension points retained

- Tree-sitter AST adapter
- LSP bridge
- semantic vector index
- graph backend
- framework-specific extractors
- post-write validation adapters

## Source-of-truth boundary

The generated matrix is a navigation and acceleration surface. It does not override current files and cannot be the sole basis for high-impact claims or writes.
