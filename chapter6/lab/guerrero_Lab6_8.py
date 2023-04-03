# Artemio Guerrero,
# complete,
def main():
    try:
        # Open the file for reading
        file = open("random_numbers.txt", "r")

        # Initialize variables to keep track of the total and the number of random numbers read
        total = 0
        num_random_numbers = 0

        # Read the file line by line and process each random number
        for line in file:
            try:
                random_number = int(line.strip())
                print(random_number)
                total += random_number
                num_random_numbers += 1
            except ValueError:
                print(f"Invalid data found in the file: {line.strip()}")

        # Close the file
        file.close()

        # Check if no random numbers were read from the file
        if num_random_numbers == 0:
            raise ValueError("No valid random numbers were found in the file")

        # Calculate the average and display the results
        average = total / num_random_numbers
        print(f"Total: {total}")
        print(f"Number of random numbers read: {num_random_numbers}")
        print(f"Average: {average}")
    except IOError:
        print("Error: File not found or could not be opened")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except:
        print("An unspecified error occurred")


if __name__ == '__main__':
    main()
