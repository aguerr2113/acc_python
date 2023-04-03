# 1. Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, then someone else’s name. Then, write your age to
# the file. Close the file.

# 2. Open my_name.txt in notepad and view the contents.

# 3. Write a program that opens the my_name.txt file that was created by the
# program in problem 1, reads the names from the file, displays the names on the
# screen. Read your age and divide it by two. Print both age and age divided by 2
# and then close the file. Don’t forget to strip off the newline character when you
# read in the names and convert the age to int.

# 4. Turn in your program to the practice assignment link in course
# content

def read_div():
    # 3. Write a program that opens the my_name.txt file that was created by the
    # program in problem 1, reads the names from the file, displays the names on the
    # screen.
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


def main():
    age = 33
    # 1. Write a program that opens an output file with the filename my_name.txt,
    outfile = open('my_name.txt', 'w')
    # writes your name to the file, then someone else’s name. Then, write your age to
    outfile.write('name = Artemio Guerrero\n')
    outfile.write('name = Edmund Burke\n')
    outfile.write(f'age = {age}\n')

    outfile.close()





    read_div()



if __name__ == '__main__':
    main()








Practice Assignment Ch. 6-1
1. Write a program that opens an output file with the filename my_name.txt,
writes your name to the file, then someone else’s name. Then, write your age to
the file. Close the file.
2. Open my_name.txt in notepad and view the contents.
3. Write a program that opens the my_name.txt file that was created by the
program in problem 1, reads the names from the file, displays the names on the
screen. Read your age and divide it by two. Print both age and age divided by 2
and then close the file. Don’t forget to strip off the newline character when you
read in the names and convert the age to int.
4. Turn in your program to the practice assignment link in course
content.
Practice Assignment Ch. 6-2
Program 1 - Write numbers to a file:
1. Open an output file with the filename number_list.txt
2. Use a loop to write the numbers 50 through 100 to the
file, and then close the file. Be sure to save your file to
use in the next assignment
Program 2 – Read numbers from a file:
1. Open the file you just created.
2. Read all the numbers from the file and display them.
Terminate the loop by detecting end of file with a for loop
(the second method we discussed).
Turn in your two program files to the practice assignment link
in course content.


can you give each program a file name with a name that associates it with the programs purpose