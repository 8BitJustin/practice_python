"""
Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.
"""

import datetime
now = datetime.datetime.now()

name = input("What is your name? ")
age = int(input("How old are you? "))

year = (now.year - age) + 100

print(name + " you should turn 100 by the year " + str(year) + ".")