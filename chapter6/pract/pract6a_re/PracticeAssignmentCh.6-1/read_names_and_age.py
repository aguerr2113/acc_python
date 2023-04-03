# 3. Write a program that opens the my_name.txt file that was created by the
# program in problem 1, reads the names from the file, displays the names on the
# screen.
def read_div():

    infile = open('my_name.txt', 'r')
    file_contents = infile.read()
    infile.close()

 
    lines = file_contents.split('\n')
    # Don’t forget to strip off the newline character when you
    # read in the names and convert the age to int.
    my_name = lines[0].split('=')[1].strip()
    other_name = lines[1].split('=')[1].strip()

    age = int(lines[2].split('=')[1].strip())
    # Read your age and divide it by two
    div_age = age / 2

    print(f'My name is {my_name}')
    print(f'The other name is {other_name}')
    # Print both age and age divided by 2
    # and then close the file.
    print(f'My age is {age}')
    print(f'My age divided by 2 is {div_age}')
read_div()