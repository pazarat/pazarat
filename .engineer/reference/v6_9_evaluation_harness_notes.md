# v6.9 Evaluation Harness Notes

This version adds a project-neutral evaluation harness for testing whether the model behaves as a fused project engineer, not merely whether it produces a pleasant answer.

Core targets:
- Tool-first operation.
- Evidence-backed claims.
- Maturity-based recommendations.
- Absence claims only after zero-result scans.
- Safe write governance before modification.
- Runtime/project separation.
- Domain neutrality: no assumption that the project is software.

The test suite is intentionally written as user prompts because the primary risk is not Python test failure; it is model behavior drift under natural language requests.
