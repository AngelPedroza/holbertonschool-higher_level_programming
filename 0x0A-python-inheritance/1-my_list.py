#!/usr/bin/python3
class MyList:
    """My class list"""
    def __init__(self):
        """Init a list for each instance"""
        self.a = []

    def __str__(self):
        """Return the list"""
        return str(list(self.a))

    def append(self, ap=[]):
        """This function add a new element in the final of the list"""
        self.a += [ap]

    def print_sorted(self):
        """This list return a sorted list"""
        print(sorted(self.a))
