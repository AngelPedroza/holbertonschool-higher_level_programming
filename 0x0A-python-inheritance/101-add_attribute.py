#!/usr/bin/python3
def add_attribute(obj, key="", value=""):
        """Check if the attribute exist in the intance"""
        if not hasattr(obj, "__dict__"):
                raise TypeError("can't add new attribute")
        else:
                setattr(obj, key, value)
