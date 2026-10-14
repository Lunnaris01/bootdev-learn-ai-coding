---
name: create-and-validate
description: Create a SlopLang example program with tests, then run full validation
---

# Create and Validate

Given a language feature, run these two skills in order via the `skill` tool.
Follow their instructions as written; do not reimplement them here.

1. Load `create-test-program` and complete its workflow (spec check, example
   in `examples/`, exact-output test in `tests/test_example_outputs.py`).
2. Load `validate` and run all four checks (tests, formatting, lint, types).

If either skill fails, stop and report the failure before proposing fixes.
