statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def count_status(statuses, status_to_check):
    number = 0
    for i in statuses:
        if statuses[i] == status_to_check:
            number += 1
    return number


print(count_status(statuses, "xxx"))
