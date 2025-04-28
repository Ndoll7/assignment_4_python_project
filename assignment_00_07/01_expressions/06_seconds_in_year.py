DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    
    SECOND_IN_YEAR = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    print(f"There are {SECOND_IN_YEAR} seconds in a year!")
#  print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


if __name__ == '__main__':
    main()