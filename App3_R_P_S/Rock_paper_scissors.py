import random
computer_choice =  random.choice(['rock', 'paper', 'scissors'])
playername = input('What is your name: \n')
user_choice = input('\nDo you want rock, paper, or scissors? \n')
print('\nBingoChose:', computer_choice)

if computer_choice == user_choice:
    print('\nIts a TIE, play again\n')
#there are 3 ways when user can win in this game lets define that.

elif user_choice == 'rock' and computer_choice =='scissors':
    print('Playername:', playername, 'is winner, Bingo loose\n')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Playername:', playername, 'is winner, Bingo loose\n')
elif user_choice == 'scissors' and computer_choice == 'paper':
        print('Playername:', playername, 'is winner, Bingo loose\n')
else:
    print('Playername:', playername, ' you loose, Bingo wins' )
