#!/usr/bin/python3
"""
Module models.base
Contains a class Base with methods for serialization and deserialization.
"""

import csv
import json
import os


class Base:
    """
    Base class for all other classes in this project.
    Handles id attribute and provides JSON and CSV serializaon/deserializn.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list_objs to a JSON file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to a CSV file.

        Args:
            list_objs (list): List of instances to serialize.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                writer.writerow(obj.to_csv_list())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize a list of objects from a CSV file.

        Returns:
            list: List of deserialized instances.
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            list_objs = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(1, 1)
                elif cls.__name__ == "Square":
                    obj = cls(1)
                obj.update(*[int(val) for val in row])
                list_objs.append(obj)
        return list_objs
