from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ENGINEER=ROOT/'.engineer'/'commands'/'engineer.py'

def test_maturity_features_are_registered_and_neutral():
    text=ENGINEER.read_text(encoding='utf-8')
    assert 'def build_maturity_map' in text
    assert 'def answer_receipt' in text
    assert 'sub.add_parser("maturity-map")' in text
    assert 'sub.add_parser("placeholder-scan")' in text
    assert 'sub.add_parser("answer-receipt")' in text
    assert 'maturity is based on semantic evidence, not file size' in text
    for term in ['SPECIFIC_PROJECT_NAME_EXAMPLE','SPECIFIC_MODULE_EXAMPLE','SPECIFIC_STACK_EXAMPLE']:
        assert term not in text

def test_maturity_governance_files_exist():
    assert (ROOT/'.engineer'/'governance'/'maturity_evidence.yaml').exists()
    assert (ROOT/'.engineer'/'protocols'/'maturity_grounded_answer.yaml').exists()
    assert (ROOT/'.engineer'/'reference'/'v6_8_maturity_truth_notes.md').exists()

def test_placeholder_scan_logic_is_content_based():
    text=ENGINEER.read_text(encoding='utf-8')
    assert 'semantic_placeholder_status' in text
    assert 'density_score' in text
    assert 'File size is not maturity' in (ROOT/'.engineer'/'reference'/'v6_8_maturity_truth_notes.md').read_text(encoding='utf-8')
