import random

userHand = input("Rock, Paper, Scissors:")

computerHand = random.random()

if computerHand <= .33:
	computerHand = "rock"

elif computerHand <= .66:
	computerHand = "paper"

else:
	computerHand = "scissors"

def game(first, second):
	if first == second:
	 print ("You chose", first)
	 print ("Computer chose", second)
	 print ("It is a tie")
	elif first == "rock":
		if second == "scissors":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win!")
		else:
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You lose")
	elif first == "paper":
		if second == "rock":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win!")
		else:
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You lose")
	elif first == "scissors":
		if second == "paper":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win!")
		else:
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You lose")

game(userHand, computerHand)