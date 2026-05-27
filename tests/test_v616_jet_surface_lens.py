import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = ["python", ".engineer/commands/engineer.py"]
SURFACE_REQUEST = "اخبرني عنك من انت و ماهو عملك وظيفتك ومهامك ومهاراتك وكيف تتعامل مع مشروعي وتقييمك لوضعه الحالي وماهي اول خطوة تتخذها اتجاه المشروع"


def run_json(*args):
    out = subprocess.check_output(CMD + list(args), cwd=ROOT, text=True)
    return json.loads(out)


def run_text(*args):
    return subprocess.check_output(CMD + list(args), cwd=ROOT, text=True)


def test_project_lens_finds_actionable_domain_and_owner_gate():
    lens = run_json("project-lens", "--scope", "project")
    assert lens["strongest_actionable_domain"]["domain"]
    assert lens["surface_owner_child_truth_gate"]["owner_truth_file"]["content_status"] == "content_bearing"
    assert lens["first_step_candidate"]["target_incomplete_truth_file"] is None
    assert lens["implementation_status"] == "no_code_detected_in_current_project_scope"


def test_project_surface_answer_uses_lens_not_raw_snippet_dump():
    text = run_text("answer", SURFACE_REQUEST)
    assert "مهندس مشروع" in text
    assert "ورشة العمل" in text
    assert "أقوى إشارات الحقيقة التي لمستها" not in text


def test_plug_compact_contains_surface_lens():
    plug = run_json("plug", SURFACE_REQUEST)
    assert plug["output_mode"] == "compact"
    assert plug["version"] == "7.0.0"
    assert plug["project_surface_lens"]["strongest_actionable_domain"]["domain"]
    assert plug["project_surface_lens"]["workshop_universal_lens"]["silent_gate"] is True
    assert "project-lens" in plug["mandatory_next_actions"]


def test_relationship_graph_uses_effective_surface_query():
    graph = run_json("relationship-graph", SURFACE_REQUEST, "--scope", "project", "--limit", "6")
    assert graph["effective_query"] != graph["query"]
    assert graph["concept_owner_candidates"]


def test_runtime_audit_passes_after_surface_lens_changes():
    audit = run_json("runtime-audit")
    assert audit["status"] == "pass"
    assert audit["parser_command_count"] == audit["registry_command_count"]
