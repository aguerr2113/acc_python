# Practice Assignment Ch. 4-3
# 
# Artemio Guerrero,
# complete,
# this Asks the user for a positive integer no greater than 15,
# Asks the user for a character to use to create the square.
# The program should display a square on the screen with the
# number of rows and columns entered by the user using the
# character provided by the user.

pos = int(input('please give a positive integer no greater than 15:'))
char = input('please choose a character to create a square:')
# this Asks the user for a positive integer no greater than 15,
#
# Feedback to Learner
# 2/20/23 7:29 AM
# In 4-3 wrong logic not accepting even number. Keep it simple 
while pos < 1 or pos > 15:
    print('Error')
    pos = int(input('please give a positive integer no greater than 15...:'))
# this iterates the outer loop
for p in range(pos):
    # this iterates the inner loop
    for p in range(pos):
        print(char, end='')
    print()
