#!/usr/bin/python3
""" Module containing the Base class """
import json


class Base:
    """ Base class for all other classes """
    def __init__(self, id=None):
        """ Initialize the Base class with an id """
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to a JSON string """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
