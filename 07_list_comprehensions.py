"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write
one line of Python that takes this list a and makes a new list that has only the even elements of
this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# using list comprehension. within the new list, the first item is the expression, which ties
# into the for loop, and then finally the if statement. If true, only even numbers are placed
# within the new b list
b = [num for num in a if num % 2 == 0]

print(b)
