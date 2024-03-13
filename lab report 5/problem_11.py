# 11.A university management is going to make a system to generate a unique student e-mail id of
# newly admitted students. Suppose you are the programmer is said to be generate to make e-mail
# by taking a list of student’s name. You have to generate e-mail by adding the length of name and
# also add the ASCII value of first character after the lower case name. If the name exceed 20
# character it ignores that name and proceed to the next activity.
# Input: The first line contain the single integers N - Numbers of students in the list. The second
# line contains N Strings of names N1,N2,N3,…….N(i).(String must not exceed 20 character.
# Output: Print the email list according to the scenario. (Lower case name_lenth of name_ascii
# value of first character)


def generate_email(name):
    if len(name) <= 20:
        lowercase_name = name.lower()
        email_id = f"{lowercase_name}_{len(lowercase_name)}_{ord(lowercase_name[0])}"
        return email_id
    else:
        return None


# Input the number of students
n = int(input("Enter the number of students: "))

# Input the list of student names
students = [input(f"Enter name for student {i + 1}: ") for i in range(n)]

# Generate and print email IDs for each student
print("\nGenerated Email IDs:")
for student in students:
    email_id = generate_email(student)
    if email_id:
        print(email_id)
    else:
        print(f"Ignoring {student} as the name exceeds 20 characters.")
