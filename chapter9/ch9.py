
# Exercise 1: Creating a Dictionary
# Write a Python program that asks the user to enter the name and age of three people, and stores this information in a dictionary. The keys in the dictionary should be the names of the people, and the values should be their ages. After the information has been entered, print out the dictionary.
########################################################################################################################################################
# Example output:
# Enter the name of person 1: John
# Enter the age of person 1: 30
# Enter the name of person 2: Sarah
# Enter the age of person 2: 25
# Enter the name of person 3: Michael
# Enter the age of person 3: 45
# {'John': 30, 'Sarah': 25, 'Michael': 45}

########################################################################################################################################################

# people_dict = {}

# for num in range(3):

#     name = input(f"Enter the name of person {num+1}: ")
#     age = int(input(f"Enter the age of person {num+1}: "))

#     people_dict[name] = age
# print(people_dict)
########################################################################################################################################################

# Exercise 2: Retrieving a Value from a Dictionary
# Write a Python program that stores the price of a set of products in a dictionary. The keys in the dictionary should be the names of the products, and the values should be their prices. Ask the user to enter the name of a product, and then use the dictionary to retrieve and print the price of that product. If the product does not exist in the dictionary, print an appropriate message.

# Example output:
# Enter the name of a product: Shirt
# The price of Shirt is $25.

# Enter the name of a product: Hat
# Sorry, the product Hat does not exist in our inventory.

########################################################################################################################################################

# ret_valv = {'shirt':25,'shoes':50,'shorts':12.5,'pants':45}

# prod = input("Enter name of product: ")
# if prod  in ret_valv:
#     print(f"The {prod} costs ${ret_valv[prod]}")
# else:
#     print(f"The product {prod} doesnt exist")

########################################################################################################################################################

# Exercise 3: Updating a Dictionary
# Write a Python program that stores the phone numbers of a set of people in a dictionary. The keys in the dictionary should be the names of the people, and the values should be their phone numbers. Ask the user to enter the name of a person, and then ask the user to enter the person's new phone number. Use the dictionary to update the person's phone number, and then print out the updated dictionary.

# Example output:
# Enter the name of a person: John
# Enter the new phone number for John: 555-1234
# {'John': '555-1234', 'Sarah': '555-5678', 'Michael': '555-4321'}


########################################################################################################################################################

# Exercise 1: Deleting Elements

# Create a dictionary called shopping_list with the following key-value pairs:
# 'apples': 5
# 'bananas': 2
# 'bread': 1
# 'eggs': 6
# Delete the 'bread' key and its value from the shopping_list dictionary using the del statement.
# Check if the 'bread' key still exists in the shopping_list dictionary using the in operator. Print a message indicating whether the key exists or not.
########################################################################################################################################################

# shopping_list = {'apples':5,'bananas': 2,'bread': 1,'eggs': 6}
# del shopping_list['bread']
# print(shopping_list)


########################################################################################################################################################
# Exercise 2: Getting the Number of Elements in a Dictionary

# Create a dictionary called words with the following key-value pairs:
# 'apple': 'a fruit'
# 'carrot': 'a vegetable'
# 'pizza': 'a food'
# 'book': 'a thing to read'
# Use the len function to get the number of elements in the words dictionary and assign it to a variable called num_words.
# Print the value of the num_words variable.
########################################################################################################################################################

# words = {
#     'apple': 'a fruit',
#     'carrot': 'a vegetable',
#     'pizza': 'a food',
#     'book': 'a thing to read'
# }
# num_words = len(words)

# print(f'words in words dictionary{words}')
# print(f'amount of words in words dictionary{num_words}')

########################################################################################################################################################


# Exercise 3: Mixing Data Types in a Dictionary

# Create a dictionary called students with the following key-value pairs:
# 'John': [85, 90, 92]
# 'Sarah': [80, 88, 91]
# 'Mike': [92, 93, 89]
# Access the list of test scores for 'John' and assign it to a variable called john_scores.
# Print the value of the john_scores variable.
########################################################################################################################################################

# students = {
#     'John': [85, 90, 92],
#     'Sarah': [80, 88, 91],
#     'Mike': [92, 93, 89]
# }

# john_scores = students['John']

# print(f'johns scores are {john_scores}')
########################################################################################################################################################

# Exercise 1: Create a Dictionary and Print Its Elements

# Write a program that creates an empty dictionary called car_prices and then prompts the user to enter the prices of three cars (make and model do not matter). The program should add the prices to the dictionary and then use a for loop to print each car's make and price.

