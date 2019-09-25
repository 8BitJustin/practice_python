"""
Ask the user for a number. Depending on whether the number is even or odd, print out an
appropriate message to the user. Hint: how does an even / odd number react differently when
divided by 2?
"""

num = int(input("Input a number: "))

# Lines 10, 11, extra credit
if num % 4 == 0:
    print("By four")
elif num % 2 == 0:
    print("Even")
elif num % 1 == 0:
    print("Odd")