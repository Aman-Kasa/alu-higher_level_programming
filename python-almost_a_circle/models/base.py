#!/usr/bin/python3
""" Module that contains the Base class """
import json


class Base:
    """ Base class for other classes """
    def __init__(self, id=None):
        """ Initializes the Base class """
        self.id = id  # Ensure id is set here

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
