# Artemio Guerrero,
# complete,
# falling_distance – will be passed one parameter which is the time in seconds the object has been
# falling and will calculate and return the distance in meters. falling_distance should be stored in
# a separate file (module) called distance.py 

def falling_distance(time):
    t = time**2
    g = 9.8
    distance = .5 * g * time

    return distance