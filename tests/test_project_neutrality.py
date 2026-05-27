from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _t(*parts):
    return ''.join(parts)

FORBIDDEN = [
    _t('Paza','rat'), _t('paz','arat'), _t('User ','Management'), _t('Admin ','Dashboard'),
    _t('Roles ','Permissions'), _t('B','2B'), _t('B','2C'), _t('sel','ler'), _t('sel','lers'),
    _t('or','ders'), _t('pay','ments'), _t('log','istics'), _t('market','place'), _t('بازا','رات'), _t('با','زار'),
]
ALLOWED_DIR_PREFIXES = ('02_WORKSHOP/ACTIVE_PROJECT/', '.engineer/indexes/', '.engineer/ledgers/', '.engineer/state/', '.pytest_cache/')

def test_engineer_runtime_has_no_project_specific_terms():
    violations = []
    for p in ROOT.rglob('*'):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(('.git/', '__pycache__/', '.pytest_cache/')):
            continue
        if rel.startswith(ALLOWED_DIR_PREFIXES):
            continue
        if p.suffix.lower() not in {'.md','.txt','.yaml','.yml','.json','.py','.toml'}:
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        for term in FORBIDDEN:
            if term in text:
                violations.append((rel, term))
    assert not violations, violations[:20]

def test_active_project_boundary_is_valid():
    active = ROOT / '02_WORKSHOP' / 'ACTIVE_PROJECT'
    files = [p.relative_to(active).as_posix() for p in active.rglob('*') if p.is_file()]
    assert '.keep' in files or files
    # Template packages may ship empty; working packages may include a real project.
    # In both cases, project-specific terms are allowed only under ACTIVE_PROJECT, not static runtime.
