import unmatched
from unmatched import core


def test_package_imports() -> None:
    assert unmatched.__version__ == "0.1.0"


def test_core_subpackage_imports() -> None:
    assert core.__name__ == "unmatched.core"
