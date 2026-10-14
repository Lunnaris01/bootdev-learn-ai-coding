# sloperator/parser — AGENTS.md

## One method per grammar rule

Each EBNF rule in `docs/spec.md` maps to exactly one `Parser` method
(`expression` → `logic_or` → `logic_and` → … → `call` → `primary`).
When adding syntax, add the grammar rule to the spec and a same-named method
here — never fold two rules into one method or split a rule across methods.
Statement-level rules live in `statement()`/`declaration()`/`top_level()`.

## Syntax errors name the token found

Build errors via `self.error(token, message)` or `self.expect(...)`, which
append `, found '<lexeme>'` automatically. Never raise a bare message that
omits what was actually found — e.g. prefer
`expected ✨ after variable declaration, found 'slop'`.
