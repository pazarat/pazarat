# PAZARAT TASK EXECUTION AND DELIVERY CONFORMANCE STANDARD

# Purpose

This standard makes every meaningful Pazarat task executable, traceable, and verifiable before delivery.

Pazarat is not managed by narrative confidence. It is managed through a task plan, affected-path map, routing map, execution evidence, validation, and delivery conformance.

---

# Binding Rule

Any task that changes or generates Pazarat documentation, backend, frontend, database, infrastructure, scripts, tests, routing, registries, or tunnel standards must pass through the Pazarat task execution cycle.

The cycle is mandatory:

1. create or update a task plan;
2. identify the actual Pazarat project boundary;
3. identify affected docs/code/data/test/routing surfaces;
4. execute only against the planned surfaces;
5. update traceability and registries when relevant;
6. run validation checks;
7. create or update a delivery conformance report;
8. disclose any limitation before claiming completion.

---

# Project Boundary

The actual Pazarat project folder is:

```text
02_MY_PROJECT/pazarat/
```

Inside Pazarat means inside this folder.

The project-local control plane is:

```text
02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/
```

Product/developer documentation is:

```text
02_MY_PROJECT/pazarat/docs/
```

Implementation lives in:

```text
02_MY_PROJECT/pazarat/backend/
02_MY_PROJECT/pazarat/frontend/
02_MY_PROJECT/pazarat/database/
02_MY_PROJECT/pazarat/infra/
```

---

# Required Task Artifacts

For a non-trivial Pazarat task, the model must use:

```text
00_PROJECT_TUNNEL/_execution/CURRENT_TASK_LEDGER.yaml
00_PROJECT_TUNNEL/_execution/TASK_EXECUTION_PLAN.template.yaml
00_PROJECT_TUNNEL/_execution/DELIVERY_CONFORMANCE_REPORT.template.md
00_PROJECT_TUNNEL/_execution/DONE_DEFINITION.md
```

When the task is a feature or scenario, it must also create or update a feature packet under:

```text
00_PROJECT_TUNNEL/work_items/
```

When the task changes docs/code/database routing, it must update:

```text
00_PROJECT_TUNNEL/_routing/
00_PROJECT_TUNNEL/traceability/
00_PROJECT_TUNNEL/_registries/
```

as applicable.

---

# Pazarat Task Plan Minimum

A valid Pazarat task plan must identify:

- task id;
- user goal;
- task type;
- actual project folder;
- baseline source;
- affected documentation paths;
- affected backend paths;
- affected frontend paths;
- affected database paths;
- affected tunnel/routing paths;
- required outputs;
- forbidden paths and behaviors;
- governing Pazarat standards;
- validation checks;
- delivery conformance criteria.

---

# Forbidden Delivery Patterns

Reject or repair these patterns:

- generating backend/frontend/database outside `02_MY_PROJECT/pazarat/`;
- writing Pazarat project truth into general layers;
- treating `docs/` as the project-local tunnel;
- writing code without a feature packet or implementation contract when the code represents business behavior;
- writing documentation that cannot identify code/data/API implications when implementation relevance exists;
- changing docs without updating routing when the path affects implementation ownership;
- claiming completion without validation output.

---

# Delivery Conformance

Before any Pazarat artifact is delivered, verify:

- the task plan existed or was materially represented;
- required outputs were created or explicitly deferred;
- affected paths match the project boundary;
- forbidden paths are absent;
- docs/code/data/test/routing links are updated when relevant;
- repository or project validators ran when files were produced;
- known limitations are disclosed.

The final response should summarize this conformance for non-trivial work.

---

# Done Definition

A Pazarat task is not done because files exist.

It is done only when the task plan, produced files, routing/traceability, and validation evidence agree.
