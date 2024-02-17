# Problem 3: Write a function that inputs a number and prints the multiplication table of that number

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{i} * {num} = {i * num}")


multiplication_table(4)
