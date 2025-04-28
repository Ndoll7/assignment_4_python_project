import random


NUM_SIDES = 6

def roll_dice():


    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"Die1: {die1}, Die2: {die2}, Total: {total}")

def main():
    die1: int = 10
    print(f"die1 in main starts as: {die1} ")

    for _ in range(3):
        roll_dice()

    print(f"die1 in main is still: {die1} " )


if __name__ == '__main__':
    main()