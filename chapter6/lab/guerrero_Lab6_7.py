# Artemio Guerrero,
# complete

import random


def main():
    try:
        # Prompt the user to specify the number of random numbers to generate
        user_number = int(input('How many random numbers do you want to generate? '))

        # Open the file for writing
        outfile = open('random_numbers.txt', 'w')

        # Generate the specified number of random numbers and write them to the file
        for i in range(user_number):
            random_number = random.randint(1, 500)
            outfile.write(str(random_number) + "\n")

        # Close the file
        outfile.close()

        # Display a success message
        print(f"{user_number} random numbers have been written to random_numbers.txt.")
    except IOError:
        print("Error: File could not be opened for writing")
    except ValueError:
        print("Error: Invalid input, please enter a valid integer")
    except:
        print("An unspecified error occurred")


if __name__ == '__main__':
    main()
