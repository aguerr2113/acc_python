# Artemio Guerrero,
# complete
# Problem 2.  Date Printer - Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.   It should print the date in the format March 12, 2018.  

# Sample dialog:
# Enter a date in the format mm/dd/yyyy: 01/16/2018
# January 16, 2018




def main():
    months = ['', 'January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    date_string = input("Enter a date in the format mm/dd/yyyy: ")
    month_str, day_str, year_str = date_string.split('/')
   
    month = months[int(month_str)]
    day = int(day_str)
    year = int(year_str)

    print(month,day,',',year)



main()
