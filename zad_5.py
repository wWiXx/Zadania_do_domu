word1 = "mąka"
word2 = "knmą"


def is_anagram(word1, word2):
    lista_slowa_2 = list(word2)
    lista_slowa_1 = list(word1)
    lista_odwroconego_slowa_1 = []
    for i in lista_slowa_1:
        if i in lista_slowa_2:
            lista_odwroconego_slowa_1.append(i)
    if len(lista_odwroconego_slowa_1) == len(lista_slowa_2):
        return True
    else:
        return False


print(is_anagram(word1, word2))

