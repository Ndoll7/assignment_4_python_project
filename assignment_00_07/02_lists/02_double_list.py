def main():
    number: list[int] = [9, 8, 7, 6, 5]  

    for num in range(len(number)):  
        sum_of_list = number[num]  
        number[num] = sum_of_list * 2 

    print(number) 


if __name__ == '__main__':
    main()

