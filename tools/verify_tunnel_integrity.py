#!/usr/bin/env python3
"""Structural and hygiene integrity checks for the Mind_Ai repository.

This validator is intentionally conservative. It checks failures that previously caused
repository/codebase integration drift or tunnel degradation:

- missing root entrypoints
- buried or duplicated tunnel paths
- missing structural transformation gates
- broken command-board wiring
- obvious generator residue such as `$content`
- stale User Management approval route wording after the user_approvals migration
"""
from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = [
    "00_AI_REPOSITORY_BOOTSTRAP.md",
    "00_ENTRY_MAP.md",
    "ENGINEER_ENTRY_PROTOCOL.md",
    "00_TUNNEL_EXECUTION_COMMANDS.yaml",
    "00_COGNITIVE_RUNTIME",
    "01_PROJECT_ORCHESTRATION",
    "02_MY_PROJECT",
]

FORBIDDEN_PATH_PARTS = [
    "docs/ai_tunnel/00_COGNITIVE_RUNTIME",
    "docs/ai_tunnel/01_PROJECT_ORCHESTRATION",
    "docs/ai_tunnel/02_MY_PROJECT",
    "docs/ai_tunnel/docs/ai_tunnel",
]

REQUIRED_FILES = [
    "01_PROJECT_ORCHESTRATION/22_REPOSITORY_STRUCTURAL_TRANSFORMATION_AND_CODEBASE_INTEGRATION_GATE.md",
    "02_MY_PROJECT/pazarat/17_PAZARAT_CODEBASE_INTEGRATION_AND_DOCUMENTATION_ROUTING_STANDARD.md",
]

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def main() -> None:
    for item in REQUIRED_ROOT:
        if not (ROOT / item).exists():
            fail(f"missing required root item: {item}")

    all_paths = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")]
    for forbidden in FORBIDDEN_PATH_PARTS:
        if any(path.startswith(forbidden) for path in all_paths):
            fail(f"forbidden buried/duplicated tunnel path detected: {forbidden}")

    for item in REQUIRED_FILES:
        if not (ROOT / item).exists():
            fail(f"missing repaired gate file: {item}")

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "$content" in text:
                fail(f"generator residue `$content` detected in {path.relative_to(ROOT).as_posix()}")

    command_board_text = read("00_TUNNEL_EXECUTION_COMMANDS.yaml")
    if yaml is not None:
        try:
            command_board = yaml.safe_load(command_board_text)
        except Exception as exc:
            fail(f"root command board YAML is invalid: {exc}")
    else:
        command_board = {}

    for required in [
        "STRUCTURAL_TRANSFORMATION_GATE",
        "PATCH_DISCIPLINE",
        "DIRECT_EXECUTION_PRECISION",
        "HARD_CONSTRAINT_VALIDATION",
    ]:
        if required not in command_board_text:
            fail(f"root command board does not activate {required}")

    if "command_priority:" not in command_board_text:
        fail("root command board is missing command_priority precedence block")

    if "if_large_or_multi_file_update" not in command_board_text:
        fail("PATCH_DISCIPLINE is missing large/multi-file update branch")

    if isinstance(command_board, dict):
        always = command_board.get("operating_cycle", {}).get("always", [])
        if "activate_general_360_coherence" in always:
            fail("general 360 coherence must not be forced in operating_cycle.always; activate it by signal/command")
        if "synchronize_repository_operating_identity" in always:
            fail("operating identity must not be forced in operating_cycle.always; activate it by signal/command")

    pazarat_board = read("02_MY_PROJECT/pazarat/12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml")
    if "codebase_integration_and_docs_routing_gate" not in pazarat_board:
        fail("Pazarat command board does not activate codebase integration routing gate")

    user_mgmt = ROOT / "02_MY_PROJECT/pazarat/A_dashboards/A-A_admin_dashboard/modules/business/User_Management/User_Management_PRD.md"
    if user_mgmt.exists():
        text = user_mgmt.read_text(encoding="utf-8")
        if "Approval Route Naming" in text or "current `approved` route" in text:
            fail("stale Approval Route Naming / approved route wording remains in User_Management_PRD.md")
        if "user_approvals" not in text:
            fail("User_Management_PRD.md does not reference current user_approvals route")

    print("OK: Mind_Ai tunnel integrity and hygiene checks passed.")


if __name__ == "__main__":
    main()
