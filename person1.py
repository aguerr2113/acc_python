# Artemio Guerrero
import random
import squares
#Generate a random integer between 1 and 100 which will be the
#side of the square

def main():
#2. Pass that number to called functions called square_area and
#square_perimeter.
#3. Display the side, the returned area, and the returned perimeter
    side = random.randint(1,100)
    print(f'side = {side}')
    print(f'area = {squares.square_area(side)}')
    print(f'perimeter = {squares.square_perimeter(side)}')
main()
