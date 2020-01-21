#!/usr/bin/python3
import json


def class_to_json(obj):
    """Change all the attributes in JSON"""
    j_f = json.dumps(obj.__dict___)
    return json.loads(j_f)
