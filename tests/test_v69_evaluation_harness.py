import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_deep_test_suite_exists_and_is_project_neutral():
    p = ROOT / '.engineer' / 'evaluation' / 'deep_test_suite_ar.json'
    assert p.exists()
    data = json.loads(p.read_text(encoding='utf-8'))
    assert len(data['questions']) >= 12
    blob = p.read_text(encoding='utf-8').lower()
    forbidden = ['pa'+'zarat', 'user '+'management', 'بازا'+'رات']
    assert not any(x in blob for x in forbidden)


def test_engineer_can_print_test_suite():
    out = subprocess.check_output([sys.executable, str(ROOT/'.engineer'/'commands'/'engineer.py'), 'test-suite'], cwd=ROOT, text=True)
    assert 'Deep Evaluation Test Suite' in out
    assert 'T01_surface_identity_fusion' in out


def test_rubric_has_critical_failures():
    p = ROOT / '.engineer' / 'evaluation' / 'evaluation_rubric.yaml'
    txt = p.read_text(encoding='utf-8')
    assert 'critical_failures' in txt
    assert 'absence' in txt or 'غياب' in txt
