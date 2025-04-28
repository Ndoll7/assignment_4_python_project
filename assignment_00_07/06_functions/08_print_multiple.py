def main():
    message = input("Please type a message:")
    repeats = int(input("Enter a number of times to repeat your message: "))
    repeats = (message + " ") * repeats
    print(repeats)

if __name__ == '__main__':
    main()