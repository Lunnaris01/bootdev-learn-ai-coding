# AGENTS.md

SlopLang tree-walking interpreter. Pipeline: `sloperator/lexer/` (text→tokens)
→ `sloperator/parser/` (tokens→AST) → `sloperator/evaluator/` (walks the AST).
`sloperator/runner.py` wires the stages; `sloperator.py` is the CLI entrypoint.
`sloperator/parser/AGENTS.md` has parser-specific style rules.

## Validation

```bash
uv run pytest -q                            # full suite (add -k to focus)
uv run pytest tests/test_comparisons.py -q  # single file, e.g. comparison tests
uv run ruff format --check                  # formatting (line-length 100)
uv run ruff check                           # linting
uv run ty check                             # type checking
```

Always run via `uv` (never bare `python`); Python >= 3.13.
Run `uv run ruff format` after any code change so formatting never drifts.

## Regression tests

Add one when fixing a bug or changing language behavior. Use
`runner.run_source()` in-process and assert the exact outcome:

- error cases: `result.stderr == "SlopLang {lexical|syntax|runtime} error at line N: msg\n"`
  with `exit_code == 1` (see `tests/test_errors.py`);
- lexer-only cases: `pytest.raises(LexicalError)` via `tokenize`
  (see `tests/test_lexer.py`, `tests/test_lexer_regression.py`).
- Only `tests/test_cli.py` uses subprocess (CLI exit codes 0/1/2).

## Language behavior

`docs/spec.md` is the contract — check it before implementing or disputing
behavior, and update it when the language changes. Keep `README.md` short;
it links to the spec instead of describing the language.
