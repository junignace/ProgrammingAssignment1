def getGuessedWord (secretWord, lettersGuessed):
    list(secretWord)
    
    if all(x in secretWord for x in lettersGuessed):
        return True
    else:
        return False
