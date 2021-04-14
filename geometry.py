import math
from math import sqrt

def geometry (length, width, height):
    if (length == width == height):
        shape = "cube"
        sides = length
        D = sqrt(3 * (sides ** 2))
        R = D/2
        r = sides/2
        
    else:
        if (length == width or width == height or length == height):
            shape = "isosceles cuboid"
            ratio = length/width if length == height else length/height
            ratio_standard = ratio if ratio > 1 else 1/ratio
            no_of_cubes = math.floor(ratio_standard)
            side_of_cube = height if length != width else length
        else:
            shape = "regular cuboid"
        sides = [length, width, height]
        sides.sort()
        D = sqrt((sides[-2] ** 2) + (sides[-1] ** 2) + (sides[0] ** 2))
        R = D/2
        r = sides[0]/2
        
    volume = length * width * height
    surface_area = 2 * (length * (width + height) + (width * height))
    vol_in = 4/3 * math.pi * (r ** 3)
    vol_circum = 4/3 * math.pi * (R ** 3)
    print("This is a " + shape + " of side " + str(sides) + ".")
    print("The volume of the " + shape + " is " + str(volume) + ".")
    print("The surface area of the " + shape + " is " + str(surface_area) + ".")
    print("The diameter of the circumscribed sphere is " + str(D))
    print("The volume of the circumscribed sphere is " + str(vol_circum) + ".")
    print("The diameter of the inscribed sphere is " + str(2 * r))
    print("The volume of the inscribed sphere is " + str(vol_in) + ".")
    if (shape == "isosceles cuboid"):
        print("A total of " + str(no_of_cubes) + " cubes of sides " 
              + str(side_of_cube) + " can be fit into this " + shape)
    
a = input("Please enter the length:")
length = int(a)
b = input("Please enter the width:")
width = int(b)
c = input("Please enter the height:")
height = int(c)
geometry(length, width, height)
    
        
