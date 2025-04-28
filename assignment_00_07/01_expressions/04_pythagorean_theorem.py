import math  

def main():
   
    ab: float = float(input("\033[1;3m Enter the length of AB: \033[0m"))
    ac: float = float(input("\033[1;3m Enter the length of AC: \033[0m"))

   
    bc: float = math.sqrt(ab**2 + ac**2)
    
    print("The length of BC the hypotenuse is: " + str(bc))


if __name__ == '__main__':
    main()