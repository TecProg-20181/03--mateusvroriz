import random
import string
from sets import Set
WORDLIST_FILENAME = "palavras.txt"

def numberDiff(numberoftrys):
     word = loadWords()

     diffLetters = Set(list(word))
     while len(diffLetters) > numberoftrys:
         word = loadWords()
         diffLetters = Set(list(word))
     if len(diffLetters) < numberoftrys:
        print "Loading word list from file..."
        print "  ", len(word), "words loaded."
        print "  ", len(diffLetters), " different letters."

     return word


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    #wordlist = string.split(line)
    wordlist = ['sderfdpmnjkhtfde','asxdfrg', 'adasdfgfgjukbrv', 'wqcasdasdsfghdfbcaz', 'huadhash']
    word = random.choice(wordlist)
    print "  ", len(wordlist), "words loaded."
    return word


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():
     guessed = ''
     return guessed

def getAvailableLetters():
    import string
    available = string.ascii_lowercase
    return available

def numberguesses():
    remaininguesses = 8
    return remaininguesses

def replaceWords(lettersGuessed):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed;


def hangman(secretWord):
    guesses = numberguesses()
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            wordReplacer = replaceWords(lettersGuessed)

            print 'Oops! You have already guessed that letter: ', wordReplacer
        elif letter in secretWord:
            lettersGuessed.append(letter)

            wordReplacer = replaceWords(lettersGuessed)

            print 'Good Guess: ', wordReplacer
        else:
            guesses -=1
            lettersGuessed.append(letter)


            wordReplacer = replaceWords(lettersGuessed)


            print 'Oops! That letter is not in my word: ',  wordReplacer
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = numberDiff(numberguesses())
hangman(secretWord)
