import subprocess, sys, json, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CMD=[sys.executable, str(ROOT/".engineer/commands/engineer.py")]

def run(*args):
    return subprocess.check_output(CMD+list(args), cwd=ROOT, text=True, encoding="utf-8")

def test_route_surface():
    out=json.loads(run("route","اخبرني عنك من انت وما عملك مع مشروعي وتقييمك"))
    assert out["route"]=="project_surface"
    assert out["scope"]=="project"

def test_project_state_matches_current_files():
    out=json.loads(run("touch","--scope","project"))
    cls=out["classification"]
    # The framework may be shipped empty or with a test project inserted.
    if cls.get("files", 0):
        assert cls["state"]=="PROJECT_DISCOVERY"
    else:
        assert cls["state"]=="PROJECT_FORMATION"

def test_doctor_pass():
    out=json.loads(run("doctor"))
    assert out["status"]=="pass"

def test_answer_no_runtime_leakage():
    out=run("answer","اخبرني عنك من انت وما عملك مع مشروعي")
    assert ".engineer" not in out
    assert "GPT" not in out
    assert "مهندس مشروعك" in out

def test_zip_flat_assumption():
    assert (ROOT/"00_ENTRYPOINT.yaml").exists()
    assert (ROOT/"02_WORKSHOP"/"ACTIVE_PROJECT").exists()

def test_cycle_surface_returns_operating_context_v612():
    out=json.loads(run("cycle","اخبرني عنك من انت وما عملك مع مشروعي وتقييمك الحالي"))
    assert out["central_os_mode"] == "mandatory_operating_context"
    assert out["route"]["route"] == "project_surface"
    assert "tool_keyboard" in out
    assert "concept_matrix" in out


def test_truth_map_detects_scenario_material(tmp_path):
    scenario_dir=ROOT/"02_WORKSHOP"/"ACTIVE_PROJECT"/"scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    f=scenario_dir/"checkout_scenarios.md"
    f.write_text("# Checkout Scenarios\n\n## Scenario: approved user completes order\n\nAcceptance criteria and lifecycle events.", encoding="utf-8")
    try:
        out=json.loads(run("truth-map","--scope","project"))
        assert out["category_counts"]["scenario"] >= 1
        assert any("سيناريو" in c["claim"] or "Scenario" in c["claim"] or "سيناريوهات" in c["claim"] for c in out["claims"])
        ans=run("answer","اخبرني عنك وما تقييمك لوضع المشروع")
        assert "سيناريو" in ans or "سيناريوهات" in ans
        assert "بلا سيناريو" not in ans
    finally:
        try: f.unlink()
        except FileNotFoundError: pass
        try: scenario_dir.rmdir()
        except OSError: pass

def test_evidence_command_finds_content_not_only_titles(tmp_path):
    d=ROOT/"02_WORKSHOP"/"ACTIVE_PROJECT"/"materials"
    d.mkdir(parents=True, exist_ok=True)
    f=d/"notes.md"
    f.write_text("# Notes\n\nهذا الملف يحتوي سيناريو ناضج لرحلة المستخدم رغم أن العنوان لا يقول ذلك.", encoding="utf-8")
    try:
        out=json.loads(run("evidence","سيناريو","--scope","project"))
        assert out["count"] >= 1
        assert any("notes.md" in r["path"] for r in out["results"])
    finally:
        try: f.unlink()
        except FileNotFoundError: pass
        try: d.rmdir()
        except OSError: pass
