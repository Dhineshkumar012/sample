import random

# Define possible choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    while True:
        # Get player's choice
        player_choice = input("\nEnter rock, paper, or scissors: ").strip().lower()

        # Check if the input is valid
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()

        # Display choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! 🎮")
            break

if __name__ == "__main__":
    play_game()
