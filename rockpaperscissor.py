import random

# Rock, Paper, Scissors game
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f'Computer chose: {computer}')

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # Return True if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False  # Explicitly return False

# Run the game
print(play())
