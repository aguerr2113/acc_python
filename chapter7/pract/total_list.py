# Practice Assignment Ch. 7-3

# 3. The main function will join the two lists together, sort
# the resulting 10 integer list, and pass it to the
# total_list function
# 4. The total_list function will total the integers in the
# list and return the total to the main function
# 5. The main function will print the list, print the total, and
# print the maximum and minimum values in the list.
# Turn in your program to the practice assignment
# link in course content.

# 1. and a sub-function called total_list.
# def total_list():
def total_list(lists):
    total = sum(lists)

    return total


# 1. Write a program that contains a main function

def main():

#  2. The main function will create two lists containing five
# integers (of your choosing) each
    list_one = [1,21,13,4,15]
    list_two = [61,17,81,19,10]
#  3. The main function will join the two lists together,sort
    new_list = list_one + list_two
    new_list.sort()
# 4. pass it to the total_list function
# 4. The total_list function will total the integers in the
# list and return the total to the main function
    total = total_list(new_list)
# 5. The main function will print the list, 
    print(f"The combined sorted list is: {new_list}")
# print the total, 
    print(f'The total sum of the list is: {total}')
# and print the maximum and minimum values in the list.
    print(f"the minimum value is: {min(new_list)}")
    print(f"the maximum value is: {max(new_list)}")

main()

    