import random

user = 0
computer = 0

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    while user not in ('r', 's', 'p'):
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r'):
        return True

while(True):
    did_win = play()
    if did_win == "You won!":
        print(did_win)
        user += 1
    elif did_win == "You lost!":
        print(did_win)
        computer += 1
    else:
        print(did_win)
    print(f"user: {user} \t\t computer: {computer}")
        
    
