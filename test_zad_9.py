from zad_9 import is_palindrome


def test_is_palindrome():
    assert is_palindrome("Ile Roman ładny dyndał na moreli") is True
    assert is_palindrome("kajak") is True
    assert is_palindrome("Ile romek") is False
