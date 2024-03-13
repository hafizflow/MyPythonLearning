# 4. Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is
# a palindrome (reads the same forwards and backward). Use `continue` to skip checking the word if
# its length is less than 3 characters.

while True:
    my_str = input('Enter a word: ')
    if len(my_str) < 3:
        print('Word length should be at least 3 character')
        continue

    # check palindrome
    if my_str == my_str[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')
    break
