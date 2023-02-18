# Practice Assignment Ch. 4-1
# ----------------------------------------------------------------------
#  Artemio Guerrero,
# complete,
# here inputs aquire the date from the userbybasking for them to choose a number and returning a day of the  week that corresponds with said number.if the user chooses a number more than 7 or less than 0 it asks the user to choose a number.
# once the program is finished the user is asked to choose a number again or quit.

# here we use a while loop to keep asking the user for the input
while True:
    num =int(input('choose a number 1-7 or type 0 to quit:'))
# he i put in a condition of if user chooses to quit by picking 0 then the loop breaks and the program ends.
    if num == 0:
        break
    elif num > 7 or num <0:
        print("please choose a number between 1 and 7")
    elif num == 1:
        print ('Monday')
    elif num == 2:
        print ('Tuesday')
    elif num == 3:
        print ('Wednesday')
    elif num == 4:
        print ('Thursday')
    elif num == 5:
        print ('Friday')
    elif num == 6:
        print ('Saturday')
    else:
        print('Sunday')


