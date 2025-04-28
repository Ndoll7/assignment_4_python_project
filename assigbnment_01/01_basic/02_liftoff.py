
import time

def main():
    

    print("Counting Star...")
    count_num = 10

    while count_num > 0:
        print(count_num, end=" ", flush=True)
        time.sleep(1)  #  adds a 1-second pause between numbers
        count_num -= 1

    print("Liftoff!")
    
    
    
if __name__ == "__main__":
    main()
