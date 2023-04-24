#Artemio Guerrero
#complete

# Practice Assignment Ch. 9-2
# Still in the groups from last class (online students do remainder of assignment), using
# the dictionary application you created, add two new menu items:
#  Save the dictionary – write a function to pickle the dictionary to a file
#  Retrieve the dictionary – write a function to retrieve the pickled
# dictionary that was saved earlier
#  Put both functions in a separate module that is imported by your main
# program

import pickle
########################################################################################################################################################
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SEE_ALL = 5
SAVE_DICT = 6
RETRIEVE_DICT = 7
QUIT = 8


# main function
def main():

        # Try to retrieve the dictionary from file
    try:
        movies = retrieve_dictionary()
    except EOFError:
        # If the file is not found, start with an empty dictionary
        movies = {
            "The Shawshank Redemption": "5",
            "The Godfather": "4",
            "The Dark Knight": "4",
            "Pulp Fiction": "4",
            "The Lord of the Rings: The Fellowship of the Ring": "5"
            }

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(movies)
        elif choice == ADD:
            add(movies)
        elif choice == CHANGE:
            change(movies)
        elif choice == DELETE:
            delete(movies)
        elif choice == SEE_ALL:
            see_all(movies)
        elif choice == SAVE_DICT:
            save_dictionary(movies)
        elif choice == RETRIEVE_DICT:
            retrieve_dictionary()
            print("Dictionary retrieved successfully.")
        elif choice == QUIT:
            print("Exiting program...")
        else:
            print("Invalid choice. Please try again.\n")


def get_menu_choice():
    print()
    print("Movies---------Release-Date")
    print("---------------------------")
    print("1. Look up a Movie")
    print("2. Add a Movie")
    print("3. Change a Movie")
    print("4. Delete a Movie")
    print("5. See all Movies")
    print("6. Save the Dictionary")
    print("7. Retrieve the Dictionary")
    print("8. Quit the program")
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

def look_up(movies):
    # Get a name to look up.
    name = input('Enter a movie title: ')

    # Look it up in the dictionary.
    print(movies.get(name, 'Not found.'))

def add(movies):
    # Get a name to look up.
    title = input('Enter a movie title: ')
    date = input('Enter your movie rating(0-5): ')

    # Look it up in the dictionary.
    movies[title] = date
    for key in movies:
        print(f'{key}: {movies[key]}')


def change(movies):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in movies:
        # Get a new birthday.
        date = input('Enter new rating(0-5): ')

        # Update the entry.
        movies[name] = date
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# birthdays dictionary.
def delete(movies):
    # Get a name to look up.
    name = input('Enter a movie title: ')

    # If the name is found, delete the entry.
    if name in movies:
        del movies[name]
    else:
        print('That name is not found.')


def see_all(movies):
    for key in movies:
        stars = int(float(movies[key]))
        print(f'{key}: {movies[key]} stars {"*" * stars}')

def save_dictionary(movies):

    output_file = open('info.dat', 'wb')
    # Pickle the dictionary.
    pickle.dump(movies, output_file)
    output_file.close()


def retrieve_dictionary():
    input_file = open('info.dat', 'rb')
    dictionary = pickle.load(input_file)
    input_file.close()
    for key in dictionary:
        stars = int(float(dictionary[key]))
        print(f'{key}: {dictionary[key]} stars {"*" * stars}')
    return dictionary


# Call the main function.
if __name__ == '__main__':
    main()

########################################################################################################################################################