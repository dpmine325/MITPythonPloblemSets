# -*- coding: utf-8 -*-

def isWordGuessed(secretWord, lettersGuessed):

    for s in secretWord:
        if s not in lettersGuessed:
            return False
        
    return True
