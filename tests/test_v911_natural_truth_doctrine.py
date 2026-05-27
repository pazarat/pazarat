import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / '.engineer' / 'commands' / 'engineer.py'

def run_cmd(*args):
    out = subprocess.check_output([sys.executable, str(ENG), *args], cwd=str(ROOT), text=True)
    return json.loads(out)


def test_truth_authority_is_advisory_not_cage():
    data = run_cmd('truth-authority-gate', 'اخبرني عن مشروعك وما اول خطوة؟', '--scope', 'project')
    assert data['authority_style'] == 'advisory_truth_compass_not_permission_cage'
    assert data['model_freedom_contract']['no_forced_search_sequence'] is True
    assert data['model_freedom_contract']['model_decides_depth'] is True
    assert data['claim_permissions']['advisory_only'] is True


def test_file_matrix_pulse_defaults_are_not_artificially_capped():
    data = run_cmd('file-matrix-pulse', 'تقييم المشروع', '--scope', 'project')
    coverage = data['coverage']
    assert coverage['content_read_mode'] == 'full_read_through_safe_reader'
    assert coverage['value_basis'] == 'content_and_truth_alignment_not_file_size'
    assert coverage['scanned_files'] == coverage['total_files']


def test_plug_fast_exposes_principles_not_mandatory_next_actions():
    data = run_cmd('plug-fast', 'اخبرني عن مشروعك')
    assert data.get('mandatory_next_actions') == []
    assert 'truth_principles' in data
    assert data.get('hard_blocks') == ['Advisory: do not use file size as value; calibrate claims to content/value truth.']
    assert data['governed_decision_space']['model_is_free_to_choose_depth'] is True
