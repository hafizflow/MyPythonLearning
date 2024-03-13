# 7.Develop a student information system. Students submit their information & the data has been
#
# stored. Print the data they are submitting in this information system.
# Case 1: Allow students to choose which information they want to submit.
# Case 2: If age is chosen, it should be submitted as a float number.
# Case 3: Limit all other information to a maximum of 5 characters.

student_info = {
    'Name': '',
    'Batch': '',
    'ID': '',
    'Grade': '',
    'Age': 0.0,
}

while True:
    print('\nStudent Information System')
    print('1. Submit Name')
    print('2. Submit Batch')
    print('3. Submit ID')
    print('4. Submit Grade')
    print('5. Submit Age')
    print('6 Print Submitted Information')
    print('7. Exit Student Information System')

    choice = int(input('Enter your choice (1-7): '))

    if choice == 1:
        student_info['Name'] = input('Enter your Name: ')[:20]
    elif choice == 2:
        student_info['Batch'] = input('Enter your Batch: ')[:5]
    elif choice == 3:
        student_info['ID'] = input('Enter your ID: ')[:12]
    elif choice == 4:
        student_info['Grade'] = input('Enter your Grade: ')[:5]
    elif choice == 5:
        try:
            student_info['Age'] = float(input('Enter your Age: ')[:5])
        except ValueError:
            print('Invalid input, Please enter valid age')

    elif choice == 6:
        for key, value in student_info.items():
            print(f'{key} : {value}')
    elif choice == 7:
        print('Thank you')
        break
    else:
        print('Enter valid (1-7) choice')
