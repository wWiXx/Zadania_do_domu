import string


def is_pangram(sentence):
    alfabet_polski = list("aąbcćdeęfghijklłmnńoóprsśtuwyzźż")
    print(alfabet_polski)
    interpunkcja = list(string.punctuation)

    print(sentence)
    non_spaces_sentence = sentence.replace(" ", "")
    print(non_spaces_sentence)
    non_inteerpunkcja = ""
    for i in non_spaces_sentence:
        if i in interpunkcja:
            pass
        else:
            non_inteerpunkcja += i

    print(non_inteerpunkcja)
    listed_non_spaces_sentence = []
    for i in non_inteerpunkcja:
        listed_non_spaces_sentence.append(i.lower())
    print(listed_non_spaces_sentence)
    length_to_check = []
    for i in listed_non_spaces_sentence:
        if i in alfabet_polski:
            length_to_check.append(i)
    return len(alfabet_polski) == len(length_to_check)


print(is_pangram("Pójdźże, kiń tę chmurność w głąb flaszy!"))
