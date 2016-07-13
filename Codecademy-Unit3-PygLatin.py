pyg = 'ay'
# User inputs oringal word to be translated
original = raw_input('Enter a word:')

# Check to see if word is good
if len(original) > 0 and original.isalpha():
    word = original.lower() #Make lowercase
    first = word[0] #Take first letter of word
    new_word = word + first + pyg #create new word with first letter
    new_word = new_word[1:len(new_word)] #remove first letter
    print new_word
else:
    print 'empty or not a word'
