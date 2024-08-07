#!/usr/bin/python3
""" Module that contains the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """ Returns a dictionary representation of the Square """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
