import random
#Defining the function. Since we want to use this again and again. 
def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1, 6)
    return dice_total
def main():

    player1 = input("Enter player 1's name:\n")
    player2 = input("Enter player 2's name:\n")
    #defining another function. So roll_dice will get called and return a dice value. And we store it in new variables for each player.
    roll1 = roll_dice()
    roll2 = roll_dice()
    #players should know what they rolled. So lets print them.
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)
    if roll1 > roll2:
        print(player1, 'wins')
    elif roll2 > roll1:
        print(player2, 'wins')
    else:
        print('you tie!')
main()
