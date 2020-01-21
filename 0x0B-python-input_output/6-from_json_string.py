#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Transform json to python object"""
    return json.loads(my_str)
