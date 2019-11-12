import string

def getAvailableLetters(lettersGuessed):
    letters = string.ascii_lowercase
    fin = ''
    for x in letters:
        if x in lettersGuessed:
            fin = fin + ''
        else: 
            fin = fin + x
        
            
    return fin
        
    
        