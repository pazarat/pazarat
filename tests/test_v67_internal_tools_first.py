import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT/'.engineer'/'commands'/'engineer.py'

def run(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)

def test_tool_plan_project_surface_prefers_internal_tools():
    out=json.loads(run('tool-plan','اخبرني عنك وما عملك مع مشروعي'))
    assert out['internal_tools_first'] is True
    assert out['route']['route'] == 'project_surface'
    cmds=[s['cmd'] for s in out['sequence']]
    assert 'context-pack' in cmds
    assert 'evidence-lock' in cmds
    assert out['fallback_policy']['allowed'] is True

def test_receipt_records_internal_usage():
    out=json.loads(run('receipt','اخبرني عنك وما عملك مع مشروعي'))
    assert out['tool_contract'] == 'internal_tools_first_then_native_fallback_if_needed'
    assert 'evidence-lock' in out['internal_tools_used']
    assert 'category_counts' in out

def test_tool_contract_files_exist():
    assert (ROOT/'.engineer'/'governance'/'internal_tools_first.yaml').exists()
    assert (ROOT/'.engineer'/'runtime'/'tool_contract.yaml').exists()
    assert (ROOT/'.engineer'/'protocols'/'tool_first_navigation.yaml').exists()
