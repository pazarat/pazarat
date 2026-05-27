import json
import subprocess


def run_cmd(*args):
    out = subprocess.check_output(["python", ".engineer/commands/engineer.py", *args], text=True)
    return json.loads(out)


def test_project_surface_requires_owner_content_gate():
    lens = run_cmd("project-lens", "--scope", "project")
    gate = lens["surface_owner_child_truth_gate"]
    assert gate["status"] == "pass"
    assert gate["owner_truth_file"]["content_status"] == "content_bearing"
    assert gate["owner_truth_file"]["path"].startswith("02_WORKSHOP/ACTIVE_PROJECT/")
    assert gate["incomplete_truth_children"]
    assert lens["first_step_candidate"]["action"] == "read_owner_and_direct_children_then_select_owner_ordered_incomplete_truth"
    assert lens["first_step_candidate"]["target_incomplete_truth_file"] is None
    assert lens["first_step_candidate"]["owner_truth_file"] == gate["owner_truth_file"]["path"]


def test_plug_surface_lens_carries_no_guessing_gate():
    plug = run_cmd("plug", "اخبرني عنك من انت وما عملك وماهي اول خطوة")
    lens = plug["project_surface_lens"]
    gate = lens["surface_owner_child_truth_gate"]
    assert gate["owner_truth_file"]["content_status"] == "content_bearing"
    assert any("Do not say the domain itself" in x for x in gate["claim_blocks"])
    assert plug["version"] == "7.0.0"
    assert lens["workshop_universal_lens"]["silent_gate"] is True
