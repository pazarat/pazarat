import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = [sys.executable, '.engineer/commands/engineer.py']


def run_json(*args):
    cp = subprocess.run(CMD + list(args), cwd=ROOT, text=True, capture_output=True, check=True, timeout=60)
    return json.loads(cp.stdout)


def test_open_entry_is_not_first_contact_cage():
    packet = run_json('open-neural-entry', 'اخبرني عنك وما عملك وكيف تتعامل مع مشروعي')
    assert packet['command'] == 'open-neural-entry'
    assert packet['intent_profile']['model_freedom_contract']['model_role'] == 'reasoning_engine_not_script_reader'
    assert packet['identity_boundary']['active_project'] == 'the subject project truth surface'
    assert 'first-contact' not in packet.get('open_navigation', {}).get('recommended', [])


def test_truth_sweep_uses_content_not_size():
    packet = run_json('truth-sweep-360', 'تقييم المشروع الحالي', '--scope', 'project')
    assert packet['command'] == 'truth-sweep-360'
    assert packet['coverage']['documentation_files_read'] > 0
    rules = ' '.join(packet['governance_rules']).lower()
    assert 'file size is never' in rules
    assert packet['truth_spine']


def test_operation_360_is_lifecycle_packet():
    packet = run_json('operation-360', 'ضع خطة إصلاح جذري لمشكلة في المشروع')
    assert packet['command'] == 'operation-360'
    steps = [x['step'] for x in packet['lifecycle_trace']]
    assert 'truth_sweep_360' in steps
    assert 'anti_patchwork_gate' in steps
    assert packet['rule'].startswith('No proposal')
