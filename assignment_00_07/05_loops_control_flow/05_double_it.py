def main():
    # Take user input and convert it to an integer
    user_input = int(input("Enter a number: "))
    
    # Initialize curr_value with the user input
    curr_value = user_input
    
    # Loop runs as long as curr_value is less than or equal to 100
    while curr_value <= 100:
        curr_value = curr_value * 2  # Double the value
        print(f"{user_input} is Double {curr_value}")

if __name__ == '__main__':
    main()
