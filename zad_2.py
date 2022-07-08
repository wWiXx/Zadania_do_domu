def mid(word):
    if len(word) % 2 != 0:
        # print(word[round((len(word)/ 2))])
        mid_index = round((len(word) / 2))
        return word[mid_index - 1]
    else:
        return ""


print(mid("abc"))
