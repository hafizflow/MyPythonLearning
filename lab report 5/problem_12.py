# 12.Design a Python function that compresses a given string by replacing repeated
# characters with the number of repetitions followed by the character itself. It takes input
# from users of how many string users want to input, maximum length of string and show
# output of compressed string.


def compress_string(s):
    compressed_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += str(count) + s[i - 1] if count > 1 else s[i - 1]
            count = 1

    compressed_string += str(count) + s[-1] if count > 1 else s[-1]
    return compressed_string


def main():
    num_strings = int(input("Enter the number of strings you want to input: "))

    for _ in range(num_strings):
        max_length = int(input("Enter the maximum length of the string: "))
        user_input = input(f"Enter a string (max length {max_length}): ")

        if len(user_input) > max_length:
            print("Input string exceeds the maximum length. Skipping.")
            continue

        compressed_result = compress_string(user_input)
        print(f"Compressed String: {compressed_result}")


if __name__ == "__main__":
    main()
