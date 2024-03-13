# 11.A university management is going to make a system to generate a unique student e-mail id of
# newly admitted students. Suppose you are the programmer is said to be generated to make e-mail
# by taking a list of student’s name. You have to generate e-mail by adding the length of name and
# also add the ASCII value of first character after the lower case name. If the name exceed 20
# character it ignores that name and proceed to the next activity.
# Input: The first line contain the single integers N - Numbers of students in the list. The second
# line contains N Strings of names N1,N2,N3,…….N(i).(String must not exceed 20 character.
# Output: Print the email list according to the scenario. (Lower case name_lenth of name_ascii
# value of first character)

name_list = ['Haifz', 'Nishat', 'Anjum']


def email_maker(name):
    if len(name) > 20:
        return None

    student_email = ''
    student_email += name.lower()
    student_email += str(len(name))
    student_email += str(ord(name.lower()[0]))
    return student_email


email_list = [email_maker(name) for name in name_list]
print(email_list)
