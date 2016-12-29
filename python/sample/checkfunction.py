import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


maximum = max(1,2,3,4,5)
print maximum

minimum = min(1,2,3,4,5)
print minimum


absolute = abs(-42)
print absolute


print type(4)
print type(4.4)
print type("hello")