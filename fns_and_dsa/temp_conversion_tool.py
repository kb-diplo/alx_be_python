# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Define conversion functions
def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

# Get user input with validation and retry
while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit.upper() in ("C", "F"):
            break
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Perform conversion and display result
if unit.upper() == "F":
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
elif unit.upper() == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
