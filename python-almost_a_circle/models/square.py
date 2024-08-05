#!/usr/bin/python3
"""Module defining a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        ))

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.width,  # Square uses width for size
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Update the Square instance with argumentrguments"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                if attr == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                elif hasattr(self, key):
                    setattr(self, key, value)
