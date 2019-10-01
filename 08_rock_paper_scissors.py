"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start a
new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import random

game = True

while game:
    count = 0
    chances = int(input("How many chances would you like? "))
    cpu_list = ["Rock", "Paper", "Scissors"]
    choice = input("Rock, Paper, or Scissors? ")
    random_cpu = random.choice(cpu_list)
    if choice == "Rock" and random_cpu == "Rock":

    if count == chances:
        again = input("Try again? (y or n) ")
        if again == "y":
            continue
        elif again == "n":
            print("Thank you for playing!")
            break
    break
