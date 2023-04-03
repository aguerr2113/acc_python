# Artemio Guerrero,
# complete,
# d = .5gt^2
# d is distance in meters 
# g is 9.8
# t is amount of time in seconds the object has been falling
# program will calculate the distance in meters based on the object’s falling distance.
# main – will call the falling_distance function in a loop, passing it the values 1 – 10 as arguments
# (seconds the object has been falling). It will display the returned distance.
from distance import falling_distance


def main():

    print('Year    Falling Distance')
    print('------------------------')
    for i in range(0,10):
        i += 1
        fall = falling_distance(i)

        print(f'{i}\t{"%.2f"%fall}')
main()