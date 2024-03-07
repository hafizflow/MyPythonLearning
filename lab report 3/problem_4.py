# 4. String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def isPalindrome(word: str):
    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')


isPalindrome('lol')
