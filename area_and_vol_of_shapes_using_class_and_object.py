''' creating a import math'''
import math
class Shape:
    # """ Shape is the parent class"""
    # def area(self):
    #     """ to find the area"""
    #     pass
    # def volume(self):
    #     """ to find the volume"""
    #     pass
    # 
class Sphere(Shape):
    """ sphere is the inherited class of shape"""
    def __init__(self, radius_1):
        self.radius = radius_1
    def area(self):
        """ to find area of sphere"""
        return 4 * math.pi * self.radius ** 2
    def volume(self):
        """ to find volume of sphere"""
        return 4/3 * math.pi * self.radius ** 3
class Cube(Shape):
    """ cube is the iherited class of shape"""
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        """ to find area of cube"""
        return 6 * self.side_length ** 2
    def volume(self):
        """ to find volume of cube"""
        return self.side_length ** 3
class Cylinder(Shape):
    """ cylinder is the iherited class of shape"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def area(self):
        """ to find area of cylinder"""
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2
    def volume(self):
        """ to find volume of cylinder"""
        return math.pi * self.radius ** 2 * self.height
    while True:
        def menu(self):
            """ to show the options for selecting the shape"""
            options = '1. Sphere \n2. Cube \n3. Cylinder \n4. Exit'
            print(options)
        menu()
        choice = int(input('Please select one of the following : ')) 
        if choice == 1:
            sphere_input=int(input("enter the radius of sphere (in cm):- "))
            sphere = Sphere(sphere_input)
            """gave input to sphere"""
            print(f"Sphere area (in cm^2): {sphere.area()}")
            print(f"Sphere volume (in cm^3): {sphere.volume()}")
        elif choice == 2:
            cube_input=int(input("enter the side_length of cube (in cm):- "))
            cube = Cube(cube_input)
            """gave input to cube"""

            print(f"Cube area (in cm^2): {cube.area()}")
            print(f"Cube volume (in cm^3): {cube.volume()}")
        elif choice == 3:
            cylinder_radius=int(input("enter the radius of cylinder (in cm):- "))
            cylinder_height=int(input("enter the height of cylinder (in cm):- "))
            cylinder = Cylinder(cylinder_radius, cylinder_height)
            print(f"Cylinder area (in cm^2): {cylinder.area()}")
            print(f"Cylinder volume (in cm^3): {cylinder.volume()}")
        elif choice == 4:
            print("Thank You")
            break
        else:
            print("Invalid Input")
    print()
