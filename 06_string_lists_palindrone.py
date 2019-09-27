"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome
is a string that reads the same forwards and backwards.)
"""

inpt = input("Type a word: ")

inpt_rev = inpt[::-1]

if inpt == inpt_rev:
    print(True)
else:
    print(False)

