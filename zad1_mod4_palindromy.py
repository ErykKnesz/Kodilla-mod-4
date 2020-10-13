word = "Do geese see God?"


def palindrom_check(word):
    '''Returns True if the string in variable word
    spelled backwards is the same as spelled forwards,
    otherwise returns False:
    e.g attribute lol == True
    roftl == False'''
    letters = []
    letters_2 = []
    for letter in word.lower():
        if letter.isalpha() is False:
            pass
        else:
            letters.append(letter)
    for letter_2 in word[::-1].lower():
        if letter_2.isalpha() is False:
            pass
        else:
            letters_2.append(letter_2)
    if letters == letters_2:
        return True
    else:
        return False


print(palindrom_check(word))
