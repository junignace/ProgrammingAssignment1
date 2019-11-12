import string

def getGuessedWord(secretWord, lettersGuessed):
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word = word+ x
        else:
            word = word + '_ '
            
    return word


def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    word1 = ' '
    for x in letters:
        if x in lettersGuessed:
            word1 = word1 + ''
        else: 
            word1 = word1 + x
        
            
    return word1





def Hangaroo(secretWord):
    print('The secret word contains', len(secretWord), 'letters') #Describes how many numbers there is
    print('You can only have 5 wrong guesses')
    lettersGuessed = [] # Inventory for lettersGuessed
    word= ''
    miss= 0
    guess = False #set the guess to false first so that if it becomes true it exits the loop
    while guess == False:
        if all(x in lettersGuessed for x in secretWord): #if every elements in x are in the word then it becomes true
            guess = True
            break
        
        k= input('Letters: ')
        k= k.lower()
        
        if k in secretWord and k not in lettersGuessed:
            lettersGuessed.insert(0,k) # Adds letters to list inventory
            print('Nice, the letter is in the word')
            print('The available letters are', getAvailableLetters(lettersGuessed))
        elif k in secretWord and k in lettersGuessed:
            print('You have already entered that letter')
            print('The available letters are', getAvailableLetters(lettersGuessed))
            
        else:
            lettersGuessed.insert(0,k)
            print('Too bad, the letter is not in the word')
            print('The available letters are', getAvailableLetters(lettersGuessed))
            miss += 1 #wrong letter adds counter
            if miss == 5:
                break
        
        
    
    if guess == True:
        print('Congratulations, you have guessed the word', getGuessedWord(secretWord,lettersGuessed))
        
    else: 
        print('I am sorry but you have only guessed, ', getGuessedWord(secretWord,lettersGuessed), 'please try again later, GAME OVER' )
    
    
    
            
    
            
            
            