# 12. Prime Number Checker: Write a Python program using a while loop to check if a given
# number N is prime or not.

def prime_checker(num):
    is_prime = True
    divisor = 2

    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

    if is_prime and num > 1:
        print('Prime Number')
    else:
        print('Not prime number')


user_input = int(input('Enter a number to check: '))
prime_checker(user_input)
