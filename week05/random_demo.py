import random

RANGE_FROM = 0
RANGE_TO = 10
MAX_ATTEMPTS = 3


def guessing_game(
    range_from: int = RANGE_FROM,
    range_to: int = RANGE_TO,
    max_attempts: int = MAX_ATTEMPTS,
):

    correct_guess = False
    attempt = 0

    number_to_guess = random.randint(range_from, range_to)

    while not correct_guess and attempt < max_attempts:
        n = input("\nGuess which number I am thinking of: ")
        n = int(n)
        attempt = attempt + 1
        correct_guess = n == number_to_guess
        if not correct_guess:
            print("Nope!")

    if correct_guess:
        print(f"\nCongratulations. {n} is indeed the number I was thinking off.")
    else:
        print(f"\nBummer, it was {number_to_guess}. Better luck next time, LOOSER!")

def main():
    guessing_game()

main()