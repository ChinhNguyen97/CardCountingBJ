#!/usr/bin/python3

#TO-DO: refractor using Classes

#For first draft use golbal
RUNNINGCOUNT = 0
CARDINDECK = 52
TOTALCARDS = 0

DECKINFO = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "1": 0}

#Count methods
def getCount():
	return RUNNINGCOUNT

def addToCount(num):
	global RUNNINGCOUNT
	RUNNINGCOUNT = RUNNINGCOUNT + num

#Total methods
def setTotal(decks):
	global CARDINDECK
	global TOTALCARDS
	TOTALCARDS = CARDINDECK * decks

def subTotal(num):
	global TOTALCARDS
	TOTALCARDS -= 1

def getTotal():
	global TOTALCARDS
	return TOTALCARDS

def getTrueCount():
	global TOTALCARDS
	global RUNNINGCOUNT

	return format(RUNNINGCOUNT / (TOTALCARDS / 52), '.3f')

#Deck methods
def setupDeck(decks):
	global DECKINFO
	for number in DECKINFO:
		if number == "10":
			DECKINFO[number] = 4*4*decks
		else:
			DECKINFO[number] = 4*decks

def printDeck():
	global DECKINFO
	for number in DECKINFO:
		print(number + " - " + str(DECKINFO[number]) + ", ", end = '')
	print("\n")

def removeFromDeck(num):
	global DECKINFO
	try:
		DECKINFO[str(num)] -= 1
	except:
		print("J Q K is also 10")

#Main drive methods
def help():
	print("Options: \nq - quit \nc - running count \nt - total number of cards left \nx - true count")


def intro():
	print("****Welcome to Gamble Me****")
	help()
	deck_num = input("Enter number of starting decks: ")
	setTotal(int(deck_num))
	setupDeck(int(deck_num))

	return 0

def outro():
	print("****See you later****")

	return 0

def checkValue(number,lower = 1,upper = 13):
	if (isinstance(number, int)):
		if number in range(lower, upper+1):
			return True
	
	return False


def assignValue(number):
	value = None
	if (isinstance(number, int)):
		if number in range(2,7):
			value = 1
		elif number in range(7,10):
			value = 0
		elif number == 1 or ( number >= 10 and number <= 13 ):
			value = -1

	if value is not None:
		return value
	else:
		return 99

def deal():
	user_input = ""
	while(user_input.lower() != "q"):
		try:
			user_input = input("Deal: ")
			if user_input.lower() == "c":
				print("Running count: " + str(getCount()))
			elif user_input.lower() == "t":
				print("Total cards left: " + str(getTotal()))
			elif user_input.lower() == "x":
				print("True count: " + str(getTrueCount()))
			elif user_input.lower() == "e":
				printDeck()
			elif user_input.lower() == "q":
				pass
			else:
				try:
					number = int(user_input)
					if (checkValue(number)):
						removeFromDeck(number)
						val = assignValue(number)
						addToCount(val)
						subTotal(1)
				except ValueError:
					print("Please enter Q/C or a number")
		except KeyboardInterrupt:
			break
	return 0

def main():
	intro()
	deal()
	outro()

main()

