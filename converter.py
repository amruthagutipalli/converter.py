import argparse

def celsius_to_fahrenheit(celsius):
    '''Convert Celsius to Fahrenheit.'''
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Convert temperature between Celsius and Fahrenheit.')

    # Add the arguments
    parser.add_argument('temperature', type=float, help='Temperature value to convert')
    parser.add_argument('--to-fahrenheit', action='store_true', help='Convert from Celsius to Fahrenheit')
    parser.add_argument('--to-celsius', action='store_true', help='Convert from Fahrenheit to Celsius')

    # Parse the arguments
    args = parser.parse_args()

    # Perform the conversion based on the specified option
    if args.to_fahrenheit:
        fahrenheit = celsius_to_fahrenheit(args.temperature)
        print(f'{args.temperature}°C is equal to {fahrenheit:.2f}°F')
    elif args.to_celsius:
        celsius = fahrenheit_to_celsius(args.temperature)
        print(f'{args.temperature}°F is equal to {celsius:.2f}°C')
    else:
        print("Please specify a conversion option: --to-fahrenheit or --to-celsius.")

if __name__ == '__main__':
    main()