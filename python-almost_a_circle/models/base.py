#!/usr/bin/python3
"""Module defining a Base class"""

import json


class Base:
    """Base class for managing ID"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list of dict): List of dictionaries to convert

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation

        Args:
            json_string (str): JSON string to convert

        Returns:
            list: List represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list of Base instances): List of instances to convert

        Returns:
            None
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)
