
# The Perfect Guess Game...

import random

num = random.randint(0,100)

print("\n\n\nLet's Play the game of Perfect guess...\nYou have to guess a number between 0 and 100.")

x = None
guesses = 0

while x != num:
    x = int(input("\nYour Guess : \n"))
    guesses += 1
    if x < (num-20) :
        print("Think Higher...")
    elif (num-20) < x < num :
        print("Just a little higher...")
    elif x > (num+20) :
        print("The Number is not that big...")
    elif (num+20) > x > num :
        print("Just a little more smaller...")
else:
    print("Your guess is Absolutely correct...\n The number is,", num)
    print(f"Your total number of guesses are {guesses}")
