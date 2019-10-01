"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start a
new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import sys

user1 = input("What's your name? ")
user2 = input("And your name? ")
user1_answer = input("%s, do yo want to choose rock, paper or scissors? " % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors? " % user2)


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return"Invalid input! You have not entered rock, paper or scissors, try again."
        sys.exit()

print(compare(user1_answer, user2_answer))


# My code

# import random
#
# chances = int(input("How many chances would you like? "))
#
# while True:
#     count = 0
#
#     cpu_list = ["Rock", "Paper", "Scissors"]
#     choice = input("Rock, Paper, or Scissors? ")
#     random_cpu = random.choice(cpu_list)
#     if choice == "Rock":
#         if random_cpu == "Rock":
#             print("Tie")
#             count = count + 1
#             print(count)
#             continue
#         elif random_cpu == "Paper":
#             print('Winner!')
#             count = count + 1
#             print(count)
#
#     if count == chances:
#         again = input("Try again? (y or n) ")
#         if again == "y":
#             continue
#         elif again == "n":
#             print("Thank you for playing!")
#             break
#     break