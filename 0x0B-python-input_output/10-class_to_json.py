#!/usr/bin/python3
def class_to_json(obj):
    """Change all the attributes in JSON"""
    return obj.__dict__
