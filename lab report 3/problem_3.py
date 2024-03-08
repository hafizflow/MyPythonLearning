# 3. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
# Take the Celsius temperature as input from the user.

def temp_convert(celsius):
    fahrenheit = (9 / 5 * celsius) + 32
    print(f'Converted temperature in Fahrenheit {fahrenheit} °C')


input_celsius = float(input('Enter temperature in Celsius: '))
temp_convert(input_celsius)
