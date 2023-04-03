# Program 1 - Write numbers to a file:
    # 1. Open an output file with the filename number_list.txt
    
    # 2. Use a loop to write the numbers 50 through 100 to the
    # file, and then close the file. Be sure to save your file to
    # use in the next assignment
def main():
    # 1. Open an output file with the filename number_list.txt
    outfile = open('number_list.txt', 'w')
    # 2. Use a loop to write the numbers 50 through 100
    for num in range(50,101):
        outfile.write(f'{num}\n')
    #  close the file.
    outfile.close()

if __name__ == '__main__':
    main()


