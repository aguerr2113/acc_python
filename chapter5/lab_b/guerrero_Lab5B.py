# d = .5gt^2
# d is distance in meters 
# g is 9.8
# t is amount of time in seconds the object has been falling
from falling_distance import falling_distance

def main():
    print('Year    Falling Distance')
    print('------------------------')
    for i in range(0,10):
        i += 1
        fall = falling_distance(i)

        print(f'{i}\t{"%.2f"%fall}')
main()