# Sloperator

A tree-walking interpreter for [SlopLang](docs/spec.md), written in Python.

```bash
uv run sloperator.py examples/hello.slop   # run a program
uv run sloperator.py --check path/to/program.slop  # syntax check only
```

```bash
uv run pytest              # tests
uv run ruff format --check # formatting
uv run ruff check          # linting
uv run ty check            # type checking
```

## Example

```slop
clanker describe(count) {
    vibe count > 1 {
        ship “big slop”✨
    } nah {
        ship “small slop”✨
    }
}
hallucinate(describe(3))✨
```

See [docs/spec.md](docs/spec.md) for the full language reference
(keywords, values, operators, grammar, and error format).

## Layout

| Path                    | What it is                                           |
| ----------------------- | ---------------------------------------------------- |
| `sloperator.py`         | Command-line entrypoint                              |
| `sloperator/lexer/`     | Source text to tokens                                |
| `sloperator/parser/`    | Tokens to AST (`ast.py` holds the node definitions)  |
| `sloperator/evaluator/` | Walks the AST: values, environments, the interpreter |
| `sloperator/runner.py`  | Runs source through all three stages                 |
| `examples/`             | Example programs                                     |
| `tests/`                | Pytest suite                                         |
| `playground/`           | Tiny web server and editor page (`server.py`)        |
