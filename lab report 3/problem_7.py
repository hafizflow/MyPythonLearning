# 7.Table of a Number: Write a Python program using a for loop to print
# the multiplication table of a given number N.

def multiplication_table(num):
    for i in range(1, 11):
        res = num * i
        print(f'{num} * {i} = {res}')


multiplication_table(5)
