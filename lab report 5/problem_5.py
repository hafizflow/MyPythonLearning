# 5. Vowel Counter: Write a Python program that takes a string as input and counts the number of
# vowels (a, e, i, o, u) in it. Use a `for` loop and `continue` to skip counting non-vowel characters.

vowel = 'aeiou'
user_word = input('Enter a word: ')
vowel_count = 0
for char in user_word:
    if char not in vowel:
        continue
    vowel_count += 1
print(f'Total vowel in the word is {vowel_count}')
