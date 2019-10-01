"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the
user input lessons from the very first exercise)
"""

import random

chances = int(input("How many chances would you like? "))

while True:
    count = 0

    cpu_list = ["Rock", "Paper", "Scissors"]
    choice = input("Rock, Paper, or Scissors? ")
    random_cpu = random.choice(cpu_list)
    if choice == "Rock":
        if random_cpu == "Rock":
            print("Tie")
            count = count + 1
            print(count)
            continue
        elif random_cpu == "Paper":
            print('Winner!')
            count = count + 1
            print(count)

    if count == chances:
        again = input("Try again? (y or n) ")
        if again == "y":
            continue
        elif again == "n":
            print("Thank you for playing!")
            break
    break