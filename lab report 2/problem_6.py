# Problem 4: Write a program to reverse an integer number using for loop or while loop.
# Example: 1435
# Result: 5341

def reverse_num(num):
    str_num = str(num)
    reverse = ''
    for i in range(len(str_num) - 1, -1, -1):
        reverse += str_num[i]
    print(reverse)


reverse_num(1435)
