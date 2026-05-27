import subprocess, sys, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CMD=[sys.executable, str(ROOT/'.engineer/commands/engineer.py')]

def run(*args):
    return subprocess.check_output(CMD+list(args), cwd=ROOT, text=True, encoding='utf-8')

def test_evidence_lock_and_scenario_map_detect_content(tmp_path):
    d=ROOT/'02_WORKSHOP'/'ACTIVE_PROJECT'/'scenario_pack'
    d.mkdir(parents=True, exist_ok=True)
    f=d/'operations.md'
    f.write_text('# Operations\n\nThis contains a mature workflow and acceptance criteria for approval lifecycle.', encoding='utf-8')
    try:
        sm=json.loads(run('scenario-map','--scope','project'))
        assert sm['scenario_count'] >= 1
        lock=json.loads(run('evidence-lock','approval lifecycle','--scope','project'))
        assert lock['scenario_map']['scenario_count'] >= 1
        assert lock['status'] == 'pass'
    finally:
        f.unlink(missing_ok=True)
        try: d.rmdir()
        except OSError: pass

def test_claim_check_rejects_false_absence(tmp_path):
    d=ROOT/'02_WORKSHOP'/'ACTIVE_PROJECT'/'scenario_pack'
    d.mkdir(parents=True, exist_ok=True)
    f=d/'journey.md'
    f.write_text('# Journey\n\nسيناريو ناضج لرحلة المستخدم ومعايير قبول واضحة.', encoding='utf-8')
    try:
        out=json.loads(run('claim-check','لا توجد سيناريوهات في المشروع','--scope','project'))
        assert out['status'] == 'fail'
        assert out['problems']
    finally:
        f.unlink(missing_ok=True)
        try: d.rmdir()
        except OSError: pass

def test_write_plan_detects_related_material_before_adding(tmp_path):
    d=ROOT/'02_WORKSHOP'/'ACTIVE_PROJECT'/'requirements'
    d.mkdir(parents=True, exist_ok=True)
    f=d/'core_capability.md'
    f.write_text('# Core Capability\n\nThis file defines capability ownership, access rules, verification steps, and approval criteria.', encoding='utf-8')
    try:
        out=json.loads(run('write-plan','02_WORKSHOP/ACTIVE_PROJECT/requirements/new_capability.md','capability access verification approval'))
        assert out['impact_scan']['related_count'] >= 1
        assert out['recommendation'] in {'update_existing_or_confirm_new_file','safe_to_create_after_review'}
    finally:
        f.unlink(missing_ok=True)
        try: d.rmdir()
        except OSError: pass

def test_safe_write_is_dry_run_by_default(tmp_path):
    target='02_WORKSHOP/ACTIVE_PROJECT/tmp_should_not_exist.md'
    p=ROOT/target
    p.unlink(missing_ok=True)
    out=json.loads(run('safe-write',target,'--text','hello','--reason','test safe write'))
    assert out['status'] == 'dry_run'
    assert not p.exists()

