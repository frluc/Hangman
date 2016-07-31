#Hangman

import random

#defining functions

def getword():
	word = "testword"
	return word


#hardcoded hangman

hangpost = (
"""
         /_\ 
""",
"""
       	  |	
          |
          |
         /_\ 
""",
"""
      ____
         \|
       	  |	
          |
          |
         /_\ 
""",
"""
      ____
      |  \|
      o	  |	
      |   |
          |
         /_\ 
""",
"""
      ____
      |  \|
      o	  |	
     -|-  |
          |
         /_\ 
""",
"""
      ____
      |  \|
      o	  |	
     -|-  |
     /|   |
         /_\ 
""")



	
#variables initialization

maxerrors = 6
guesses = ""
letterscumulated = list()
voidchar = "#"
	
#main

print("-- HANGMAN --")
print("Guess the word letter by letter, don't let that poor dude hang")

errorsleft = maxerrors
wordtoguess = list(getword().upper())
worddisplay = list(wordtoguess)

while errorsleft > 0:
	
	if errorsleft > 1:
		print("You have "+str(errorsleft)+" guesses left")
	elif errorsleft == 1:
		print("You have "+str(errorsleft)+" guess left")
		
	print("Enter a letter:")
	playerinput = input().upper()
	while playerinput in letterscumulated:
		print("You already tried that one, enter another letter:")
		playerinput = input().upper()
		
	letterguess = playerinput
	letterscumulated.append(letterguess)

	if letterguess in wordtoguess:
		print("Good guess!")
	else:
		print("Got it wrong!")
		errorsleft -= 1
		print (hangpost[maxerrors - errorsleft - 1])
		
	for i in range(len(worddisplay)):
		if wordtoguess[i] in letterscumulated:
			worddisplay[i] = wordtoguess[i]
		else:
			worddisplay[i] = voidchar

	print(' '.join(worddisplay))
	
	if worddisplay == wordtoguess:
		break
	
if errorsleft == 0:
	print("You lost!")
else:
	print("You won!")
