#!/usr/bin/env python3
from pathlib import Path
import re, sys

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
failures = []

def check(cond, msg):
    if not cond:
        failures.append(msg)

# Required root entry and general layers
for path in [
    '00_AI_REPOSITORY_BOOTSTRAP.md',
    '00_ENTRY_MAP.md',
    'ENGINEER_ENTRY_PROTOCOL.md',
    '00_TUNNEL_EXECUTION_COMMANDS.yaml',
    '00_COGNITIVE_RUNTIME',
    '01_PROJECT_ORCHESTRATION',
    '02_MY_PROJECT',
]:
    check((ROOT/path).exists(), f'missing required root/layer path: {path}')

# General enforcement gates must exist
for path in [
    '01_PROJECT_ORCHESTRATION/22_REPOSITORY_STRUCTURAL_TRANSFORMATION_AND_CODEBASE_INTEGRATION_GATE.md',
    '01_PROJECT_ORCHESTRATION/23_TARGET_REPOSITORY_TOPOLOGY_CONTRACT_GATE.md',
    '01_PROJECT_ORCHESTRATION/24_TASK_EXECUTION_PLAN_AND_DELIVERY_CONFORMANCE_GATE.md',
    '01_PROJECT_ORCHESTRATION/25_PROTOCOL_ENFORCEMENT_AND_NON_SLOGAN_RUNTIME_GATE.md',
]:
    check((ROOT/path).exists(), f'missing enforcement gate: {path}')

# Command boards must reference the enforcement gates
cmd_file = ROOT/'00_TUNNEL_EXECUTION_COMMANDS.yaml'
orch_board = ROOT/'01_PROJECT_ORCHESTRATION'/'18_PROJECT_EXECUTION_GATES.yaml'
if yaml and cmd_file.exists():
    try:
        data = yaml.safe_load(cmd_file.read_text(encoding='utf-8'))
        commands = data.get('commands', {})
        check('TASK_EXECUTION_PLAN_AND_DELIVERY_CONFORMANCE' in commands, 'root command board missing TASK_EXECUTION_PLAN_AND_DELIVERY_CONFORMANCE')
        check('PROTOCOL_ENFORCEMENT_NON_SLOGAN' in commands, 'root command board missing PROTOCOL_ENFORCEMENT_NON_SLOGAN')
    except Exception as e:
        failures.append(f'root command board YAML parse failed: {e}')
elif cmd_file.exists():
    text = cmd_file.read_text(encoding='utf-8', errors='ignore')
    check('TASK_EXECUTION_PLAN_AND_DELIVERY_CONFORMANCE' in text, 'root command board missing task execution command text')
    check('PROTOCOL_ENFORCEMENT_NON_SLOGAN' in text, 'root command board missing protocol enforcement command text')

if yaml and orch_board.exists():
    try:
        data = yaml.safe_load(orch_board.read_text(encoding='utf-8'))
        gates = data.get('gates', {})
        activation = data.get('activation_order', [])
        check('task_execution_plan_and_delivery_conformance' in gates, 'orchestration board missing task execution gate')
        check('protocol_enforcement_non_slogan' in gates, 'orchestration board missing protocol enforcement gate')
        check('task_execution_plan_and_delivery_conformance' in activation, 'orchestration activation order missing task execution gate')
        check('protocol_enforcement_non_slogan' in activation, 'orchestration activation order missing protocol enforcement gate')
    except Exception as e:
        failures.append(f'orchestration command board YAML parse failed: {e}')

# 02_MY_PROJECT is container; project folders are actual projects
paz = ROOT/'02_MY_PROJECT'/'pazarat'
if paz.exists():
    check((paz/'00_PROJECT_TUNNEL').is_dir(), 'Pazarat project missing 00_PROJECT_TUNNEL')
    check((paz/'docs').is_dir(), 'Pazarat project missing docs')
    check((paz/'backend').is_dir(), 'Pazarat project missing backend')
    check((paz/'frontend').is_dir(), 'Pazarat project missing frontend')
    check((paz/'database').is_dir(), 'Pazarat project missing database')
    check((paz/'00_PROJECT_TUNNEL'/'19_PAZARAT_TASK_EXECUTION_AND_DELIVERY_CONFORMANCE_STANDARD.md').exists(), 'Pazarat missing local task execution standard')
    check((paz/'00_PROJECT_TUNNEL'/'_execution').is_dir(), 'Pazarat missing _execution folder')
    for ex in [
        'CURRENT_TASK_LEDGER.yaml',
        'TASK_EXECUTION_PLAN.template.yaml',
        'DELIVERY_CONFORMANCE_REPORT.template.md',
        'DONE_DEFINITION.md',
    ]:
        check((paz/'00_PROJECT_TUNNEL'/'_execution'/ex).exists(), f'Pazarat execution control missing {ex}')
    check(not (ROOT/'02_MY_PROJECT'/'backend').exists(), 'backend must not be placed directly under 02_MY_PROJECT')
    check(not (ROOT/'02_MY_PROJECT'/'frontend').exists(), 'frontend must not be placed directly under 02_MY_PROJECT')
    check(not (ROOT/'02_MY_PROJECT'/'database').exists(), 'database must not be placed directly under 02_MY_PROJECT')
    check(not (paz/'docs'/'ai_tunnel').exists(), 'forbidden docs/ai_tunnel')
    for old in ['A_dashboards','B_web_frontend','C_mobile_app']:
        check(not (paz/old).exists(), f'old docs root should not remain at project root: {old}')
        check((paz/'docs'/old).exists(), f'migrated docs branch missing: docs/{old}')

# No conflict markers
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in ['.md','.yaml','.yml','.txt','.cs','.csproj','.sln','.json','.ps1','.sh']:
        text = p.read_text(encoding='utf-8', errors='ignore')
        if '<<<<<<< ' in text or '=======' in text or '>>>>>>> ' in text:
            failures.append(f'conflict marker found in {p.relative_to(ROOT)}')

# General layers must not carry named-project or stack-specific terms
upper = [ROOT/'00_COGNITIVE_RUNTIME', ROOT/'01_PROJECT_ORCHESTRATION', ROOT/'00_ENTRY_MAP.md', ROOT/'ENGINEER_ENTRY_PROTOCOL.md']
for base in upper:
    files = base.rglob('*') if base.is_dir() else [base]
    for p in files:
        if p.is_file() and p.suffix.lower() in ['.md','.yaml','.yml','.txt']:
            text = p.read_text(encoding='utf-8', errors='ignore')
            if re.search(r'\bPazarat\b|\bpazarat\b|بازارات|ASP\.NET|Next\.js|PostgreSQL', text):
                failures.append(f'project-specific term leaked into general layer: {p.relative_to(ROOT)}')

if failures:
    print('FAIL')
    for f in failures: print('-', f)
    sys.exit(1)
print('OK: tunnel integrity, task enforcement, and project-container boundaries are valid')
