lista_do = [[1, 2], [[3, 4], [23, 24]], [5, 6], [7, 8], [9, 10]]


def flatten(lists_to_flatten):
    new_list = []
    for i in lists_to_flatten:
        new_list += i
    print(new_list)
    new_list_extended = []
    for lista in new_list:
        print(lista)
        if type(lista) is not int:
            new_list_extended.extend(lista)
        else:
            new_list_extended.append(lista)
    return new_list_extended


flatten(lista_do)
