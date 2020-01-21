#!/usr/bin/python3
import json


def class_to_json(obj):
    """Change all the attributes in JSON"""
    return json.loads(json.dumps(obj.__dict___))
