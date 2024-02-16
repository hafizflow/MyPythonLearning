# Problem -01: Suppose, you are working as a python programmer in a Software company.
# You are asked to create a python program which will take a String as an Input and
# rotate some of its characters to make a secure password.Now,
# You should take input string of ‘m’ size without a whitespace.
# Take ‘n’ as the numbers of characters to rotate the string.
# Where n<=m

# Sample Input:
# Size of String m= 9
# Input String:ummeAyman
# Number of characters to rotate:05

def rotate_string(intput_str, n):
    if n <= 0 or n > len(intput_str):
        print('Invalid rotation value')
        return

    rotate_str = intput_str[n:] + intput_str[:n]
    print(f"Rotated String: {rotate_str}")


n = int(input('Enter how many times to rotate: '))
str_input = input('Enter which string to rotate: ')
rotate_string(str_input, n)
