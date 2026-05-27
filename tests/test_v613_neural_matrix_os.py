import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = ["python", ".engineer/commands/engineer.py"]


def run(*args):
    out = subprocess.check_output(CMD + list(args), cwd=ROOT, text=True)
    return json.loads(out)


def test_plug_contains_neural_reflex_graph():
    data = run("plug", "أريد إضافة ملف جديد يشرح مفهوم موجود")
    assert data["central_os_mode"] == "mandatory_operating_context"
    assert "neural_reflex_graph" in data
    graph = data["neural_reflex_graph"]
    assert "write_reflex" in [r["name"] for r in graph["active_reflexes"]]
    assert "duplicate-scan" in graph["required_gates"]
    assert "create_before_owner_search" in graph["blocked_operations"]


def test_neural_command_routes_best_fit_and_blocks_generic_advice():
    data = run("neural", "استنتج النواقص وافضل الممارسات المناسبة للبيئة")
    assert "best_fit_reflex" in [r["name"] for r in data["active_reflexes"]]
    assert "generic_advice_without_project_mapping" in data["blocked_operations"]


def test_best_fit_review_returns_gap_matrix():
    data = run("best-fit", "نضج بيئة المهندس", "--scope", "runtime")
    assert data["mode"] == "internal_best_fit_review_not_external_web_research"
    assert data["summary"]["patterns_checked"] >= 5
    assert "fit_matrix" in data and data["fit_matrix"]
    assert {"pattern", "fit_status", "recommendation"}.issubset(data["fit_matrix"][0].keys())


def test_safe_write_includes_preflight_gate_on_dry_run():
    data = run("safe-write", "02_WORKSHOP/ACTIVE_PROJECT/_tmp_neural_test.md", "--text", "test", "--reason", "اختبار كتابة", "--scope", "project")
    assert data["status"] == "dry_run"
    assert "preflight_gate" in data
    assert "duplicate-scan" in data["preflight_gate"]["required_gates"]


def test_runtime_audit_knows_new_commands():
    data = run("runtime-audit")
    assert data["status"] == "pass"
    assert data["parser_command_count"] == data["registry_command_count"]
    assert data["parser_command_count"] >= 38
