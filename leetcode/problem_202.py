# k = 2
#
# s = 0
# cont = 0
# while True:
#     for i in str(k):
#         s += int(i) ** 2
#     if s == 1:
#         print('Happy')
#         break
#     if cont == 10:
#         print('Sad')
#         break
#     else:
#         cont += 1
#         k = s
#         s = 0

# for j in range(4):
#     for i in str(k):
#         s += int(i) ** 2
#     k = s
#     s = 0
#     print(k)


n = 19
seen = set()
while n not in seen:
    total = 0
    seen.add(n)
    for i in str(n):
        total += int(i) ** 2
    if total == 1:
        print('Happy')
        break
    n = total
    print('Sad')
