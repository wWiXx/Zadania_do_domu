from zad_1 import format_number


def test_format_number():
    assert format_number(1000000) == "1,000,000"
