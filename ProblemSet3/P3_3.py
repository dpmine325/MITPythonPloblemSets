
def getAvailableLetters(lettersGuessed):

    import string
    lowerCase = string.ascii_lowercase
    notInGueesed = ''
    for s in lowerCase:
        if s not in lettersGuessed:
            notInGueesed +=s
    
    return notInGueesed