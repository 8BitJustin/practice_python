"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
list of only the first and last elements of the given list. For practice, write this code inside a
function.
"""
import random

# makes random list
random_list = [random.randint(0,50) for i in range(5)]

random_list.sort()


def list_ends(list):
    beta = [list.pop(0), list.pop(-1)]

    print(beta)


# this prints what the random list is
print(random_list)

# this calls the function to pull the first and last items from the list
list_ends(random_list)

# this uses the function using a list instead of a variable as the argument
list_ends([2, 4, 5, 6, 98])
