# This program plays hangman!

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in range(0,len(secretWord)):
        if secretWord[x] not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    outstring = ''
    for x in range(0,len(secretWord)):
        if secretWord[x] in lettersGuessed:
            outstring += secretWord[x]
        else:
            outstring += '_'
    return outstring

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availletters = ''
    for x in string.ascii_lowercase:
        if x not in lettersGuessed:
            availletters += x
    return availletters


def isLetterinWord(secretWord, guess):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if letter appears in secretWord are in lettersGuessed;
      False otherwise
    '''
    if guess in secretWord:
        return True
    return False

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
    print('Welcome to the game, Hangman!')

    secretWord = secretWord.lower()
    print('I am thinking of a word that is '+ str(len(secretWord)) +' letters long.')

    guesses = 8
    lettersGuessed = []
    while guesses > -1:
        print('-------------')

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        elif guesses == 0:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break

        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))

        guess = raw_input('Please guess a letter: ')

        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter:" + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += guess
            if isLetterinWord(secretWord, guess):
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                guesses -= 1
                
# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder 
# input cases.

def isLetterinWord(secretWord, guess):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if letter appears in secretWord are in lettersGuessed;
      False otherwise
    '''
    if guess in secretWord:
        return True
    return False

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
    print('Welcome to the game, Hangman!')

    secretWord = secretWord.lower()
    print('I am thinking of a word that is '+ str(len(secretWord)) +' letters long.')

    guesses = 8
    lettersGuessed = []
    while guesses > -1:
        print('-------------')

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        elif guesses == 0:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break

        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))

        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()

        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter:" + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += guess
            if isLetterinWord(secretWord, guess):
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                guesses -= 1
