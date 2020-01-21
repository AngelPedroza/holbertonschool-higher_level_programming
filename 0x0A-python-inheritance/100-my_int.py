#!/usr/bin/python3
class MyInt(int):
    def __init__(self, value):
        self.var = value

    def __eq__(self, var):
        return self.var != int(var)

    def __ne__(self, var):
        return self.var == int(var)
