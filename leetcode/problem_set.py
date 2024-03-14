import math

n = 80
x = math.log(n, 3)
# print(x)
r = int(3 ** x)
# print(r)
if r == n:
    print("true")
else:
    print("false")
