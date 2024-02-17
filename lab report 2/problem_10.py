# Problem 8: Write a recursive function that accepts a number as its argument and
# returns the sum of digits, or you can use a loop to solve it.
# Example : 2331
# Output: 9

def addition(num):
    total = 0
    for i in str(num):
        total += int(i)
    print(total)


addition(78)
