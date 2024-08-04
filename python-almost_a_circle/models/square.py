#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size attribute with validation"""
        self.width = value
        self.height = value

    @staticmethod
    def to_csv_list(obj):
        """Convert a Square object to a CSV list"""
        return [obj.id, obj.size, obj.x, obj.y]
