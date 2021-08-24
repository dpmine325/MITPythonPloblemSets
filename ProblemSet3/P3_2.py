def getGuessedWord(secretWord, lettersGuessed):

    printString =''
    for s in secretWord:
        if s not in lettersGuessed:
            printString +="_"
            
        else:
            printString +=s
            
        printString += " "
    
    return printString