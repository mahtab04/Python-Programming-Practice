# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right. (Hint: remember to
# use the user input lessons from the very first exercise)

import random

guess = random.randint(1, 20)

print("Enter a number between 1-20: ")

number = int(input())
while guess != number:
    if guess < number:
        print("Your guess is too high, Try again!")
    elif guess > number:
        print("Your guess is too low, Try again!")

    number = int(input("Enter a number again: "))

print("You got it!")
