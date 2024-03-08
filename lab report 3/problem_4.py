# 4. String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def is_palindrome(word: str):
    # using string slicing technique to reverse the string
    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')


is_palindrome('lol')
