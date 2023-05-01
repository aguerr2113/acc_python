#Artemio Guerrero
#complete

import pets

def main():
    # Get a list of CellPhone objects.
    pets = make_list()

    # Display the data in the list.
    print('Here is the data you entered:')
    display_list(pets)

# The make_list function gets data from the user
# for five phones. The function returns a list
# of CellPhone objects containing the data.

def make_list():
    # Create an empty list.
    pet_list = []


    print('Enter data for your pet.')
    
    name = input('Enter the pets name: ')
    ani_type = input('Enter the type of pet: ')
    age = float(input('Enter the age of the pet: '))


    pet = pets.Pets(name, ani_type, age)

    # Add the object to the list.
    pet_list.append(pet)

    # Return the list.
    return pet_list

# The display_list function accepts a list containing
# CellPhone objects as an argument and displays the
# data stored in each object.

def display_list(pet_list):
    for item in pet_list:
        print(f'pets name: {item.get_name()}')
        print(f'pet type: {item.get_animal_type()}')
        print(f'pet age: {item.get_age()}')
        print()

# Call the main function.
if __name__ == '__main__':
      main()
