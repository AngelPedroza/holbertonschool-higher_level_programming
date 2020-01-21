#!/usr/bin/python3
class Student:
    """The class for a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        dicty = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    for h in self.__dict__:
                        if i == h:
                            dicty[i] = self.__dict__[h]
                else:
                    return self.__dict__
            return dicty
        else:
            return self.__dict__
