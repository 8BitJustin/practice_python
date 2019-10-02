"""
Ask the user for a number and determine whether the number is prime or not. (For those who have
forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer
to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
"""


def is_prime(num):

    if num % 1 == num:
        print(True)
    else:
        print(False)

is_prime(12)

"""
num = int(input("Please choose a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
"""