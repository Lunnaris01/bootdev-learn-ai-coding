import pytest

from sloperator.errors import LexicalError
from sloperator.lexer import tokenize


@pytest.mark.parametrize("source", ["$", "#", "@", "slop x = @✨"])
def test_unexpected_character_fallthrough(source: str):
    with pytest.raises(LexicalError) as info:
        tokenize(source)
    (bad_char,) = [ch for ch in source if ch in "$@#"]
    assert info.value.line == 1
    assert info.value.message == f"unexpected character '{bad_char}'"
    assert str(info.value) == f"SlopLang lexical error at line 1: unexpected character '{bad_char}'"
