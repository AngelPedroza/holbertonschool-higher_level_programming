#!/usr/bin/python3
class MagicClass:
    import math






    def __init__(self, radius=0):
        self.radius = 0
        if type(radius) is not int is not float:
            raise TypeError("radius must be a number")
        return self.radius = radius



    def area(self):
        return self.radius ** 2 * math.pi


    def circumference(self):
        return 2 * math.pi * self.raduis
