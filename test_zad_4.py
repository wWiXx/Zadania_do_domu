from zad_4 import double_letters


def test_double_letters():
    assert double_letters("ala") == False
    assert double_letters("Hello") == True
    assert double_letters("abc") == False
    assert double_letters("nono") == False