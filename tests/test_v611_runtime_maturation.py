import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT/'.engineer'/'commands'/'engineer.py'

def run(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True, encoding='utf-8')


def test_semantic_routes_do_not_fall_back_to_surface():
    assert json.loads(run('route', 'أريد بحثاً علمياً عن الطاقة الشمسية'))['route'] == 'research_work'
    assert json.loads(run('route', 'ابحث خارجياً عن أحدث معيار للخصوصية'))['route'] == 'external_research_work'
    assert json.loads(run('route', 'حول PRD إلى API و Database وصلاحيات'))['route'] == 'implementation_translation_work'


def test_safe_write_blocks_project_scope_from_runtime_paths():
    out = json.loads(run('safe-write', '.engineer/governance/should_not_write.md', '--text', 'x', '--reason', 'scope boundary test', '--scope', 'project'))
    assert out['status'] == 'blocked'
    assert out['reason'] == 'target_outside_declared_scope'
    assert not (ROOT/'.engineer/governance/should_not_write.md').exists()


def test_runtime_audit_exposes_health_without_failing_on_nonfatal_warnings():
    out = json.loads(run('runtime-audit'))
    assert out['status'] == 'pass'
    assert out['health'] in {'pass', 'pass_with_warnings'}
    assert out['distribution_mode'] in {'template', 'working_snapshot'}


def test_tool_plan_sequences_include_governance_guards():
    out = json.loads(run('tool-plan', 'أضف ملف جديد يشرح نفس المفهوم الموجود'))
    cmds = [s['cmd'] for s in out['sequence']]
    assert 'duplicate-scan' in cmds
    assert 'impact-scan' in cmds
    assert 'safe-write' in cmds
