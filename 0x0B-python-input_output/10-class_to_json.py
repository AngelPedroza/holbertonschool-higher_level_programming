#!/usr/bin/python3
import json

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    """
    json_format = json.dumps(obj.__dict__)
    return json.loads(json_format)
