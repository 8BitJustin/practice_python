import datetime
now = datetime.datetime.now()

name = input("What is your name? ")
age = int(input("How old are you? "))

year = (now.year - age) + 100

print(name + " you should turn 100 by the year " + str(year) + ".")