import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ENGINEER=ROOT/'.engineer/commands/engineer.py'

def run_cmd(*args):
    return subprocess.check_output([sys.executable, str(ENGINEER), *args], cwd=ROOT, text=True)

def test_context_pack_exists_and_respects_project_boundary():
    data=json.loads(run_cmd('context-pack','--scope','project'))
    assert data['scope']=='project'
    assert 'category_counts' in data
    assert 'usage_contract' in data
    active_files=[p for p in (ROOT/'02_WORKSHOP'/'ACTIVE_PROJECT').rglob('*') if p.is_file() and p.name != '.keep']
    raw=json.dumps(data, ensure_ascii=False)
    forbidden=['Paz'+'arat','User '+'Management','ASP'+'.NET','Postgre'+'SQL','Next'+'.js']
    if not active_files:
        for term in forbidden:
            assert term not in raw
    else:
        # When a real active project is inserted, the context pack must surface its truth.
        assert data['category_counts']

def test_surface_check_blocks_meta_opening():
    data=json.loads(run_cmd('surface-check','سأتعامل مع سؤالك كمساعد تقني ثم أفحص ملف المشروع'))
    assert data['status']=='fail'
    assert data['hits']

def test_one_page_generates_evidence_file():
    data=json.loads(run_cmd('one-page','--scope','project'))
    assert data['written'].endswith('project_one_page_evidence.md')
    assert (ROOT/data['written']).exists()
