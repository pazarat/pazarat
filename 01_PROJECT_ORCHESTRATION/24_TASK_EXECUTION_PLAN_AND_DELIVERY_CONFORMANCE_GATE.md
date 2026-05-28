# TASK EXECUTION PLAN AND DELIVERY CONFORMANCE GATE

# Purpose

This gate converts project-orchestration guidance into an enforceable execution protocol.

It prevents the model from treating standards as reading material only. For any meaningful project task, the model must establish a task plan, execute against it, and verify the delivered result against the plan before final delivery.

This is a general project-orchestration rule. It must not contain project names, project-specific stacks, or product-specific business logic.

---

# Core Rule

No meaningful project task may be delivered as final output unless the model has completed a task execution cycle.

The cycle is:

1. classify the task;
2. establish the task execution plan;
3. define expected outputs and affected surfaces;
4. define validation gates and stop conditions;
5. execute only the planned safe operation;
6. verify produced output against the plan;
7. produce or summarize a delivery conformance result.

For trivial answers, the plan may remain internal and minimal. For repository changes, generated ZIPs, code changes, documentation migrations, large audits, or multi-file outputs, the plan must be materialized as a file, ledger entry, manifest, or explicit delivery report.

---

# Trigger

Activate this gate when the task involves any of the following:

- repository, ZIP, codebase, folder structure, or file generation;
- documentation creation, migration, repair, or standard update;
- code, database, frontend, backend, infrastructure, tests, or scripts;
- audit, diagnosis, comparison, refactoring, validation, or repair;
- project strategy that affects future execution;
- user reports that a prior result was not aligned with intent;
- any work that spans more than one artifact or layer.

---

# Mandatory Task Plan Fields

Before execution, the model must know:

- task id or short task label;
- user goal in preserved form;
- task type;
- active project or artifact boundary;
- baseline source;
- required outputs;
- affected paths or artifact families;
- forbidden paths or forbidden behaviors;
- governing protocols or standards;
- assumptions and open decisions;
- validation checks;
- completion definition;
- delivery format.

The plan may be internal for small conversational work, but must be written to the repository or final report for non-trivial repository/artifact generation.

---

# Execution Rules

The model must:

1. execute against the plan rather than against a vague intent;
2. preserve the baseline unless the task explicitly requests replacement;
3. update the smallest correct owner;
4. avoid adding explanatory files when a binding gate or routing file is the correct repair;
5. keep project-specific truth out of general layers;
6. keep general method out of project product documentation;
7. update routing, registries, traceability, or ledgers when they are the owner of continuity;
8. stop or report partial completion when validation fails.

---

# Delivery Conformance Gate

Before final delivery, compare the output against the plan:

- required outputs created or intentionally deferred;
- affected paths changed as planned;
- forbidden paths absent;
- standards and gates applied;
- validation checks run;
- failures, limitations, or unknowns disclosed;
- next unsafe action not silently performed.

The final answer must not claim success unless the conformance result supports it.

---

# Stop Conditions

Stop and repair, ask the smallest necessary question, or deliver a partial diagnostic when:

- actual project boundary is unclear;
- baseline source is unclear;
- topology contract cannot be established;
- a required file cannot be inspected;
- validation detects broken entry routes, duplicated truth, forbidden paths, or missing routing;
- the generated artifact cannot be verified;
- the model cannot prove that required outputs match the plan.

---

# Minimal Visible Reporting

For non-trivial deliverables, the final response should include a concise delivery conformance summary:

- what was planned;
- what was changed or produced;
- what was verified;
- what remains limited or unverified.

Do not replace actual validation with persuasive wording.
