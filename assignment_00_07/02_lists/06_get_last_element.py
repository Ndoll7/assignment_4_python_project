def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[len(lst) - 1])

# There is no need to edit code beyond this point

def get_lst():
    
    lst = []
    user_input: str = input("Please enter an element of the list or press enter to stop. ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()