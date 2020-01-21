#!/usr/bin/python3

"""Script that create a json in a file from sys.argv[1:]"""

import sys
import json
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

my_list += sys.argv[1:]
save_to_json_file(my_list, "add_item.json")
