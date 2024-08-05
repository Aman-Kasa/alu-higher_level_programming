#!/usr/bin/python3
"""Module defining the Base class."""


class Base:
    """Base class for managing id attributes in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): The ID of the instance. If None, assigns a new ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
