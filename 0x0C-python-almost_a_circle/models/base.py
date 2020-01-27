#!/usr/bin/python3
"""Module for base class"""
import json
import os
import csv


class Base:
    """This the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Transform to JSON format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        list_dicts = []
        if json_string is None or len(json_string) == 0:
            return list_dicts
        else:
            list_dicts = json.loads(json_string)
            return list_dicts

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        new_list = []

        stri = "{}.json".format(cls.__name__)
        with open(stri, mode="w", encoding="utf-8") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                for i in list_objs:
                    new_list += [i.to_dictionary()]
                list = cls.to_json_string(new_list)
                fd.write(list)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(5, 5)
        else:
            instance = cls(5)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        string = "{}.json".format(cls.__name__)
        if os.path.exists(string) is False:
            return []

        with open(string) as fd:
            str_list = fd.read()

        cls_list = cls.from_json_string(str_list)
        instances = []

        for i in cls_list:
            instances += [cls.create(**i)]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        name = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

        with open(name, mode="w", encoding="utf-8") as fd:
            writer = csv.DictWriter(fd, fieldnames=fieldnames)
            [writer.writerow(i.to_dictionary())for i in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """Read to csv file"""
        name = "{}.csv".format(cls.__name__)

        if os.path.exists(name):
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            if cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            with open(name, mode="r", encoding="utf-8", newline="") as fdcsv:
                reader = csv.DictReader(fdcsv, fieldnames=fieldnames)
                my_instance = []
                my_dict = {}

                for dicty in reader:
                    for i in dicty:
                        my_dict[i] = int(dicty[i])
                    my_instance.append(cls.create(**my_dict))
                return my_instance
