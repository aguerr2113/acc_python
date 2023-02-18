# Artemio Guerrero,
# complete,
# here inputs aquire the date from the user
month = int(input("Enter a month(1-12):"))
day = int(input('Enter a day(1-31):'))
year = int(input('Enter a two digit year(00-99):'))

# here we use if else statements to determine whether the month*date is equal to the last two digits of the year

if month * day == year:
    print('The date is magic!')

else:
    print('The date is not magic')
