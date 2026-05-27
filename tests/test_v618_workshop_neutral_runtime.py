import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run_cmd(*args):
    return subprocess.check_output(["python", ".engineer/commands/engineer.py", *args], cwd=ROOT, text=True)

def test_runtime_audit_rejects_project_specific_coupling():
    data = json.loads(run_cmd("runtime-audit"))
    assert data["status"] == "pass"
    assert not data.get("problems")
    assert data.get("static_project_term_violations", 0) == 0

def test_workshop_lens_exists_and_is_silent_gate():
    data = json.loads(run_cmd("workshop-lens"))
    assert data["silent_gate"] is True
    assert data["files_detected"] >= 5
    assert "360_method" in data["buckets"]
    assert any("cannot replace active project truth" in r or "cannot override" in r for r in data["operating_rules"])

def test_plug_includes_workshop_and_does_not_choose_project_child_from_runtime_memory():
    data = json.loads(run_cmd("plug", "اخبرني عنك وما اول خطوة"))
    assert data["version"] == "7.0.0"
    assert data["route"]["route"] == "project_surface"
    assert data["project_surface_lens"]["workshop_universal_lens"]["silent_gate"] is True
    first = data["project_surface_lens"].get("first_step_candidate") or {}
    assert first.get("action") == "read_owner_and_direct_children_then_select_owner_ordered_incomplete_truth"
    assert first.get("target_incomplete_truth_file") is None


def test_static_runtime_does_not_hardcode_active_project_names():
    forbidden = ["Paza"+"rat", "User_Management", "verify_template", "user_approvals", "all_users", "b2b_"+"sel"+"lers", "b2c_"+"sel"+"lers"]
    roots = [ROOT/".engineer"/"commands", ROOT/".engineer"/"runtime", ROOT/".engineer"/"governance", ROOT/".engineer"/"protocols", ROOT/".engineer"/"kernel", ROOT/".engineer"/"capabilities"]
    hits=[]
    for base in roots:
        for path in base.rglob("*"):
            if path.is_file() and path.suffix in {".py", ".yaml", ".yml", ".md", ".txt"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                for term in forbidden:
                    if term in text:
                        hits.append((str(path.relative_to(ROOT)), term))
    assert hits == []
