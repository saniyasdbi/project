# Number Guessing Project
import random

print("Guess the number between 1 and 10")

secret_number = random.randint(1, 10)

guess = input("Enter your guess: ")
guess = int(guess)

if guess == secret_number:
    print("You guessed it right!")
else:
    print("Wrong guess! The number was", secret_number)
