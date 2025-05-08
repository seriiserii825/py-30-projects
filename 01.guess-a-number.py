#!/usr/bin/env python3

import random

random_num: int = random.randint(1, 10)

lower_num, higher_num = 1, 10

print(f"Guess a number between {lower_num} and {higher_num}.")

while True:
    try:
        user_quess: int = int(input("Enter your guess: "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue

    if user_quess > random_num:
        print("Too high! Try again.")
    elif user_quess < random_num:
        print("Too low! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break
