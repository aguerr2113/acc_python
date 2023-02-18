# In Python, write a program to generate a random floating point number between 1
# and 100 which will be used as the radius of a circle. In a separate function, calculate
# the area of a circle based on the radius your program just generated and return it to
# the main function. In the main function, display the radius and the area.
import random
import math
# generate a random floating point number between 1
# and 100 which will be used as the radius of a circle. 
def rand_circ():
    radius = random.randint(1,100)

    return radius
radius2 = rand_circ()
squared = radius2**2

this_pi = math.pi
def area():
    print(f'the radius of the circle is:{radius2}')
    area_1 = this_pi*squared
    print(f'the area of the circle is:{area_1}')
area()