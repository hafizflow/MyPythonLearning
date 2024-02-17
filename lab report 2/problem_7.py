# Problem 5: Write a python function that takes a string and checks if it’s a palindrome or not.
# Example: “madam” “cat”
# Result: “Palindrome, not palindrome

def is_palindrome(random_str):
    if random_str == random_str[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"


print(is_palindrome("madam"))
