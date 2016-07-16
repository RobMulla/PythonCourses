from ps4a import *
from ps4b import *


wordList = loadWords()
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)

print ""
print "========="
print ""
playGame(wordList)
