# models/square.py

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square attributes"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
