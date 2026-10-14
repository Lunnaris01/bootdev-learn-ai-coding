---
name: create-test-program
description: Create a SlopLang example program and its exact-output test for a language feature
---

# Create Test Program

Given a language feature, do all three steps in order:

1. Read `docs/spec.md` and confirm the feature's exact syntax, semantics,
   and printed output form (booleans print as `✅`/`❌`, `hallucinate` adds
   a newline per call). If the spec does not cover the feature, stop and
   say so instead of guessing.
2. Write an example program in `examples/` (lowercase-hyphen filename,
   e.g. `examples/while-loop.slop`). It must use only spec-covered syntax
   and run cleanly: `uv run sloperator.py examples/<name>.slop`.
3. Add an exact-output test for it in `tests/test_example_outputs.py`
   using `runner.run_source()` on the same source (or by reading the
   example file). Assert `exit_code == 0`, the full `stdout` string, and
   `stderr == ""`.

Then run `uv run pytest tests/test_example_outputs.py -q` and
`uv run ruff format` on the touched files.
