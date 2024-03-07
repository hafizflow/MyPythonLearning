# 6. Grades Classification: Write a Python program that takes a student’s percentage
# as input and prints their corresponding grade according to the following criteria:
# – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail.

def calculate_result(num):
    if num >= 90:
        print('A+')
    elif 80 <= num <= 89:
        print('A')
    elif 70 <= num <= 79:
        print('B')
    elif 60 <= num <= 69:
        print('C')
    else:
        print('Fail')


calculate_result(50)
