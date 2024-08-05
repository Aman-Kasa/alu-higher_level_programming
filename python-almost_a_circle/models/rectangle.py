from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)
        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_csv_list(self):
        """Return the Rectangle attributes as a list for CSV serialization."""
        return [self.id, self.width, self.height, self.x, self.y]
