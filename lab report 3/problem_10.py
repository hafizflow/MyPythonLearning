# 10. Sum of Even Numbers: Write a Python program using a while loop to calculate the
# sum of all even numbers between 1 and N, where N is taken as input from the user.

def sum_even(num):
    add = 0
    for i in range(num):
        if i % 2 == 0:
            add = add + i
    return add


number = int(input('Enter N: '))
print(sum_even(number))

