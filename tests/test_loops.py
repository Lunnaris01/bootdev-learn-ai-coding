from sloperator.runner import run_source


def test_loop_with_false_condition_runs_zero_times():
    result = run_source("ralph ❌ {\n    hallucinate(“never”)✨\n}")
    assert result.exit_code == 0
    assert result.stdout == ""
    assert result.stderr == ""
