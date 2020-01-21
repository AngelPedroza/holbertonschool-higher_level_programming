#!/usr/bin/python3
import json

class Student:
    """The class for a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        json_format = json.dumps(self.__dict__)
        return json.loads(json_format)
