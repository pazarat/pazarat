# v6.10 Runtime Integrity Notes

This release strengthens the engineer runtime itself, not only project answers.

Key changes:
- tool_registry.yaml is treated as a runtime contract and must match the CLI commands.
- doctor includes runtime integrity checks.
- runtime-audit checks command registry, volatile generated outputs, and static project-term leaks.
- generated indexes/ledgers are considered volatile session products, not static engineer memory.
- project-specific material remains valid only inside ACTIVE_PROJECT or volatile generated outputs.

Purpose: prevent the framework from having strong governance for projects but weak governance for its own runtime.
