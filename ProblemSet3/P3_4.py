def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is {} letters long.". format(len(secretWord)))
    #print(secretWord)  ####
    
    guessingWord =''
    lettersGuessed = []
    i=8
    
    while (i>0):
        print ("-----------")
        print ("You have {} guesses left".format(i))
        availableLetters = getAvailableLetters(lettersGuessed)
        print ("Available letters: " + availableLetters)
        guessInput=input ("Please guess a letter:")
        guessInputLower = guessInput.lower()
        
        if guessInputLower in lettersGuessed:
            print("Oops! You've already guessed that letter: " + guessingWord)
            continue
                
        lettersGuessed.append(guessInputLower)
        guessingWord = getGuessedWord(secretWord, lettersGuessed)
        
        t = secretWord.find(guessInputLower)
        if t== -1:
            print ("Oops! That letter is not in my word: " + guessingWord)
            i-=1
        else:
            print ("Good guess: " + guessingWord)

        if isWordGuessed(secretWord, guessingWord):
            print ("-----------")
            print ("Congratulations, you won!")
            break

    if not isWordGuessed(secretWord, guessingWord):    
        print ("Sorry, you ran out of guesses. The word was " + secretWord)