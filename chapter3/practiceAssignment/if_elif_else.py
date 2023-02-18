num =int(input('choose a number 1-7:'))

if num > 7 or num <1:
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

