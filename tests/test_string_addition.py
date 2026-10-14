import pytest

from sloperator.runner import run_source


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("hallucinate(“a” + “b”)✨", "ab\n"),
        ("hallucinate(“” + “x”)✨", "x\n"),
        ("hallucinate(1 + 2)✨", "3\n"),
    ],
)
def test_plus_adds_numbers_and_concatenates_strings(source: str, expected: str):
    result = run_source(source)
    assert result.exit_code == 0
    assert result.stdout == expected
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("source", "got"),
    [
        ("hallucinate(“a” + 1)✨", "string and number"),
        ("hallucinate(1 + “a”)✨", "number and string"),
    ],
)
def test_plus_rejects_mixed_operands(source: str, got: str):
    result = run_source(source)
    assert result.exit_code == 1
    assert result.stderr == (
        f"SlopLang runtime error at line 1: "
        f"operands of '+' must both be numbers or both be strings, got {got}\n"
    )
