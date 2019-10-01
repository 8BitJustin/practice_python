"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the
user input lessons from the very first exercise)
"""

import random

random_num = random.randint(1, 9)
count = 1

while True:
    guess = int(input("Guess a number: "))

    if guess == random_num:
        print("The number was " + str(random_num) + ", you guessed " + str(guess) + " and won!")
        print("This took you " + str(count) + " tries!")
        break
    elif guess < random_num:
        count = count + 1
        print("Higher!")
        continue
    elif guess > random_num:
        count = count + 1
        print("Lower!")
        continue
