
import random

correct_guess = False
attempt = 0

number_to_guess = random.randint(0,10)

while not correct_guess and attempt < 3:
    n = input("\nGuess which number I am thinking of: ")
    n = int(n)
    attempt = attempt + 1
    correct_guess = (n == number_to_guess)
    if not correct_guess:
        print("Nope!")

if correct_guess:
    print(f"\nCongratulations. {n} is indeed the number I was thinking off.")
else:
    print(f"\nBummer, it was {number_to_guess}. Better luck next time, LOOSER!")