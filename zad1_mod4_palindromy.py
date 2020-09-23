def palindrom_check(word):
    '''Returns True if the string spelled backwards is the same as spelled forwards,
    otherwise returns False'''
    letters = []
    letters_2 = []
    for i in word:
        letters = letters.append(i)
    for i_2 in word[-1]:
        letters_2 = letters_2.append(i_2)
    if letters == letters_2:
        return True
    else:
        return False
palindrom_check(word)