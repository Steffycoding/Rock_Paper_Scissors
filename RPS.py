import random
from termcolor import colored

def get_user_move():
    """Get the user's move and validate it."""
    while True:
        user_move = input(colored("Enter your move (rock, paper, or scissors): ", "yellow")).lower()
        if user_move in ["rock", "r", "paper", "p", "scissors", "s"]:
            return user_move
        else:
            print(colored("Invalid move. Please enter rock, paper, or scissors.", "red"))

def get_computer_move():
    """Generate a random move for the computer."""
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def determine_winner(user_move, computer_move):
    """Determine the winner of a round."""
    if user_move == computer_move:
        return colored("It's a tie!", "blue")
    elif (
        (user_move in ["rock", "r"] and computer_move == "scissors") or
        (user_move in ["paper", "p"] and computer_move == "rock") or
        (user_move in ["scissors", "s"] and computer_move == "paper")
    ):
        return colored("You win!", "green")
    else:
        return colored("Computer wins!", "red")

def play_game():
    """Play the Rock, Paper, Scissors game."""
    user_score = 0
    computer_score = 0

    rounds = int(input(colored("Enter the number of rounds: ", "yellow")))

    for _ in range(rounds):
        user_move = get_user_move()
        computer_move = get_computer_move()

        print(f"You chose: {colored(user_move, 'blue')}")
        print(f"Computer chose: {colored(computer_move, 'blue')}")

        result = determine_winner(user_move, computer_move)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    print("\nGame Over!")
    print(f"You: {colored(user_score, 'green')} | Computer: {colored(computer_score, 'red')}")

    if user_score > computer_score:
        print(colored("Congratz! You are the overall winner!", "green"))
    elif user_score < computer_score:
        print(colored("Aye! Computer is the overall winner!", "red"))
    else:
        print(colored("It's a tie overall!", "blue"))

if __name__ == "__main__":
    print(colored("Welcome to Rock, Paper, Scissors!", "light_blue"))
    play_game()
