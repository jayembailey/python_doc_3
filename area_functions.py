def sqFoot():
    length = float(input('Length: '))
    width = float(input('Width: '))
    area = length * width
    print("Area: " + str(area) + " sq. ft.")


#C =  2 pi r
from math import pi

def circumference():
    r = float(input('what is the radius of your circle?'))
    c = 2 * pi * r
    print(f'Circumference: {c}')

