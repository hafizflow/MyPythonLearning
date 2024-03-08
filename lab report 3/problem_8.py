# 8. Count Digits in a Number: Write a Python program using a
# while loop to count the number of digits in a given integer N.

def count_digit(num):
    count = 0
    while num > 0:
        count += 1
        # removing last digit
        num = num // 10

    return count


print(f'Total digit in the number: {count_digit(56789)}')
