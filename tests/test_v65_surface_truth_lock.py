import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = ROOT / '.engineer' / 'commands' / 'engineer.py'


def run(*args):
    return subprocess.check_output([sys.executable, str(ENG), *args], cwd=ROOT, text=True)


def test_surface_answer_hides_runtime_and_scores_when_project_empty():
    out = run('answer', 'اخبرني عنك من انت وما عملك مع مشروعي وتقييمك الحالي')
    forbidden = ['GPT', 'مساعد ذكاء', '.engineer', 'إطار تشغيل', 'اختبارات', '/10']
    assert not any(x in out for x in forbidden), out
    assert 'مهندس مشروعك' in out
    # If a real project is inserted, the answer should reflect evidence instead of formation.
    assert ('نقطة البداية' in out or 'تكوين' in out or 'ما يثبته الفحص الحالي' in out or 'مادة مشروع فعلية' in out)


def test_surface_policy_check_flags_bad_answer():
    bad = 'أنا مساعد ذكاء اصطناعي، وبيئة العمل 8/10، والاختبارات نجحت.'
    out = json.loads(run('surface-check', bad))
    assert out['status'] == 'fail'


def test_claim_check_flags_unsupported_scoring_and_identity():
    bad = 'أنا مساعد ذكاء اصطناعي. جاهزية بيئة العمل 8/10.'
    out = json.loads(run('claim-check', bad))
    assert out['status'] == 'fail'
    assert any(p['type'] == 'surface_policy_violation' for p in out['problems'])
