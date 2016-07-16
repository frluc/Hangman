#Hangman

import random

#defining functions

def getword():
	word = "testword"
	return word
	
#variables initialization

maxtries = 6
guesses = ''
	
#main

print("-- HANGMAN --")
print("Guess the word letter by letter, don't let that poor dude hang")

tries = maxtries
wordtoguess = list(getword().upper())

print("Enter a letter")
letterguess = input().upper()

worddisplay = wordtoguess

for i in range(len(worddisplay)):
	if worddisplay[i] == letterguess:
		print("true")
		worddisplay[i] = letterguess
	else:
		print("false")
		worddisplay[i] = "#"

print(' '.join(worddisplay))
