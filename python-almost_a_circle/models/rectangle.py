from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the Base constructor without parameters if Base doesn't require them
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @staticmethod
    def create(**dictionary):
        dummy = Rectangle(1, 1)
        dummy.update(**dictionary)
        return dummy
