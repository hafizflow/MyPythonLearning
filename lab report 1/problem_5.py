# Write a python program which contains a list of some names of items.
# case-01:Find out the length of each item  and store in an another list.
# case-02:Access each item’s  name and convert the lower case letters into
# uppercase as well as convert the uppercase letters into lowercase letters.

names = ['hafiZ', 'Rafi', 'nishat', 'ZAHID', 'SaNi', 'Zk']

# list comprehension method
new_list = [len(i) for i in names]

for i in range(len(names)):
    modified_word = ''
    for j in names[i]:
        if j.islower() and j.isascii():
            modified_word += j.upper()
        elif j.isupper() and j.isascii():
            modified_word += j.lower()
        else:
            modified_word += j
    names[i] = modified_word

print(new_list)
print(names)
