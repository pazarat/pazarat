import json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = ["python", ".engineer/commands/engineer.py"]

def run(*args):
    out = subprocess.check_output(CMD + list(args), cwd=ROOT, text=True)
    return json.loads(out)

def test_plug_defaults_to_compact_and_full_is_available():
    compact = run("plug", "حول PRD إلى API و Database")
    full = run("plug", "حول PRD إلى API و Database", "--mode", "full")
    assert compact["output_mode"] == "compact"
    assert compact["central_os_mode"] == "mandatory_operating_context"
    assert "relationship_graph_summary" in compact
    assert full["output_mode"] == "full"
    assert "relationship_graph" in full

def test_relationship_graph_command_maps_owner_and_linkages():
    data = run("relationship-graph", "API Database permissions tests", "--scope", "project")
    assert data["graph_type"] == "semantic_relationship_navigation_graph"
    assert "concept_owner_candidates" in data
    assert "cross_artifact_linkages" in data
    assert {"states_events", "permissions_audit", "data_api", "tests_acceptance"}.issubset(data["cross_artifact_linkages"].keys())

def test_best_fit_declares_generated_outputs_are_excluded():
    data = run("best-fit", "نضج بيئة المهندس", "--scope", "runtime")
    assert data["evidence_policy"] == "current_static_files_first_generated_outputs_excluded_unless_explicitly_requested"
    assert all(row.get("evidence_policy") == "generated_indexes_ledgers_state_excluded_by_default" for row in data["fit_matrix"])

def test_cache_clean_is_dry_run_by_default():
    data = run("cache-clean")
    assert data["status"] == "dry_run"
    assert "action_count" in data

def test_runtime_audit_knows_v615_commands():
    data = run("runtime-audit")
    assert data["status"] == "pass"
    assert data["parser_command_count"] == data["registry_command_count"]
    assert data["parser_command_count"] >= 42
