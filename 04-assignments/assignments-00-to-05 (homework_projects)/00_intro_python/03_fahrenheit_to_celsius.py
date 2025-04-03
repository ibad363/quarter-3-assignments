def main():
    # Prompt the user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    degrees_celcius = (degrees_fahrenheit- 32) * 5.0/9.0
    
    # Print the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celcius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()