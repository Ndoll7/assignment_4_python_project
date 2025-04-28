def main():

    number: float = float(input("Type a number to see its square: "))

    # square = number ** 2
    square = number * number

    print(f"{number} squared is {square}")

    # print(str(number) + " squared is " + str(number ** 2))

if __name__ == '__main__':
    main()