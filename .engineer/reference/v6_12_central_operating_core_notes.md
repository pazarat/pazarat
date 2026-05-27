# v6.12 Central Operating Core Notes

v6.12 matures the runtime from tool collection to mandatory operating core.

Implemented:

- `plug` command as one-touch entry.
- `cycle` delegates to `plug`.
- richer `matrix` output with concept buckets and mandatory reads.
- central governance file for plug/matrix/receipt semantics.
- updated tool contract, registry, manifest, and navigation triggers.
- tests for central plug behavior.

Design rule:

The one-touch output is not a passive report. It is the operating context the model must follow for the current request.
