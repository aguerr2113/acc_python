# Artemio Guerrero,
# complete,
# Person 1 –write the main function which will:
# 1. Generate a random integer between 1 and 100 which will be the
# side of the square
# 2. Pass that number to called functions called square_area and
# square_perimeter.
# 3. Display the side, the returned area, and the returned perimeter
import random
from square import square_area,square_perimeter
# 1. Generate a random integer between 1 and 100 which will be the
# side of the square

def main():
    square_side = random.randint(1,100)
    return square_side

side = main()

square_area(side)
square_perimeter(side)
