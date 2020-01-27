#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """This class is inheritante of Base clase"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

        super().__init__(id)

    def __str__(self):
        """Show all attributes of a instance in a string"""
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    # Methods for set and get values
    @property
    def width(self):
        """Give the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a value of width private attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Give the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a value of height private attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Give the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set a value of x private attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Give the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set a value of y private attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    # Final of the set and get methods

    # Manage methods
    def area(self):
        """This method give the area"""
        return self.__width * self.__height

    def display(self):
        """This method show a rectangle"""
        a = ""
        a += '\n' * self.__y
        for i in range(self.__height):
            a += ' ' * self.__x + '#' * self.__width + '\n'
        print(a, end="")

    def update(self, *args, **kwargs):
        """Organice each element of args and check him order"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in attr_list:
                    if i == key:
                        setattr(self, i, value)
        # setattr call the setter method

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        attr_list = ["id", "width", "height", "x", "y"]
        newD = {}

        for i in attr_list:
            newD[i] = getattr(self, i)
        return newD
