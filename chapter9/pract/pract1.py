#Artemio Guerrero
#complete

# Practice Assignment Ch. 9-1
# 1. Classroom Sections: Group assignment – break into groups of 3 or 4.
# 2. Online students: do on your own.
# 3. Using the example of the birthday dictionary in Chapter 9, create a dictionary application, subject of your choosing
# (appropriate content)
# 4. In addition to the menu choices provided to the user in the example, add menu items to display the entire
# dictionary.
# 5. Each person will create a separate module for their function(s) with the main program importing all the modules.
#  Person 1 – main program/menu display, coordinates other programs
#  Person 2 – Look up and display functions
#  Person 3 – Add function
#  Person 4 - Change, and Delete functions
########################################################################################################################################################
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SEE_ALL = 5
QUIT = 6


# main function
def main():
    # Create an empty dictionary.
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
def get_menu_choice():
    print()
    print('Movies---------Release-Date')
    print('---------------------------')
    print('1. Look up a Movie')
    print('2. Add a Movie')
    print('3. Change a Movie')
    print('4. Delete a Movie')
    print('5. See all Movies')
    print('6. Quit the program')
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
# Call the main function.
if __name__ == '__main__':
    main()

########################################################################################################################################################