import random

dice_roll = 6

def main():

    dice_1:int = random.randint(1, dice_roll)
    dice_2:int = random.randint(1, dice_roll)

    total_dice = dice_1 + dice_2

    print(f"Dice have {dice_roll} sides each.")
    print(f"First die: {dice_1}")
    print(f"Second die: {dice_2}")
    print(f"Total of two dice: {total_dice}")

if __name__ == '__main__':
    main()

