from zad_3 import count_status


def test_count_status():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    assert count_status(statuses, "online") == 2
    assert count_status(statuses, "offline") == 1
    assert count_status(statuses, "xxx") == 0
