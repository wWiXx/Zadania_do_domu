from zad_5 import is_anagram


def test_is_anagram():
    assert is_anagram("typhoon", "opython") == True
    assert is_anagram("Alice", "Bob") == False