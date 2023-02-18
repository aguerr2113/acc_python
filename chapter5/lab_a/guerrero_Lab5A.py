# Artemio Guerrero,
# complete,
# Average Restaurant Rating and Number of Stars – A restaurant receives numeric scores of 0-10 from
# five different food critics. The higher the score, the better the rating. The average score translates into a
# 1 – 5 star rating.
# Write an IPO diagram and Python program that has two functions, main and determine_stars.
# main – Should accept input of five numeric ratings from the user USING A LOOP. It should then
# calculate the average numeric score for the restaurant. The numeric average should be passed to the
# determine_stars function.

# a main function to accept input from the user
# and calculate average and a second function to display the number of stars.

# Input Validation: The test scores entered by the user should be in the range 0-10
# Output: Display both the numeric average (rounded to two decimals) and the number of stars.

def main():
    total = 0
    for count in range(1,6):
        score = float(input('give a score between 0-10:'))

        while score < 0 or score > 10:
            score = float(input('Error:give a score between 0-10:'))

        total += score
        average = total/count
    return average

def stars():
    average = main()
    if average < 5:
        print(f'Your score of {average} gives you no stars'),
    elif average >= 9:
        print(f'Your score of {average} gives you *****')
    elif average >= 8 and average < 9:
        print(f'Your score of {average} gives you ****')
    elif average >= 7 and average < 8:
        print(f'Your score of {average} gives you ***')
    elif average >= 6 and average < 7:
        print(f'Your score of {average} gives you **')
    elif average >= 5 and average < 6:
        print(f'Your score of {average} gives you *')
    
stars()

