import random

def play():
    user = input("What's your Choice? 'r' for rock , 'p' for papers, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'

def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())