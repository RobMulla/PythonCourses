# This is a scrabble game what allows users to see the best solutions
# This project was completed for MITx 6.00.1x
# Some code was provided 

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    for x in range(len(word)): # For each letter add the score
        score += SCRABBLE_LETTER_VALUES[word[x]]
    score *= len(word) # Multiply by word length
    if len(word) == n: # check to see if all letters used and add 50 pt bonus
        score += 50
    return score
    
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handnew = hand.copy()
    for i in range(len(word)):
        handnew[word[i]] -= 1
    return handnew

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    wordtest = word
    handworking = hand.copy()
    for x in range(len(wordtest)):
        if handworking.get(wordtest[x], -1) < 0:
            return False # Check to make sure letter is in word
        else:
            handworking[wordtest[x]] -= 1
            if handworking[wordtest[x]] < 0:
                return False  # Check to make sure letters remain
    if wordtest not in wordList: # See if word in wordlist
        return False
    return True

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for x in hand:
        count += hand[x]
    return count
    
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0  # Keep track of the total score

    handsize = n

    while n > 0:  # As long as there are still letters left in the hand:

        print "Current Hand:",
        displayHand(hand)  # Display the hand

        word = raw_input("""Enter word, or a "." to indicate that you are finished: """)  # Ask user for input

        if word == ".":  # If the input is a single period:

            break  # End the game (break out of the loop)

        else:  # Otherwise (the input is not a single period):

            if not isValidWord(word, hand, wordList):  # If the word is not valid:

                print "Invalid word, please try again."  # Reject invalid word (print a message followed by a blank line)

            else:  # Otherwise (the word is valid):

                score += getWordScore(word, handsize)

                print '"' + word + '"' + " earned " + str(getWordScore(word, handsize)) + " points. Total: " + str(score) + " points"
                print ""
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                hand = updateHand(hand, word)  # Update the hand
                n -= len(word)

    print "Run out of letters. Total score: " + str(score) + " points."  # Game is over (user entered a '.' or ran out of letters), so tell user the total score

            
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    
    maxscore = 0  # Create a new variable to store the maximum score seen so far (initially 0)

    bestword = None  # Create a new variable to store the best word seen so far (initially None)

    for word in wordList:  # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word,hand, wordList):
            iterscore = getWordScore(word, n)  # Find out how much making that word is worth

            if iterscore > maxscore: # If the score for that word is higher than your best score

                maxscore = iterscore # Update your best score, and best word accordingly
                bestword = word


    return bestword # return the best word you found.


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxscore = 0  # Create a new variable to store the maximum score seen so far (initially 0)

    bestword = None  # Create a new variable to store the best word seen so far (initially None)

    for word in wordList:  # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            iterscore = getWordScore(word, n)  # Find out how much making that word is worth

            if iterscore > maxscore:  # If the score for that word is higher than your best score

                maxscore = iterscore  # Update your best score, and best word accordingly
                bestword = word

    return bestword  # return the best word you found.


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # My code starts here

    totscore = 0
    bestword = compChooseWord(hand, wordList, n)
    handsize = n

    while bestword is not None:
        print "Current Hand: ",
        displayHand(hand)
        wordscore = getWordScore(bestword, handsize)
        totscore += wordscore
        print '"' + bestword + '"' + " earned " + str(wordscore) + " points. Total: " + str(totscore) + " points."
        print ""

        hand = updateHand(hand, bestword)
        n -= len(bestword)

        bestword = compChooseWord(hand, wordList, n)

    if sum(hand.values()) != 0:
        print "Current Hand: ",
        displayHand(hand)
    print "Total score: " + str(totscore) + " points."

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    n = HAND_SIZE
    hand = {}

    while True:
        doNext = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print ""
        if doNext == 'n':
            hand = dealHand(n)
            while True:
                player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if player == 'u':
                    playHand(hand,wordList,n)
                    break
                elif player == 'c':
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print "Invalid command."
                print ""

        elif doNext == 'r':
            if hand:
                while True:
                    player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if player == 'u':
                        playHand(hand, wordList, n)
                        break
                    elif player == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                        print "Invalid command."
                    print ""
            else:
                print "You have not played a hand yet. Please play a new hand first!"
        elif doNext == 'e':
            break
        else:
            print "Invalid command."
            print ""
