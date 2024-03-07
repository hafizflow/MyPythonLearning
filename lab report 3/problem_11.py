# 11. Print Patterns: Write a Python program using nested for loops to print various
# patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.

def patterns(num):
    # right-angled
    for i in range(num+1):
        for j in range(i):
            print('*', end=' ')
        print('')

    # Inverted right-angled
    for i in range(num, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print('')


patterns(5)
