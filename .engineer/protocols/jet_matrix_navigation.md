# Jet Matrix Navigation Protocol — v6.12

Jet matrix navigation exists to make a bounded, high-signal scan fast and compulsory.
It does not replace reading; it tells the engineer what to read first and what risks to avoid.

## Buckets

- truth_and_contracts
- requirements_and_prd
- scenarios_and_workflows
- states_and_events
- permissions_and_audit
- data_api_execution
- risks_and_decisions
- writing_and_content
- research_and_external

## Bucket semantics

A bucket hit means: “this file may own or constrain this concept.”
It does not mean: “this is proven final truth.”

## Required behavior

- Read owner/truth files before local details.
- Use project-neutral buckets; never assume software unless software evidence exists.
- If a relevant bucket is empty, do a zero-result scan before saying it does not exist.
- For a write, update owner files when appropriate and avoid parallel concept creation.
