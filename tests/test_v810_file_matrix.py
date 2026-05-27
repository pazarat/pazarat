import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"


def run_cmd(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)


def test_file_matrix_build_and_status():
    data = json.loads(run_cmd("file-matrix-build", "--scope", "runtime", "--force"))
    assert data["version"] == "9.1.0"
    assert data["file_count"] >= 1
    status = json.loads(run_cmd("file-matrix-status", "--scope", "runtime"))
    assert status["fresh"] is True
    assert status["symbol_count"] >= 1
    assert status["chunk_count"] >= 1


def test_file_matrix_context_returns_neural_map_and_gates():
    data = json.loads(run_cmd("file-matrix-context", "api database permissions", "--scope", "runtime", "--mode", "deep", "--max-files", "4"))
    assert data["command"] == "file-matrix-query"
    assert "one_page_project_neural_map" in data
    assert "selected_files" in data
    assert "targeted_reads" in data
    assert "current files remain source of truth" in " ".join(data["mandatory_rules"]).lower()


def test_file_matrix_doctor_passes():
    data = json.loads(run_cmd("file-matrix-doctor", "--scope", "runtime"))
    assert data["health"] in {"pass", "pass_with_warnings"}
    assert data["problems"] == []
