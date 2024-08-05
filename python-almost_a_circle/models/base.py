#!/usr/bin/python3
"""
This module contains the Base class.
"""


class Base:
    """
    The Base class for all other classes in this project.
    Manages the id attribute to avoid code duplication.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        If id is provided, use it as the instance id.
        Otherwise, increment the number of objects and assign a new id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
