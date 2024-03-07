# 9. Fibonacci Sequence: Write a Python program using a for loop to generate
# the Fibonacci sequence up to a given limit N.

def generate_fib(num):
    fibonacci_series = [0, 1]
    for i in range(2, num):
        next_num = fibonacci_series[-1] + fibonacci_series[-2]
        if next_num <= num:
            fibonacci_series.append(next_num)
        else:
            break
    return fibonacci_series


print(generate_fib(13))
