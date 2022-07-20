slowo = "Ile Roman ładny dyndał na moreli"


def is_palindrome(word):
    non_spaces_word = word.replace(" ", "")
    listed_word = []
    for i in non_spaces_word:
        listed_word.append(i.lower())

    word_done = "".join(listed_word)
    print("Słowo: ", word_done)

    listed_word.reverse()
    reversed_word_done = "".join(listed_word)
    print("Odwrócone słowo: ", reversed_word_done)
    
    return word_done == reversed_word_done



print(is_palindrome(slowo))
