import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"

def run_cmd(*args):
    cp = subprocess.run([sys.executable, str(ENG), *args], cwd=ROOT, text=True, capture_output=True, timeout=60)
    assert cp.returncode == 0, cp.stderr
    return json.loads(cp.stdout)

def test_file_matrix_pulse_returns_truth_map_and_governance():
    out = run_cmd("file-matrix-pulse", "اخبرني عن المشروع واول خطوة", "--scope", "project", "--max-files", "80", "--sample-chars", "1800")
    assert out["command"] == "file-matrix-pulse"
    assert out["version"] == "9.1.0"
    assert "one_page_neural_truth_map" in out
    assert "truth_governance" in out
    assert "recommended_entry_sequence" in out
    assert out["readiness_verdict"] in {"new_or_empty_project", "ready_for_surface_answer", "surface_answer_with_truth_warnings"}

def test_plug_fast_exposes_pulse_summary_and_surface_command():
    out = run_cmd("plug-fast", "اخبرني عنك ومشروعك", "--scope", "project")
    assert out["file_matrix_entry"]["surface_command"] == "file-matrix-pulse"
    assert "file_matrix_pulse_summary" in out
    assert "file-matrix-pulse" in out["mandatory_next_actions"]

def test_goal_closure_is_grounded_by_truth_pulse():
    out = run_cmd("goal-closure", "بناء مركز معالجة ملفات نفاث", "--scope", "runtime")
    gs = out["grounding_summary"]
    assert "truth_pulse_surface" in gs
    assert out["readiness_verdict"] in {"READY_FULL", "READY_PARTIAL", "BLOCKED_MISSING_CAPABILITY"}
