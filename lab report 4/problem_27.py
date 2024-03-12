# 27. Nested Dictionary Update: Given a nested dictionary of employee details, write a Python
# program to update an employee’s salary based on their employee ID.


def update_dic(dic: dict, emp_id: int, salary: float):
    for name, details in dic.items():
        if details['id'] == emp_id:
            details['salary'] = salary
    print(dic)


employees = {
    "Alice Smith": {
        "id": 123,
        "department": "Marketing",
        "salary": 80000
    },
    "Bob Jones": {
        "id": 456,
        "department": "Engineering",
        "salary": 95000
    }
}

update_dic(employees, 456, 600)
