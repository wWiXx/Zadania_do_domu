def double_letters(word):
    list_word = []
    for i in word:
        list_word.append(i)
    i = 0
    for _ in list_word:
        length_of_list_minus_one = len(list_word) - 1
        if i < length_of_list_minus_one:
            if list_word[i] == list_word[i + 1]:
                return True
            i += 1
    return False


print(double_letters("nono"))
