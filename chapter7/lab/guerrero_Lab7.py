# Artemio Guerrero,
# complete
# This Python program defines a function display_larger that accepts a list of numbers and a number n, and returns a new list containing all numbers greater than n. The main function takes user input for a list of 10 integers and a search number n, and calls the display_larger function to display the original list, n, and the list of numbers greater than n.

# 1 Write a function that accepts two arguments: a list, and a number n.
def display_larger(list,n):
# 2 Assume that the list contains numbers.
    large_list = []
    for num in list:
# 3 The function should display all of the numbers in the list that are greater than the number n.
        if num > n:
            large_list.append(num)
    print(f"list of numbers: {list}")
    print(f"Number: {n}")
    print(f"List of numbers greater than {n}: {large_list}")

def main():
    list = []
    for i in range(10):
# 6 The main function should accept input of a series of 10 integers from the user and an integer n that will be the search number.
        num = int(input("Enter a number: "))
        list.append(num)
    n = int(input("enter the number you wish to test if the list elements are greater than: "))
# 7 Call the function display_larger from main and pass 2 arguments: the 10 integers stored in a list, and the number n.
    display_larger(list,n)
    
if __name__ == '__main__':
    main()
