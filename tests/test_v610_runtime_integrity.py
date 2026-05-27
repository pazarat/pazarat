import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ENG=ROOT/'.engineer'/'commands'/'engineer.py'

def run(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)

def test_runtime_audit_passes_and_registry_is_complete():
    out=json.loads(run('runtime-audit'))
    assert out['status']=='pass', out
    assert out['parser_command_count'] == out['registry_command_count']

def test_doctor_uses_runtime_integrity():
    out=json.loads(run('doctor'))
    assert 'runtime_integrity' in out
    assert out['status']=='pass', out
