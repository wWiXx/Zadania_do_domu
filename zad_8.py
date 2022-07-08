slownik = {
    "4": "4",
    2: 5,
    5: 6
}
lista = [4, 5, "7"]
tupla = (4, 5, "8")
zbior = {4, 5, "9"}


def sumator(sth):
    sum_of_values = 0
    if type(sth) == dict:
        for i in sth:
            try:
                sum_of_values += int(sth[i])
            except ValueError:
                pass
        return sum_of_values
    else:
        for i in sth:
            try:
                sum_of_values += int(i)
            except ValueError:
                pass
        return sum_of_values


print(sumator(zbior))
