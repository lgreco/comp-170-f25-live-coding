import random

RANGE_FROM = 0
RANGE_TO = 10
MAX_ATTEMPTS = 3


def guessing_game(
    range_from: int = RANGE_FROM,
    range_to: int = RANGE_TO,
    max_attempts: int = MAX_ATTEMPTS,
):
    """A simple number guessing game."""
    # Initialize the game state
    correct_guess = False
    attempt = 0
    number_to_guess = random.randint(range_from, range_to)
    # Start the game by informing the user of the rules
    print("\033[2J\033[H", end="")  # Clear the screen using ANSI escape codes
    print(f"I'm thinking of a number between {range_from} and {range_to}.")
    print(f"You have {max_attempts} attempts to guess it.")
    # Loop until the user guesses correctly or runs out of attempts
    while not correct_guess and attempt < max_attempts:
        n = input("\nGuess which number I am thinking of: ")
        # Clean the input
        n = int(n)
        # Update the game state
        attempt = attempt + 1 # attempt += 1
        correct_guess = n == number_to_guess
        if not correct_guess:
            print("Nope!")
    # Game over, print the result
    if correct_guess:
        print(f"\nCongratulations. {n} is indeed the number I was thinking off.")
    else:
        print(f"\nBummer, it was {number_to_guess}. Better luck next time, LOOSER!")

def main():
    guessing_game()

main()