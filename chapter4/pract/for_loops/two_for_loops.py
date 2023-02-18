# Practice Assignment Ch. 4-2
# ----------------------------------------------------------------
# Artemio Guerrero,
# complete,
# the program will ask user for two numbers
#####
# in the 1st loop, the low number will be the starting point for the loop and the
# high will be the ending point. The loop should display the iterator number and
# that number x 10 on the same line, separated by a tab.
#####
# The second loop should accumulate all the numbers between the starting point
# and ending point

print('choose two numbers please...:')
num1 = int(input('choose your first number:'))
num2 = int(input('choose your second number:'))

# here is the for loop with range being used for the loop.
# since the smaller number is used to start off the sequence i used a if elif logic so that if the user chooses a smaller number second we use a differnt loop to achieve the smame result.
if num1 < num2:
    for num in range(num1,(num2+1)):
        ten = num * 10
        print(f'{num}\t{ten}')

else:
    for num in range(num2,(num1+1)):
        ten = num * 10
        print(f'{num}\t{ten}')
# ################################################################
# second loop starts here
# here total is an accumulator
total = 0

num1 = int(input('choose your first number:'))
num2 = int(input('choose your second number:'))


if num1 < num2:
    for num in range(num1,(num2+1)):
        ten = num * 10
        # here we use the accumulate to add the results of the loop
        total += ten
        print(f'{num}\t{ten}')


else:
    for num in range(num2,(num1+1)):
        ten = num * 10
        # here we use the accumulate to add the results of the loop
        total += ten
        print(f'{num}\t{ten}')
# total is displayed
print(f'The total is {total}.')