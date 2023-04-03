# 1. Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, then someone else’s name. Then, write your age to
# the file. Close the file.
def main():
    age = 33
    # 1. Write a program that opens an output file with the filename my_name.txt,
    outfile = open('my_name.txt', 'w')
    # writes your name to the file, then someone else’s name. Then, write your age to
    outfile.write('name = Artemio Guerrero\n')
    outfile.write('name = Edmund Burke\n')
    outfile.write(f'age = {age}\n')

    outfile.close()




if __name__ == '__main__':
    main()