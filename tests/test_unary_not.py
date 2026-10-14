import pytest

from sloperator.runner import run_source


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("hallucinate(!✅)✨", "❌\n"),
        ("hallucinate(!❌)✨", "✅\n"),
        ("hallucinate(!!✅)✨", "✅\n"),
    ],
)
def test_unary_not_flips_booleans(source: str, expected: str):
    result = run_source(source)
    assert result.exit_code == 0
    assert result.stdout == expected
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("source", "got"),
    [
        ("hallucinate(!1)✨", "number"),
        ("hallucinate(!“no”)✨", "string"),
    ],
)
def test_unary_not_rejects_non_booleans(source: str, got: str):
    result = run_source(source)
    assert result.exit_code == 1
    assert result.stderr == (
        f"SlopLang runtime error at line 1: operand of unary '!' must be a boolean, got {got}\n"
    )
