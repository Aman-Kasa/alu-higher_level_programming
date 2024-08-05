from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

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

    def to_csv_list(self):
        """Return the Square attributes as a list for CSV serialization."""
        return [self.id, self.width, self.x, self.y]
