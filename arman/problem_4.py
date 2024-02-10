def count_strings_with_same_ends(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


sample_list = ['abc', 'xyz', 'aba', '1221', 'zaz']
result = count_strings_with_same_ends(sample_list)
print("Number of strings with the same first and last characters:", result)
