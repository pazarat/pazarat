import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = [sys.executable, '.engineer/commands/engineer.py']


def run_json(*args):
    cp = subprocess.run(CMD + list(args), cwd=ROOT, text=True, capture_output=True, check=True, timeout=90)
    return json.loads(cp.stdout)


def test_truth_authority_gate_controls_claims_not_answer_shape():
    packet = run_json('truth-authority-gate', 'اخبرني عنك وما عملك وكيف تتعامل مع مشروعي', '--scope', 'project')
    assert packet['command'] == 'truth-authority-gate'
    assert 'claim_permissions' in packet
    assert packet['governing_rule'].startswith('The runtime does not cage')
    assert packet['evidence_status']['value_basis'] == 'content_value_cross_file_alignment_not_size_or_path_only'


def test_open_neural_entry_has_governed_freedom_and_truth_authority():
    packet = run_json('open-neural-entry', 'اخبرني عنك وما عملك وكيف تتعامل مع مشروعي')
    assert packet['command'] == 'open-neural-entry'
    assert packet['governed_freedom_contract']['no_scripted_first_contact'] is True
    assert packet['governed_freedom_contract']['runtime_enforces_claim_authority_not_answer_shape'] is True
    assert 'truth_authority_gate' in packet
    assert packet['identity_boundary']['engineer_runtime'].startswith('silent operating system')


def test_plug_fast_exposes_decision_space_not_forced_first_contact():
    packet = run_json('plug-fast', 'اخبرني عنك وما عملك وكيف تتعامل مع مشروعي')
    assert packet['command'] == 'plug-fast'
    assert packet.get('mandatory_next_actions') == []
    assert packet['governed_decision_space']['model_is_free_to_choose_depth'] is True
    assert 'truth_authority_gate' in packet
    assert any('file size' in x.lower() for x in packet['hard_blocks'])
