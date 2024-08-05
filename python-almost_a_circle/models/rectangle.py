#!/usr/bin/python3
"""Module defining a Rectangle class"""


class Rectangle:
    """Class representing a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rect] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Update the Rectangle instance  arguments and/or  arguments"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