# Enter the price of car 1: 15000
# Enter the price of car 2: 20000
# Enter the price of car 3: 18000

# Car Prices:
# Car 1: $15000
# Car 2: $20000
# Car 3: $18000


########################################################################################################################################################
# Exercise 1: Create a Dictionary and Print Its Elements

# car_prices = {}

# for num in range(3):
#     price = int(input(f"Enter the price of car {num+1}: "))
#     car_prices[num+1] = price
    
# print('Car Prices:')
# for key in car_prices:

#     print(f'Car {key}: ${car_prices[key]}')




########################################################################################################################################################
# Exercise 2: Modify a Dictionary Using User Input

# Write a program that creates a dictionary called grocery_list with three items and their quantities. The program should prompt the user to add or remove items from the list and update the dictionary accordingly. Use a while loop to continue prompting the user until they choose to quit.

# Example output:

# Current Grocery List: 
# - Eggs: 1 dozen
# - Milk: 2 cartons
# - Bread: 1 loaf

# Do you want to add or remove an item? (Type 'quit' to exit): add
# Enter the name of the item to add: Cheese
# Enter the quantity: 2 blocks

# Updated Grocery List: 
# - Eggs: 1 dozen
# - Milk: 2 cartons
# - Bread: 1 loaf
# - Cheese: 2 blocks

# Do you want to add or remove an item? (Type 'quit' to exit): remove
# Enter the name of the item to remove: Bread

# Updated Grocery List: 
# - Eggs: 1 dozen
# - Milk: 2 cartons
# - Cheese: 2 blocks

# Do you want to add or remove an item? (Type 'quit' to exit): quit



########################################################################################################################################################

# Exercise 2: Modify a Dictionary Using User Input
# grocery_list = {'eggs':12,'apples':4,'oranges':3}
# add = 'add'
# remove = 'remove'
# quit = 'quit'

# while True:
#     add_remove = input('Do you want to add or remove an item?(Type"quit" to exit):')

#     if add_remove == add:
#         item = input('Enter the name of the item to add: ')
#         quant = int(input('Enter the quantity: '))
#         grocery_list[item] = quant

#         print('Updated Grocery List: ')
#         for key in grocery_list:
#             print(f'{key}: {grocery_list[key]}')


#     elif add_remove == remove:

#         item = input('Enter the name of the item to remove: ')
#         if item == grocery_list:

#             grocery_list.pop(item)

#             print('Updated Grocery List: ')
            
#             for key in grocery_list:
#                 print(f'{key}: {grocery_list[key]}')

#         else:
        
#             print('invalid Try again')



#     elif add_remove == quit:
#         print('exitint list program')
#         break

#     else:
#         print('invalid Try again')


########################################################################################################################################################
# Exercise 3: Dictionary Methods

# Write a program that creates a dictionary called book_reviews with at least three books and their ratings. The program should use the items() method to print all the books and their ratings in the format "Book Title: Rating".

# Example output:

# Book Reviews:
# - To Kill a Mockingbird: 4.5 stars
# - The Great Gatsby: 3.8 stars
# - 1984: 4.2 stars

########################################################################################################################################################
########################################################################################################################################################
# book_reviews = {
#     "To Kill a Mockingbird": 4.5,
#     "The Great Gatsby": 3.8,
#     "1984": 4.2
# }
# print(book_reviews.items())
# for key in book_reviews:
#     print(f'- {key}: {book_reviews[key]} stars')


########################################################################################################################################################
########################################################################################################################################################
# LOOK_UP = 1
# ADD = 2
# CHANGE = 3
# DELETE = 4
# SEE_ALL = 5
# QUIT = 6


# # main function
# def main():
#     # Create an empty dictionary.
#     movies = {
#     "The Shawshank Redemption": "1994",
#     "The Godfather": "1972",
#     "The Dark Knight": "2008",
#     "Pulp Fiction": "1994",
#     "The Lord of the Rings: The Fellowship of the Ring": "2001"
# }

#     # Initialize a variable for the user's choice.
#     choice = 0

#     while choice != QUIT:
#         # Get the user's menu choice.
#         choice = get_menu_choice()

#         # Process the choice.
#         if choice == LOOK_UP:
#             look_up(movies)
#         elif choice == ADD:
#             add(movies)
#         elif choice == CHANGE:
#             change(movies)
#         elif choice == DELETE:
#             delete(movies)
#         elif choice == SEE_ALL:
#             see_all(movies)
# def get_menu_choice():
#     print()
#     print('Movies---------Release-Date')
#     print('---------------------------')
#     print('1. Look up a Movie')
#     print('2. Add a Movie')
#     print('3. Change a Movie')
#     print('4. Delete a Movie')
#     print('5. See all Movies')
#     print('6. Quit the program')
#     print()

