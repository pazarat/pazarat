#!/usr/bin/env python3
from pathlib import Path
import re, sys

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
failures = []

def check(cond, msg):
    if not cond:
        failures.append(msg)

check((REPO/'00_ENTRY_MAP.md').exists(), 'missing repository root entry 00_ENTRY_MAP.md')
check((REPO/'00_COGNITIVE_RUNTIME').is_dir(), 'missing general runtime layer')
check((REPO/'01_PROJECT_ORCHESTRATION').is_dir(), 'missing general orchestration layer')
check((REPO/'02_MY_PROJECT').is_dir(), 'missing project-instance container')
check(ROOT.name == 'pazarat', 'verifier must live inside the actual pazarat project folder')
check((ROOT/'00_PROJECT_TUNNEL').is_dir(), 'missing Pazarat local tunnel folder 00_PROJECT_TUNNEL')
check((ROOT/'docs').is_dir(), 'missing Pazarat docs root inside project')
check((ROOT/'backend').is_dir(), 'missing Pazarat backend inside project')
check((ROOT/'frontend').is_dir(), 'missing Pazarat frontend inside project')
check((ROOT/'database').is_dir(), 'missing Pazarat database inside project')
check(not (REPO/'02_MY_PROJECT'/'backend').exists(), 'backend incorrectly placed at 02_MY_PROJECT/backend')
check(not (REPO/'02_MY_PROJECT'/'frontend').exists(), 'frontend incorrectly placed at 02_MY_PROJECT/frontend')
check(not (REPO/'02_MY_PROJECT'/'database').exists(), 'database incorrectly placed at 02_MY_PROJECT/database')
check(not (ROOT/'docs'/'ai_tunnel').exists(), 'forbidden docs/ai_tunnel found')

for old in ['A_dashboards','B_web_frontend','C_mobile_app']:
    check(not (ROOT/old).exists(), f'duplicate old docs root still exists: {old}')
    check((ROOT/'docs'/old).exists(), f'migrated docs missing: docs/{old}')

# Execution control must exist and be routable
TUNNEL = ROOT/'00_PROJECT_TUNNEL'
for path in [
    '19_PAZARAT_TASK_EXECUTION_AND_DELIVERY_CONFORMANCE_STANDARD.md',
    '_execution/README.md',
    '_execution/CURRENT_TASK_LEDGER.yaml',
    '_execution/TASK_EXECUTION_PLAN.template.yaml',
    '_execution/DELIVERY_CONFORMANCE_REPORT.template.md',
    '_execution/DONE_DEFINITION.md',
    '_routing/AI_PROJECT_WRITE_ROUTING.yaml',
    '_routing/PRD_TO_CODEBASE_ROUTING.yaml',
    '_routing/DOCUMENTATION_MIGRATION_MANIFEST.yaml',
]:
    check((TUNNEL/path).exists(), f'missing Pazarat execution/routing path: {path}')

# Local command board must include task execution gate and delivery conformance gate
local_board = TUNNEL/'12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml'
if yaml and local_board.exists():
    try:
        data = yaml.safe_load(local_board.read_text(encoding='utf-8'))
        gates = data.get('pazarat_gates', {})
        flow = data.get('entry_flow', [])
        check('pazarat_task_execution_plan_gate' in gates, 'Pazarat board missing task execution plan gate')
        check('pazarat_delivery_conformance_gate' in gates, 'Pazarat board missing delivery conformance gate')
        check('apply_pazarat_task_execution_plan_gate_before_non_trivial_work' in flow, 'Pazarat entry flow missing task plan step')
        check('apply_delivery_conformance_gate_before_delivery' in flow, 'Pazarat entry flow missing delivery conformance step')
    except Exception as e:
        failures.append(f'Pazarat runtime gates YAML parse failed: {e}')

# Routing file must explicitly identify execution targets
routing = TUNNEL/'_routing'/'AI_PROJECT_WRITE_ROUTING.yaml'
if yaml and routing.exists():
    try:
        data = yaml.safe_load(routing.read_text(encoding='utf-8'))
        wt = data.get('write_targets', {})
        check(wt.get('pazarat_execution_control') == '02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/_execution/', 'AI_PROJECT_WRITE_ROUTING missing execution control write target')
        check('execution_rules' in data, 'AI_PROJECT_WRITE_ROUTING missing execution_rules')
    except Exception as e:
        failures.append(f'AI_PROJECT_WRITE_ROUTING YAML parse failed: {e}')

# inspect conflicts and forbidden upper project terms
for p in REPO.rglob('*'):
    if p.is_file() and p.suffix in ['.md','.yaml','.yml','.txt','.csproj','.sln','.cs','.json','.ps1','.sh']:
        text = p.read_text(encoding='utf-8', errors='ignore')
        if '<<<<<<< ' in text or '=======' in text or '>>>>>>> ' in text:
            failures.append(f'conflict marker in {p.relative_to(REPO)}')

upper = [REPO/'00_COGNITIVE_RUNTIME', REPO/'01_PROJECT_ORCHESTRATION', REPO/'00_ENTRY_MAP.md', REPO/'ENGINEER_ENTRY_PROTOCOL.md']
for base in upper:
    files = base.rglob('*') if base.is_dir() else [base]
    for p in files:
        if p.is_file() and p.suffix in ['.md','.yaml','.yml','.txt']:
            text = p.read_text(encoding='utf-8', errors='ignore')
            if re.search(r'\bPazarat\b|\bpazarat\b|بازارات|ASP\.NET|Next\.js|PostgreSQL', text):
                failures.append(f'project-specific term leaked into general layer: {p.relative_to(REPO)}')

# sln references existing csproj
sln = ROOT/'backend'/'Pazarat.sln'
if sln.exists():
    text = sln.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'"([^"]+\.csproj)"', text):
        ref = m.group(1).replace('\\','/')
        check((sln.parent/ref).exists(), f'solution references missing csproj: {ref}')
else:
    failures.append('missing backend/Pazarat.sln')

if failures:
    print('FAIL')
    for f in failures: print('-', f)
    sys.exit(1)
print('OK: Pazarat topology, task execution enforcement, routing, and backend references are valid')
