# Write a python program which contains a list of some names of items.
# case-01:Find out the length of each item  and store in an another list.
# case-02:Access each item’s  name and convert the lower case letters into
# uppercase as well as convert the uppercase letters into lowercase letters.

names = ['hafiz', 'Rafi', 'nishat', 'ZAHID', 'SaNi', 'zk']
new_list = []

for i in range(len(names)):
    new_list.append(len(names[i]))

    upperLetter = ''
    lowerLetter = ''

    for j in names[i]:
        if j.islower() and j.isascii():
            upperLetter += j.upper()
        elif j.isupper() and j.isascii():
            lowerLetter += j.lower()
    names[i] = upperLetter + lowerLetter

print(new_list)
print(names)
