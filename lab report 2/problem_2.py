def calculate_ascii_sum(name):
    return sum(ord(char) for char in name)


employee_names = ["John Doe", "Jane Smith", "Bob Johnson"]

ascii_sums = [calculate_ascii_sum(name) for name in employee_names]

for name, ascii_sum in zip(employee_names, ascii_sums):
    print(f"{name}: ASCII Sum = {ascii_sum}")
