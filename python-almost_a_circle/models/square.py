#!/usr/bin/python3
"""Module that defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        ))

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square instance."""
        if args and len(args) > 0:
            attr_names = ['id', 'size', 'x', 'y']
            for attr, val in zip(attr_names, args):
                setattr(self, attr, val)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
