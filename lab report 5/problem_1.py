# 1. Password Validator: Write a Python program that takes a password as input and checks
# if it meets the following criteria: at least 8 characters long, contains both uppercase
# and lowercase letters, and has at least one digit. If the password is valid, print
# “Password accepted.” If not, use `continue` to prompt the user to enter a valid password.


while True:
    password = input('Enter your password: ')

    # check length
    if len(password) < 8:
        print('Password is too short. Must be at least 8 character')
        continue

    # check upper and lower
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        print('Password must contain both uppercase and lowercase letters.')
        continue

    # check digit
    if not any(char.isdigit() for char in password):
        print('Password must have at least one digit')
        continue

    # If all criteria are met, accept the password
    print("Password accepted.")
    break
