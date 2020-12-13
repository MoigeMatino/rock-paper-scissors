import random

def play():
    user_input = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer_input = random.choice(['r', 'p', 's'])

    if user_input == computer_input:
        return 'It\'s a tie'
    
    if is_win(user_input,computer_input):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    #returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())