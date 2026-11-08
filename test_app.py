from app import add, subtract, is_palindrome


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_is_palindrome():
    assert is_palindrome("топот") is True
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("привет") is False