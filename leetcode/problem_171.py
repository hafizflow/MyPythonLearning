char = 'ZY'
res = 0
length = len(char) - 1

for i in char:
    res += (ord(i) - 64) * (26 ** length)
    length -= 1
print(res)
