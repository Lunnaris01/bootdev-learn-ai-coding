from pathlib import Path

from sloperator.runner import run_source


def test_equality_example_output():
    source = Path("examples/equality.slop").read_text(encoding="utf-8")
    result = run_source(source)
    assert result.exit_code == 0
    assert result.stdout == "✅\n❌\n❌\n"
    assert result.stderr == ""


def test_short_circuit_example_output():
    source = Path("examples/short-circuit.slop").read_text(encoding="utf-8")
    result = run_source(source)
    assert result.exit_code == 0
    assert result.stdout == "❌\n✅\n"
    assert result.stderr == ""
