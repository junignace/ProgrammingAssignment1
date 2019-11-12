def getGuessedWord(secretWord, lettersGuessed):
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word = word+ x
        else:
            word = word + '_ '
            
    print(word)