def main():

    num1: int = int(input("\033[1;3m Please enter an integer to be divided: \033[0m"))
    num2: int = int(input("\033[1;3m Please enter an integer to be divide by: \033[0m"))

    quotient: int = num1 // num2  # Divide with no remainder/decimals (integer division)
    remainder: int = num1 % num2  # Get the remainder of the division (modulo)

    print(f"The result of this division is {quotient}  with a remainder of {remainder}")

if __name__ == '__main__':
    main()