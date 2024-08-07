#!/usr/bin/python3
""" Module that contains the class Square, inheriting from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a Square, inheriting from Rectangle """    
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size, updating width and height with validation """
        self.width = value
        self.height = value
