#!/usr/bin/python3
class BaseGeometry:
    """Know the area of a geometry shape"""

    def area(self):
        """Give the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Vlaidate if value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
