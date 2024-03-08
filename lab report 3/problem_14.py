# 14. Reverse String: Write a Python program using a while loop to reverse a given string.

def reverse_string(word: str):
    index = len(word) - 1
    reverse_word = ''
    while 0 <= index:
        reverse_word += word[index]
        index = index - 1
    print(reverse_word)


reverse_string('Hello')
