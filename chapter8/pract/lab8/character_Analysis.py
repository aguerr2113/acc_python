# Artemio Guerrero,
# complete
# Problem 1. Character Analysis –Use the file text.txt that is attached to Blackboard.   Write a program that reads the file’s contents and determines the following:

# The number of uppercase letters in the file
# The number of lowercase letters in the file
# The number of digits in the file
# The number of whitespace characters in the file

# Output should look like this:




def main():
        # 1. Open the file you just created.
        infile = open('text.txt', 'r')

        infile_contents = infile.read()
        
        uppercase = 0
        lowercase = 0
        digits = 0
        spaces = 0

        for char in infile_contents:

            if char.isupper():
                uppercase += 1
            elif char.islower():
                lowercase += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

        print(f'Uppercase letters: {uppercase}')
        print(f'Lowercase letters: {lowercase}')
        print(f'Digits: {digits}')
        print(f'Spaces: {spaces}')
        
        infile.close()



if __name__ == '__main__':
    main()