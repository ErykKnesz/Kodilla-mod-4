def palindrom_check():
    '''Returns True if the input string spelled backwards is the same as spelled forwards,
    otherwise returns False:
    e.g attribute lol == True
    roftl == False'''
    word=input("Please provide your word or phrase: ").lower()
    letters = []
    letters_2 = []
    for i in word:
        if i.isalpha() == False:
            pass
        else:
            letters.append(i)
    for i_2 in word[::-1]:
        if i_2.isalpha() == False:
            pass
        else:
            letters_2.append(i_2)
    if letters == letters_2:
        return True
    else:
        return False
    
    
print(palindrom_check())
