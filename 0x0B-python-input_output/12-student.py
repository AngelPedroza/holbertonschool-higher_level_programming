#!/usr/bin/python3
import json


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
                    json_format = json.dumps(self.__dict__)
                    return json.loads(json_format)
            j_f = json.dumps(dicty)
            return json.loads(j_f)
        else:
            json_format = json.dumps(self.__dict__)
            return json.loads(json_format)
