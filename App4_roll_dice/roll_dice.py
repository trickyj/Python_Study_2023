import random

roll = random.randint(1,6)

#the input has to be integer because we want to comapre it to the roll.

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("\nCollect! They rolled a " + str (roll))
else:
    print("\nYou are wrong. It was " + str(roll))
    "\n"