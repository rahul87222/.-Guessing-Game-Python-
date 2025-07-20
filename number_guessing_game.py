
import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() == "yes":
            number = random.randint(1, 100)
            attempts = 0
        else:
            print("Thanks for playing!")
            break
