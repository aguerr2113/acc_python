# Practice Assignment Ch. 4-1
# ----------------------------------------------------------
# Artemio Guerrero,
# complete,
# this program uses a loop and asks the user to enter 2 numbers, then the numbers are addes and the sum is displayed
# the loop then causes the program to ask the user if he or she wishes to perform the op again.
# if they choose to repeat it continues other wise it terminates

# while loop
while True:
# beginning of peramters that asks the user for two numbers. each number is stored seperately
    print('please enter two numbers')
    num1 = int(input('please enter your first number:'))
    num2 = int(input('please enter your second number:'))
# this prints the sum of both numbers
    print(f'sum = {num1+num2}')
# here we use a condition to choose to break the loop by asking if they want to continue.if they choose y it continues.if they choose anything else it ends
    command = input('do you wish to do this again?y/n: ')
    if command != 'y':
        break

