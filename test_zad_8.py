from zad_8 import sumator


def test_sumator():
    slownik = {
        "4": "4",
        2: 5,
        5: 6,
        6: "napis"
    }
    lista = [4, 5, "7", "napis"]
    tupla = (4, 5, "8", "napis")
    zbior = {4, 5, "9", "napis"}
    assert sumator(slownik) == 15
    assert sumator(lista) == 16
    assert sumator(tupla) == 17
    assert sumator(zbior) == 18
