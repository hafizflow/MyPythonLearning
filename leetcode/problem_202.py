k = 2

s = 0
cont = 0
while True:
    for i in str(k):
        s += int(i) ** 2
    if s == 1:
        print('Happy')
        break
    if cont == 10:
        print('Sad')
        break
    else:
        cont += 1
        k = s
        s = 0

# for j in range(4):
#     for i in str(k):
#         s += int(i) ** 2
#     k = s
#     s = 0
#     print(k)
