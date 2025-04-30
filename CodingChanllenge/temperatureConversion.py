'''
Functional code block: Temperature conversion tool
Your task:
Write three Python functions that implement a simple temperature conversion tool.

celsius_to_fahrenheit(celsius): Takes a temperature in Celsius and converts it to Fahrenheit.

fahrenheit_to_celsius(fahrenheit): Takes a temperature in Fahrenheit and converts it to Celsius.

convert_temperature(temperature, unit): Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit). It calls the appropriate conversion function based on the unit and returns the converted temperature.

Tips:
Remember these formulas:

Fahrenheit = (Celsius * 9/5) + 32

Celsius = (Fahrenheit - 32) * 5/9

Example usage:
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")

Expected output:
25°C is equal to 77.0°F
77°F is equal to 25.0°C
'''


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")
