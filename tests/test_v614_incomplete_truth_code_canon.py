import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = ["python", ".engineer/commands/engineer.py"]


def run(*args):
    out = subprocess.check_output(CMD + list(args), cwd=ROOT, text=True)
    return json.loads(out)


def test_truth_maturity_command_exists_and_blocks_execution_over_incomplete_truth():
    data = run("truth-maturity", "ابدأ بناء backend و API و Database", "--scope", "project")
    assert data["mode"] == "incomplete_truth_maturity_gate"
    assert data["overall_status"] in {"partial_truth_review_required", "incomplete_truth_detected", "accepted_for_discovery_continue_with_evidence"}
    assert "Discovery may classify" in " ".join(data["rules"])
    assert data["owner_candidates"]


def test_canon_check_prioritizes_code_practice_canon():
    data = run("canon-check", "ابدأ بناء backend و API و Database", "--scope", "project")
    assert data["gate"] == "code_practice_canon_gate"
    assert data["status"] == "pass"
    assert data["canon_candidates"]
    assert "CODE_PRACTICE" in data["canon_candidates"][0]["path"] or "CANON" in data["canon_candidates"][0]["path"]


def test_plug_contains_truth_maturity_and_canon_summaries_for_implementation():
    data = run("plug", "حول PRD إلى API و Database و اختبارات")
    assert data["version"] == "7.0.0"
    assert data["route"]["route"] == "implementation_translation_work"
    assert data["truth_maturity_summary"] is not None
    assert data["canon_check_summary"] is not None
    nxt = " ".join(data["mandatory_next_actions"])
    assert "truth-maturity" in nxt
    assert "canon-check" in nxt


def test_neural_graph_has_incomplete_truth_and_code_practice_reflexes():
    data = run("neural", "ابدأ تنفيذ كود backend من معيار ناقص وحقيقة ناقصة")
    names = {r["name"] for r in data["active_reflexes"]}
    assert "incomplete_truth_reflex" in names
    assert "code_practice_reflex" in names
    assert "production_execution_over_incomplete_truth" in data["blocked_operations"]
    assert "code_from_stack_name_only" in data["blocked_operations"]


def test_runtime_audit_knows_v614_commands():
    data = run("runtime-audit")
    assert data["status"] == "pass"
    assert data["parser_command_count"] == data["registry_command_count"]
    assert data["parser_command_count"] >= 40
