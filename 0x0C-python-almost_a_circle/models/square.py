#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """This subclass manage a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the info about the object"""
        return "[{}] ({}) {}/{} - {}".format(__class__.__name__, self.id,
                                             self.x, self.y, self.width)

    # Setter and Getter methods
    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value from width and height"""
        self.width = value
        self.height = value

    # Public methods
    def update(self, *args, **kwargs):
        """Organice each element of args and check him order"""
        attr_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in attr_list:
                    if i == key:
                        setattr(self, i, value)
                    if key == "size":
                        setattr(self, "width", value)
                        setattr(self, "heigth", value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        attr_list = ["id", "size", "x", "y"]
        newD = {}

        for i in attr_list:
            newD[i] = getattr(self, i)
        return newD
