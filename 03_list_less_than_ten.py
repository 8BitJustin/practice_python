"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

# lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for i in lst:
#     if i < 6:
#         print(i)

# Extra
lst2 = [1, 4, 7, 12, 15, 19, 22, 27, 33, 45, 65]

input_n = int(input("Input number: "))

for i in lst2:
    if i < input_n:
        print(i)
