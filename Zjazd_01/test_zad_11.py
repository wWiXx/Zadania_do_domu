from zad_11 import is_pangram


def test_is_pangram():
    assert is_pangram("Filmuj rzeź żądań, pość, gnęb chłystków!") == True
    assert is_pangram("Anna ma kota") == False