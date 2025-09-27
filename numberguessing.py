import random
def play():
    number = random.randint(1,10)
    guess = input("guess a number between 1 and 10:  ")
    guess = int(guess)
    if guess == number:
	    print("you guessed it right!")
    else:
	     print("you guessed it wrong!")
	
play()	
play()
play()
play()
play()