from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)  # Initialize the Rectangle with size for both width and height
        self.size = size

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @staticmethod
    def create(**dictionary):
        dummy = Square(1)
        dummy.update(**dictionary)
        return dummy
