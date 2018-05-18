import random
import string
from sets import Set
import os
from types import *
WORDLIST_FILENAME = "palavras.txt"


def numberDiff(numberoftrys):
    if(fileExtentionTxt() == False):
        exit()
    else:
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

def fileExtentionTxt():
    if WORDLIST_FILENAME.endswith(".txt"):
        return True
    print "Not a txt file"
    return False


def isalphanumeric(letter):
    if(len(letter) == 1):
        if(letter.isalpha()):
            return True
    return False


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
    wordlist = string.split(line)
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


def getAvailableLetters():
    import string
    available = string.ascii_lowercase
    print 'Available letters', available
    return available

def numberOfGuesses():
    remaininguesses = 8
    return remaininguesses

def lettersCurrentWord(lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed;

def availableLetterReplacer(available, lettersGuessed):
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
            return available


def insertLetter(guesses, lettersGuessed, secretWord):
    print "You have" ,guesses, "guesses left"
    getAvailableLetters()
    letter = raw_input('Please guess a letter: ').lower()
    return letter

def isLetterValid(available):
    for letter in available:
        if(letter in string.ascii_lowercase and len(letter) == 1):
            return True
            print "Invalid letter"
            return False


def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:

        available = getAvailableLetters()
        if(isLetterValid(available)):
            availableLetterReplacer(available, lettersGuessed)


        letter = insertLetter(guesses,lettersGuessed, secretWord )
        if letter in lettersGuessed:

            wordReplacer = lettersCurrentWord(lettersGuessed)

            print 'Oops! You have already guessed that letter: ', wordReplacer
        elif letter in secretWord:
            lettersGuessed.append(letter)

            wordReplacer = lettersCurrentWord(lettersGuessed)

            print 'Good Guess: ', wordReplacer
        else:
            guesses -=1
            lettersGuessed.append(letter)


            wordReplacer = lettersCurrentWord(lettersGuessed)


            print 'Oops! That letter is not in my word: ',  wordReplacer
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = numberDiff(numberOfGuesses())
hangman(secretWord)
