from sloperator.runner import run_source


def test_call_used_directly_as_argument():
    result = run_source(
        "clanker add(left, right) {\n"
        "    ship left + right✨\n"
        "}\n"
        "clanker double(n) {\n"
        "    ship n * 2✨\n"
        "}\n"
        "hallucinate(add(double(3), double(4)))✨\n"
    )
    assert result.exit_code == 0
    assert result.stdout == "14\n"
