from zad_12 import perfect_number


def test_perfect_number():
    assert perfect_number(6) == True
    assert perfect_number(8128) == True
    assert perfect_number(818) == False