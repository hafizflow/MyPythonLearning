names = ['AsiF', 'aZiM', 'Nishat', 'bithI', 'TANAz']

# list comprehension method
length_list = []

for i in range(len(names)):
    length_list.append(len(names[i]))

    changed_word = ''

    for j in names[i]:
        if j.islower() and j.isascii():
            changed_word += j.upper()
        elif j.isupper() and j.isascii():
            changed_word += j.lower()
        else:
            changed_word += j
    names[i] = changed_word

print(length_list)
print(names)
