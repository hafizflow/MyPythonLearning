# 15. Dictionary Manipulation: Given a dictionary with student names as keys and
# their corresponding scores as values, write a Python program to add a new student
# to the dictionary and update the score of an existing student.


def manipulate_dic(dic):
    new_name = 'Hafiz'
    new_score = 81
    dic[new_name] = new_score

    update_name = 'Rafi'
    update_score = 91
    dic[update_name] = update_score

    return dic


dictionary = {"Nishat": 100, 'Rafi': 89}
print(manipulate_dic(dictionary))
