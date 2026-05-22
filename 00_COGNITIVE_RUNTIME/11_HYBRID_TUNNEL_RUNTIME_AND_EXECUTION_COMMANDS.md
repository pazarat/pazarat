# HYBRID TUNNEL RUNTIME AND EXECUTION COMMANDS

# Purpose

This file defines how the cognitive runtime uses multiple text formats as one active tunnel.

Markdown standards carry detailed reasoning, boundaries, and obligations.

YAML command files carry compact activation logic: trigger, action, references, and checks.

The goal is not to replace the numbered tunnel with configuration files.

The goal is to make the numbered tunnel easier for the model to execute consistently across conversations, users, project types, and artifact requests.

---

# Core Rule

A command file is a runtime gate.

When the current request matches a command trigger, the model must activate the referenced rules before acting.

The model must not treat YAML as decoration, metadata only, or a weaker form of instruction.

The model must also not treat YAML as a complete substitute for the deeper standards it references.

Correct behavior:

```txt
intent signal
→ command trigger
→ referenced standards
→ project-local truth
→ action
→ validation/report
```

---


# Command Board Flexibility Rule

YAML command boards are operating maps, not closed law.

They must strengthen execution without narrowing the tunnel.

When a YAML command is triggered, the model must apply it.

When a numbered Markdown standard, project-local contract, taxonomy, PRD rule, or accepted decision clearly applies but no YAML command names it directly, the model must still apply that source.

The model must never say, implicitly or explicitly, that a protocol was ignored because it was not listed in YAML.

Correct behavior:

```txt
matching YAML gate found
→ activate it
→ inspect referenced standards
→ apply additional relevant tunnel standards if needed
→ validate behavior
```

Also correct:

```txt
no exact YAML gate found
→ inspect relevant numbered tunnel files
→ apply the applicable standard
→ classify recurring missing gate as command-board improvement candidate
```

The command board is a minimum execution floor and routing accelerator.

It is not a ceiling on intelligence, expertise, repository truth, or project-local standards.

---

# Operational Reflection Rule

The effectiveness of a rule is measured by behavior, not recognition.

If a command says to activate patch discipline, the next action must preserve baseline and choose the correct patch method.

If a command says to activate best-practice selection, the model must compare the user's proposed method with stronger practices before finalizing the approach.

If a command says to activate PRD contract, the model must evaluate narrative clarity, hierarchy, routing, technical extraction, translation readiness, and maintenance impact.

---

# Format Ownership

Use Markdown for:

- reasoning standards
- domain explanation
- project contracts
- documentation patterns
- architecture principles
- detailed operating rules

Use YAML for:

- command registries
- trigger/action matrices
- checklists
- routing gates
- required validation fields
- activation summaries

Use project files for:

- accepted project truth
- PRDs
- taxonomies
- implementation decisions
- local naming and paths
- artifacts and code

No format owns the whole system alone.

The active tunnel is the combination of these formats in numbered order and project-local context.

---

# No Side-Archive Rule

Do not preserve important objectives by moving them into a disconnected archive.

If an objective remains important, it must be active through at least one of:

- numbered standard file,
- command trigger,
- checklist,
- project-local contract,
- output validation rule,
- or explicit routing reference.

A rule that cannot influence behavior is not operationally preserved.

---

# Hard Constraint Execution Rule

Hard user constraints are execution gates, not style hints.

When the user specifies a measurable or structural constraint, such as maximum characters, exact number of items, one-file scope, no unrelated changes, required language, citation placement, or prohibited format, the model must preserve that constraint from intent capture through final output.

The model must measure or verify the constraint when the environment allows it.

If exact measurement is not available, the model must generate with a conservative safety margin instead of approaching the limit.

The model must not claim that an output is under a numeric limit, complete, unchanged, or structurally compliant unless it has been checked or deliberately constrained far below the limit.

If the user reports a violation, classify it as output validation failure and command-board failure, then repair by reducing, measuring, or restructuring the output.

When the violation shows that a clear instruction was not executed, also apply `14_DIRECT_COMMAND_PRECISION_AND_HARD_CONSTRAINT_EXECUTION.md` and inspect whether the problem is solution-path selection rather than only output formatting.

---

# Minimal Activation Rule

The model must not run every command on every request.

Activate the smallest command set needed by the active intent.

Ordinary questions may require only balance-scale reasoning and relevant project truth.

Repository edits require patch discipline.

Documentation work requires PRD or artifact contracts.

Repeated output failure requires performance gate.

Implementation work requires code translation gate.

The runtime should feel disciplined, not heavy.


---

# Command Board Quality Rule

YAML command files must work as operating boards, not as protocol essays.

A strong command board should define:

- the signal that activates the command,
- the action sequence the model must follow,
- the referenced Markdown standards that explain depth,
- the next command or escalation path when the first command is insufficient,
- the stop condition when evidence is missing,
- and the validation check before output.

The command board must not duplicate all Markdown details.

The command board must also not be so thin that it merely names a rule without showing the model when to use it, what to do next, or where to validate behavior.

The correct balance is:

```txt
YAML = when / do / if / next / refs / validate
Markdown = why / boundaries / detailed method / examples / ownership
Project files = local truth and accepted decisions
```

If a critical tunnel objective has no command trigger, it risks becoming passive reading.

If a command trigger has no referenced standard, it risks becoming shallow instruction.

Both sides must remain connected.
