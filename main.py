#!/usr/bin/python3

RUNNINGCOUNT = 0

def getCount():
	return RUNNINGCOUNT

def addToCount(num):
	global RUNNINGCOUNT
	RUNNINGCOUNT = RUNNINGCOUNT + num

def intro():
	print("****Welcome to Gamble Me****")
	deck_num = input("Enter number of starting decks: ")

	return deck_num

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
		elif number == 1 or number >= 10:
			value = -1

	if value is not None:
		return value
	else:
		return 99

def deal():
	user_input = ""
	while(user_input.lower() != "q"):
		try:
			user_input = input()
			if user_input.lower() == "c":
				print(getCount())
			else:
				try:
					number = int(user_input)
					if (checkValue(number)):
						val = assignValue(number)
						addToCount(val)
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

