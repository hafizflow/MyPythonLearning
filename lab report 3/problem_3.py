# 3. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
# Take the Celsius temperature as input from the user.

def temp_convert(celsius):
    return (9 / 5 * celsius) + 32


input_celsius = float(input('Enter temperature in Celsius: '))
print(temp_convert(input_celsius))
