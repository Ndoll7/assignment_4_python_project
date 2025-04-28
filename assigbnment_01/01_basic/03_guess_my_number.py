import random

def main():

    secret_numb:int = random.randint(0,99)
    print("I am thinking of a number between 1 and 99...")

    user:int = int(input("Enter a number:"))
    while secret_numb != user:
        if user < secret_numb:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")

            print() 
        user: int = int(input("Enter a new guess: "))  
        
    print("Congrats! The number was: " + str(secret_numb))
    
if __name__ == '__main__':
    main()