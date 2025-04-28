def add_numbers(numbers)-> int:
    

    total: int = 0
    for number in numbers:
        total += number

    return total

# There is no need to edit code beyond this point

def main():
    numb_list: list[int] = [2, 7, 8, 3, 5]  
    sum_of_numbers: int = add_numbers(numb_list)  
    print(sum_of_numbers)  
    

if __name__ == '__main__':
    main()