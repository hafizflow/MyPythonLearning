# 3. Positive Number Sum: Write a Python program that takes positive numbers as input until a
# negative number is entered. Then, calculate and print the sum of all positive numbers entered. Use a
# `while` loop and `break` to exit the loop when a negative number is encountered.

total_sum = 0

while True:
    num = float(input("Enter positive number ( or negative number to terminate ):  "))
    if num < 0:
        break
    total_sum += num
print(total_sum)
