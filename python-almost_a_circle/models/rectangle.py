#!/usr/bin/python3
""" Module that contains the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Class representing a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the Rectangle """
        super().__init__(id)  # Properly initialize the parent class
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
