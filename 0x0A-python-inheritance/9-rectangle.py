#!/usr/bin/python3
class BaseGeometry:
    """Know the area of a geometry shape"""
    def __init__(self):
        pass

    def area(self):
        """Give the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Vlaidate if value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Generate a rectangle"""

    def __init__(self, width, height):
        """Check if the values are positve integers"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a list"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                   self.__height)

    def area(self):
        """Give the area"""
        return (self.__width * self.__height)