#     # Get the user's choice.
#     choice = int(input('Enter your choice: '))

#     # Validate the choice.
#     while choice < LOOK_UP or choice > QUIT:
#         choice = int(input('Enter a valid choice: '))

#     # return the user's choice.
#     return choice

# def look_up(movies):
#     # Get a name to look up.
#     name = input('Enter a movie title: ')

#     # Look it up in the dictionary.
#     print(movies.get(name, 'Not found.'))

# def add(movies):
#     # Get a name to look up.
#     title = input('Enter a movie title: ')
#     date = input('Enter a release date: ')

#     # Look it up in the dictionary.
#     movies[title] = date
#     for key in movies:
#         print(f'{key}: {movies[key]}')


# def change(movies):
#     # Get a name to look up.
#     name = input('Enter a name: ')

#     if name in movies:
#         # Get a new birthday.
#         date = input('Enter the new date: ')

#         # Update the entry.
#         movies[name] = date
#     else:
#         print('That name is not found.')

# # The delete function deletes an entry from the
# # birthdays dictionary.
# def delete(movies):
#     # Get a name to look up.
#     name = input('Enter a movie title: ')

#     # If the name is found, delete the entry.
#     if name in movies:
#         del movies[name]
#     else:
#         print('That name is not found.')


# def see_all(movies):
#     for key in movies:
#         print(f'{key}: {movies[key]}')
# # Call the main function.
# if __name__ == '__main__':
#     main()

########################################################################################################################################################
# Phonebook Dictionary Pickling:
# Write a Python program that creates a dictionary of names and phone numbers, then pickles the dictionary to a file. After pickling, the program should unpickle the dictionary from the file and display its contents.

# This program demonstrates object pickling and unpickling.
import pickle

# The save_data function gets data about a person,
# stores it in a dictionary, and then pickles the
# dictionary to the specified file.
def save_data(file):
    # Create an empty dictionary.
    phonebook = {}

    # Get data for a person and store
    # it in the dictionary.
    phonebook['name'] = input('Name: ')
    phonebook['numbers'] = int(input('phonenumber: '))

    # Pickle the dictionary.
    pickle.dump(phonebook, file)

# The display_data function displays the person data
# in the dictionary that is passed as an argument.
def display_data(phonebook):
    print('Name:', phonebook['name'])
    print('Phonenumber:', phonebook['numbers'])
    print()

# main function
def main():
    again = 'y'  # To control loop repetition

    # Open a file for binary writing.
    output_file = open('chinfo.dat', 'wb')

    # Get data until the user wants to stop.
    while again.lower() == 'y':
        # Get data about a person and save it.
        save_data(output_file)

        # Does the user want to enter more data?
        again = input('Enter more data? (y/n): ')

    # Close the file.
    output_file.close()

    end_of_file = False  # To indicate end of file

    # Open the file for binary reading.
    input_file = open('chinfo.dat', 'rb')

    # Read to the end of the file.
    while not end_of_file:
        try:
            # Unpickle the next object.
            person = pickle.load(input_file)

            # Display the object.
            display_data(person)
        except EOFError:
            # Set the flag to indicate the end
            # of the file has been reached.
            end_of_file = True

    # Close the file.
    input_file.close()

# Call the main function.
if __name__ == '__main__':
    main()





########################################################################################################################################################

########################################################################################################################################################
# Shopping List Dictionary Pickling:
# Write a Python program that creates a dictionary of shopping lists (where each key is a store name and the corresponding value is a list of items to buy at that store), then pickles the dictionary to a file. After pickling, the program should unpickle the dictionary from the file and display its contents.



########################################################################################################################################################

########################################################################################################################################################
# Word Count Dictionary Pickling:
# Write a Python program that reads in a text file and creates a dictionary where each key is a word and the corresponding value is the number of times that word appears in the file. The program should then pickle the dictionary to a file. After pickling, the program should unpickle the dictionary from the file and display the 10 most common words and their counts.


########################################################################################################################################################

########################################################################################################################################################

########################################################################################################################################################

########################################################################################################################################################

########################################################################################################################################################

########################################################################################################################################################
########################################################################################################################################################

########################################################################################################################################################
########################################################################################################################################################

########################################################################################################################################################
########################################################################################################################################################

########################################################################################################################################################
########################################################################################################################################################

########################################################################################################################################################
########################################################################################################################################################
