# 1. Write a program that uses the file you created in 6 – 2 called
# number_list.txt
# 2. Your program should read in number_list.txt and calculate the sum and
# average of all the numbers and display the sum and the average.
# 3. Additionally, it should:
# a. Handle any IOError exceptions that are raised when the file is opened and
# data is read from it
# b. Handle any ValueError exceptions that are raised when the items read are
# converted to numbers
# c. Handle any other unspecified errors

def main():

    number_file = "number_list.txt"
    try:
        f = open(number_file)

        count = 0
        total = 0
        for line in f:
            try:
                # Convert the line to an integer and add it to the total
                number = int(line.strip())
                total += number
                # Increment the count
                count += 1
            except ValueError:
                print("Error: the file contains non-numeric data")
                f.close()
                exit()
        # Close the file
        f.close()
        if count > 0:
            average = total / count
            print("Sum:", total)
            print("Average:", average)
        else:
            # If the file is empty, print an error message
            print("Error: the file is empty")
    except IOError as e:
        # If there is an IO error (e.g. file not found), print an error message
        print("Error opening or reading file:", e)
    except Exception as e:
        # If there is any other kind of error, print an error message
        print("Error:", e)


# If this file is being run as the main program, call the main function
if __name__ == '__main__':
    main()

