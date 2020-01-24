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
        return self.width

    @size.setter
    def size(self, value):
        super().width(value)
        self.width = value
        self.height = value
