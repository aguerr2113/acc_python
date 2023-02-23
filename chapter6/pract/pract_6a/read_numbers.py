# Program 2 – Read numbers from a file:
    # 1. Open the file you just created.
    
    # 2. Read all the numbers from the file and display them.
    # Terminate the loop by detecting end of file with a for loop
    # (the second method we discussed).

# Turn in your two program files to the practice assignment link
# in course content.

def main():
        infile = open('number_list.txt', 'r')

        for line in infile:
            amount = int(line)

            print(amount)

        infile.close()

if __name__ == '__main__':
    main()