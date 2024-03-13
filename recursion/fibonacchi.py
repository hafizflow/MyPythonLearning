def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
x = list(map(fibonacci, [0, 1, 2, 3, 4, 5, 6]))
print(x)
