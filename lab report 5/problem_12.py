# 12.Design a Python function that compresses a given string by replacing repeated
# characters with the number of repetitions followed by the character itself. It takes input
# from users of how many string users want to input, maximum length of string and show
# output of compressed string.

def compress_string(string):
    compressed = ""
    count = 1
    for i in range(len(string)):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            compressed += str(count) + string[i]
            count = 1
        else:
            count += 1
    return compressed


num_strings = int(input("Enter the number of strings you want to input: "))
max_length = int(input("Enter the maximum length of each string: "))

for _ in range(num_strings):
    input_string = input(f"Enter a string (max length {max_length}): ")
    if len(input_string) > max_length:
        print("String length exceeds the maximum limit. Skipping this string.")
        continue
    compressed_string = compress_string(input_string)
    print(f"Original string: {input_string}")
    print(f"Compressed string: {compressed_string}")
    print()
