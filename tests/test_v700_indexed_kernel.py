import json, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"


def run_cmd(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)


def test_build_index_and_kernel_status():
    data=json.loads(run_cmd("build-index", "--scope", "project", "--compact"))
    assert data["kernel_version"] == "7.0.0"
    assert data["file_count"] >= 1
    status=json.loads(run_cmd("kernel-status"))
    assert status["version"] == "7.0.0"
    assert status["indexes"]["project"]["exists"] is True


def test_plug_fast_is_compact_and_indexed():
    data=json.loads(run_cmd("plug-fast", "اخبرني عنك وما عملك"))
    assert data["command"] == "plug-fast"
    assert data["index_status"]["file_count"] >= 1
    assert "selected_lens" in data
    assert len(json.dumps(data, ensure_ascii=False)) < 20000


def test_plug_default_uses_fast_kernel():
    data=json.loads(run_cmd("plug", "اخبرني عنك وما عملك"))
    assert data["command"] == "plug-fast"
    assert data["kernel_version"] == "7.0.0"


def test_operation_mode_and_deep_plug():
    mode=json.loads(run_cmd("operation-mode", "أصلح بيئة المهندس دون كسر"))
    assert mode["risk"] in {"high", "critical"}
    deep=json.loads(run_cmd("plug-deep", "أصلح بيئة المهندس دون كسر", "--scope", "runtime", "--full-reads", "2"))
    assert deep["command"] == "plug-deep"
    assert len(deep.get("deep_reads", [])) <= 2


def test_golden_suite_exists():
    data=json.loads(run_cmd("golden-suite"))
    assert len(data["prompts"]) >= 4
    assert any(p["id"] == "surface_identity" for p in data["prompts"])
