# Daniel Rios
#03MAY2026
#LLM_LAB1
#Generating code with specific functions using AI

import random

def main():
    print("Welcome to the Number Guessing Game!")

    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of guesses
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
