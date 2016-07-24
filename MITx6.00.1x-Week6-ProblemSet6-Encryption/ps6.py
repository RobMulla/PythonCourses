# This program was developed as a course project for MITx 6.00.1x - Intro to Computer Science in Python
# The program consists a class 'Messages' and subclasses 'PlaintextMessage' and 'CiphertextMessage'
# Used to encrypt and decrypt a message using the Caesar Cipher method
# The structure of the program was provided, including some functions and methods noted below
# The implementation of the major methods were written by me.

# This and other examples of my coding work can by found on my github.com/robmulla

import string

### DO NOT MODIFY THIS FUNCTION ###
## THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
### THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
### THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    ### THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    ### THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    ### THE FUNCTION BELOW WAS PROVIDED BY THE COURSE ##
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        #  MY CODE BELOW

        shift_dict = {}
        for x in range(26):
            if (x + shift) > 25:  # see if shifting will start at the beginning of ascii string
                shiftloop = x + shift - 26
                # print shiftloop
                shift_dict[string.ascii_uppercase[x]] = string.ascii_uppercase[shiftloop]
                shift_dict[string.ascii_lowercase[x]] = string.ascii_lowercase[shiftloop]
                # print shift_dict
            else:
                shift_dict[string.ascii_uppercase[x]] = string.ascii_uppercase[x + shift]
                shift_dict[string.ascii_lowercase[x]] = string.ascii_lowercase[x + shift]
                # print shift_dict
        return shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        #  MY CODE BELOW

        shiftedmessage = ''
        shiftdict = self.build_shift_dict(shift)
        for x in range(len(self.message_text)):
            if self.message_text[x] in string.ascii_letters:
                shiftedmessage += shiftdict[self.message_text[x]]
            else:
                shiftedmessage += self.message_text[x]
        return shiftedmessage

# Test Message class
# testmsg = Message('Testing the message class!! Shift. Method')
# print testmsg.apply_shift(1)


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # MY CODE BELOW
        Message.__init__(self, text)
        self.message_text = Message.get_message_text(self)
        self.valid_words = Message.get_valid_words(self)
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

        self.shift = shift
        self.text = text

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        # MY CODE BELOW
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        # MY CODE BELOW
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        Returns: self.message_text_encrypted
        '''
        # MY CODE BELOW
        return self.message_text_encrypted



    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # MY CODE BELOW
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        # MY CODE HERE
        Message.__init__(self, text)
        self.text = text
        self.message_text = Message.get_message_text(self)
        self.valid_words = Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # MY CODE BELOW

        testshift = 0
        correctwordsprev = 0
        bestshift = 0

        while testshift < 26:
            decryptedmsg = self.apply_shift(testshift)
            splitdecryptedmsg = decryptedmsg.split(' ')

            # print splitdecryptedmsg
            correctwords = 0

            for word in splitdecryptedmsg:
                if word in self.valid_words:
                    correctwords += 1
            # print testshift, correctwords, bestshift
            if correctwords > correctwordsprev:
                bestshift = testshift
                correctwordsprev = correctwords

            testshift += 1

        solution = self.apply_shift(bestshift)
        return (bestshift, solution)


#  Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()


#  Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()


def decrypt_story():
    ciphered = CiphertextMessage(get_story_string())
    return ciphered.decrypt_message()

print decrypt_story()
#
# testmessage = PlaintextMessage('Hello my name is testing',10)
# print testmessage.text
# testency = testmessage.get_message_text_encrypted()
# print testmessage.get_message_text_encrypted()
# print "Shifted Message:" + testmessage.apply_shift(10)
#
# getanswer = CiphertextMessage(testency)
# print getanswer.decrypt_message()
#
# print 'test'