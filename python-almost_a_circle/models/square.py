#!/usr/bin/python3
""" Module that contains the class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a Square, inheriting from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size with validation """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the Square """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """ Updates the Square attributes """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
