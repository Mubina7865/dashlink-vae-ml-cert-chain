from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_DIRS = [
    "requirements",
    "data/raw", "data/splits", "data/slices",
    "src/model", "src/pipeline", "src/coverage", "src/explain", "src/traceability",
    "tests", "artifacts", "reports", "docs",
    ".github/workflows",
]

def test_repo_layout():
    missing = [d for d in EXPECTED_DIRS if not (ROOT / d).is_dir()]
    assert not missing, f"Missing directories: {missing}"
