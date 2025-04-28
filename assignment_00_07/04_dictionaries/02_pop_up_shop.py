
def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        
        # Handle invalid input gracefully
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
                if amount_bought < 0:
                    print("Please enter a valid positive number.")
                    continue
                break  # Exit loop if valid input is given
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        total_cost += (price * amount_bought)
    
    print(f"Your total is ${total_cost:.2f}")  # Formatted output to show two decimal points

if __name__ == '__main__':
    main()
