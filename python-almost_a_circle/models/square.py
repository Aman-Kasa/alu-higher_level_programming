# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of a Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance."""
        attributes = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attributes):
                if attributes[i] == "size":
                    self.width = self.height = arg
                else:
                    setattr(self, attributes[i], arg)
        for key, value in kwargs.items():
            if key == "size":
                self.width = self.height = value
            elif key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square instance."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def to_csv_list(self):
        """Return the Square attributes as a list for CSV serialization."""
        return [self.id, self.width, self.x, self.y]
