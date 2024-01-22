import random

def get_user_move():
    """Get the user's move and validate it."""
    while True:
        user_move = input("Enter your move (rock, paper, or scissors): ").lower()
        if user_move in ["rock", "paper", "scissors"]:
            return user_move
        else:
            print("Invalid move. Please enter rock, paper, or scissors.")

def get_computer_move():
    """Generate a random move for the computer."""
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def determine_winner(user_move, computer_move):
    """Determine the winner of a round."""
    if user_move == computer_move:
        return "It's a tie!"
    elif (
        (user_move == "rock" and computer_move == "scissors") or
        (user_move == "paper" and computer_move == "rock") or
        (user_move == "scissors" and computer_move == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    user_score = 0
    computer_score = 0

    rounds = int(input("Enter the number of rounds: "))

    for _ in range(rounds):
        user_move = get_user_move()
        computer_move = get_computer_move()

        print(f"You chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        result = determine_winner(user_move, computer_move)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    print("\nGame Over!")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer is the overall winner!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
