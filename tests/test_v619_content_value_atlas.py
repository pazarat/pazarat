import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"


def run_json(*args):
    out = subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)
    return json.loads(out)


def test_value_atlas_command_exists_and_touches_all_file_types():
    data = run_json("value-atlas", "assessment and first step", "--scope", "project", "--limit", "12")
    assert data["file_count"] >= 1
    assert "counts_by_role" in data
    assert "high_value_files" in data
    assert "required_full_reads_before_high_impact_claims" in data
    assert data["high_impact_request"]["is_high_impact"] is True


def test_plug_includes_content_value_atlas_summary():
    data = run_json("plug", "evaluate project and first step", "--mode", "compact")
    assert "content_value_atlas_summary" in data
    assert data["content_value_atlas_summary"]["file_count"] >= 1
    assert "top_high_value_files" in data["content_value_atlas_summary"]


def test_runtime_audit_still_passes_and_registry_is_synced():
    data = run_json("runtime-audit")
    assert data["status"] == "pass"
    assert data["parser_command_count"] == data["registry_command_count"]


def test_neural_reflex_contains_content_value_and_response_rhythm():
    data = run_json("neural", "write a repair plan for the repository")
    names = [r["name"] for r in data["active_reflexes"]]
    assert "content_value_reflex" in names
    assert "response_rhythm_reflex" in names


def test_no_static_project_coupling_after_v619():
    data = run_json("runtime-audit")
    assert data.get("static_project_term_violations", 0) == 0
