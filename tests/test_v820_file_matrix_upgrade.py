import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"

def run_cmd(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)

def test_v820_file_matrix_has_chunk_and_semantic_lenses():
    data = json.loads(run_cmd("file-matrix-context", "api database permissions", "--scope", "runtime", "--mode", "deep", "--max-files", "4"))
    lenses = set(data["search_lenses_used"])
    assert "chunk-fts" in lenses
    assert "semantic-lite-chunks" in lenses
    assert "selected_files" in data
    assert "relationship_neighbors" in data

def test_v820_doctor_reports_adapter_readiness():
    data = json.loads(run_cmd("file-matrix-doctor", "--scope", "runtime"))
    assert data["version"] == "9.1.0"
    adapters = data["adapter_readiness"]
    assert adapters["sqlite_fts5"] is True
    assert adapters["chunk_index"] is True
    assert adapters["semantic_lite"] is True
    assert "tree_sitter_ast" in adapters
    assert "lsp_bridge" in adapters
