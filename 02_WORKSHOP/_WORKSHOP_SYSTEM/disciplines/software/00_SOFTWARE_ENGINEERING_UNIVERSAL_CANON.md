# Software Engineering Universal Canon

This canon is language-neutral. It does not prescribe .NET, Python, JavaScript, or any stack.
It defines the questions and standards a serious software project must answer locally.

## Universal Questions

- What application type is this?
- What architecture style is accepted locally?
- What is the source of truth for requirements?
- What is the data model and persistence strategy?
- What is the API or integration contract?
- What is the authorization and audit model?
- Does the system need realtime, events, background jobs, search, cache, or queues?
- How are migrations, tests, observability, deployment, and failure recovery handled?
- What patterns are forbidden?

## Local Specialization

Each software project must generate its local canons: stack, backend, database, API, frontend,
quality/testing, deployment/observability, security, and code practice as needed.
