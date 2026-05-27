import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ["python", str(ROOT / ".engineer" / "commands" / "engineer.py")]


def run_json(*args):
    out = subprocess.check_output(CLI + list(args), cwd=ROOT, text=True)
    return json.loads(out)


def test_plug_exists_and_returns_operating_context():
    data = run_json("plug", "حول PRD إلى API و Database")
    assert data["central_os_mode"] == "mandatory_operating_context"
    assert data["route"]["route"] == "implementation_translation_work"
    assert "tool_keyboard" in data and data["tool_keyboard"]
    assert "protocol_stack" in data and "entrypoint_first" in data["protocol_stack"]
    assert "concept_matrix" in data and "concept_buckets" in data["concept_matrix"]
    assert "hard_blocks" in data and data["hard_blocks"]


def test_cycle_delegates_to_plug_shape():
    data = run_json("cycle", "افحص بيئة المهندس والملاحة")
    assert data["central_os_mode"] == "mandatory_operating_context"
    assert data["route"]["route"] == "runtime_work"
    assert "runtime_audit" in data["protocol_stack"] or "runtime_scope_only" in data["protocol_stack"]


def test_write_route_has_write_gates():
    data = run_json("plug", "أضف ملف جديد يشرح مفهوم موجود")
    assert data["route"]["route"] == "write_or_modify_work"
    nxt = " ".join(data.get("mandatory_next_actions", []))
    assert "duplicate-scan" in nxt
    assert "impact-scan" in nxt
    assert "write-plan" in nxt
    assert "safe-write" in nxt


def test_tool_registry_includes_plug():
    text = (ROOT / ".engineer" / "runtime" / "tool_registry.yaml").read_text(encoding="utf-8")
    assert "plug:" in text
    assert "last_central_plug.json" in text


def test_runtime_audit_passes_with_plug():
    data = run_json("runtime-audit")
    assert data["status"] == "pass"
    assert not data.get("problems")
