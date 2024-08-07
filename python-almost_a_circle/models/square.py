#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square instance """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ Return the string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Update attributes """
        if args:
            attributes = ["id", "size", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif hasattr(self, key):
                    setattr(self, key, value)
