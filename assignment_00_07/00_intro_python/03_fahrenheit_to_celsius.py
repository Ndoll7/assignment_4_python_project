def main():

    degrees_fahrenheit= float(input("\033[1;3m Enter temperature in Fahrenheit:"))

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C \033[0m")

if __name__ == '__main__':
    main()