# 1. Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, then someone else’s name. Then, write your age to the file. Close the file.

# 2. Open my_name.txt in notepad and view the contents.



# 4. Turn in your program to the practice assignment link in course
# content.



# 1. Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, then someone else’s name. Then, write your age to the file. Close the file.
def main():
    age = 33
    outfile = open('my_name.txt', 'w')
    outfile.write('name = Artemio Guerrero\n')
    outfile.write('name = Edmund Burke\n')
    outfile.write(f'age = {age}\n')

    outfile.close()


# 3. Write a program that opens the my_name.txt file that was created by the
# program in problem 1, reads the names from the file, displays the names on the
# screen. Read your age and divide it by two. Print both age and age divided by 2
# and then close the file. Don’t forget to strip off the newline character when you
# read in the names and convert the age to int.

    def read_div():
        infile = open('my_name.txt', 'r')
        div_age = age / 2

        file_contents = infile.read()
        infile.close()

        print(file_contents)
        print(f'age divided by 2 = {div_age}\n')

        infile.close()
    read_div()







if __name__ == '__main__':
    main()


# 3. Write a program that opens the my_name.txt file that was created by the
# program in problem 1, reads the names from the file, displays the names on the
# screen. Read your age and divide it by two. Print both age and age divided by 2
# and then close the file. Don’t forget to strip off the newline character when you
# read in the names and convert the age to int.
