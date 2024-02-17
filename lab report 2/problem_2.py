def calculate_ascii_sum(name):
    return sum(ord(char) for char in name)


employee_names = ["John Doe", "Jane Smith", "Bob Johnson"]

ascii_sums = [calculate_ascii_sum(name) for name in employee_names]

ascii_list = []

for i in ascii_sums:
    ascii_list.append(i)

print(ascii_list)
