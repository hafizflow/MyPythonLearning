def sum_of_digit(n):
    if n <= 9:
        return n
    else:
        return (n % 10) + sum_of_digit(n // 10)


print(sum_of_digit(56))
