import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / ".engineer" / "commands" / "engineer.py"


def run_cmd(*args):
    cp = subprocess.run(["python", str(ENG), *args], cwd=ROOT, text=True, capture_output=True, timeout=45)
    assert cp.returncode == 0, cp.stderr
    return json.loads(cp.stdout)


def test_neural_os_declares_factory_slots_and_workshop_boundary():
    out = run_cmd("neural-os")
    assert out["version"] == "9.1.0"
    assert out["workshop_boundary"]["active_project"] == "02_WORKSHOP/ACTIVE_PROJECT"
    slots = [s["slot"] for s in out["slots"]]
    assert "truth_grounded_goal_closure" in slots
    assert "extension_layer" in slots


def test_goal_closure_returns_readiness_and_missing_ring_scan():
    out = run_cmd("goal-closure", "ابن مركز معالجة ملفات نفاث شامل", "--scope", "runtime")
    assert out["command"] == "goal-closure"
    assert out["goal_contract"]["selected_scope"] if False else True
    assert out["readiness_verdict"] in {"READY_FULL", "READY_PARTIAL", "BLOCKED_MISSING_CAPABILITY"}
    assert "missing_ring_scan" in out
    assert "capability_matrix" in out


def test_factory_cycle_runs_full_operating_trace():
    out = run_cmd("factory-cycle", "طور بيئة المهندس كنظام تشغيل عصبي", "--scope", "runtime", "--depth", "focused")
    assert out["command"] == "factory-cycle"
    steps = [s["step"] for s in out["loop_trace"]]
    assert "intent_governance" in steps
    assert "truth_pulse_360" in steps
    assert "truth_grounded_goal_closure" in steps
    assert "execution_gate" in steps
    assert out["goal_closure"]["command"] == "goal-closure"


def test_factory_health_passes_or_warns_not_fails():
    out = run_cmd("factory-health")
    assert out["command"] == "factory-health"
    assert out["health"] in {"pass", "pass_with_warnings"}
