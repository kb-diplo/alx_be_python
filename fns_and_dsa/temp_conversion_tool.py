# Global conversion factors  
# temp_conversion_tool.py  

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  
FREEZING_C_POINT = 32  

def convert_to_celsius(fahrenheit):  
    global FAHRENHEIT_TO_CELSIUS_FACTOR  
    celsius = (fahrenheit - FREEZING_C_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR  
    return celsius  

def convert_to_fahrenheit(celsius):  
    global CELSIUS_TO_FAHRENHEIT_FACTOR  
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_C_POINT  
    return fahrenheit  

def main():  
    try:  
        temp = float(input("Enter the temperature to convert: "))  
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  

        if unit == 'C':  
            result = convert_to_fahrenheit(temp)  
            print(f"{temp}°C is {result}°F")  
        elif unit == 'F':  
            result = convert_to_celsius(temp)  
            print(f"{temp}°F is {result}°C")  
        else:  
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")  
    except ValueError as e:  
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")  

if __name__ == "__main__":  
    main()
