#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Transform a json of a file to a python object"""
    with open(filename, mode="r", encoding="utf-8") as fd:
        return json.loads(fd.readline())
