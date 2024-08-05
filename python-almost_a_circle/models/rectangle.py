# In models/rectangle.py
class Rectangle(Base):
    def to_csv_list(self):
        return [self.id, self.width, self.height, self.x, self.y]

    @staticmethod
    def from_csv_list(csv_list):
        return {
            'id': int(csv_list[0]),
            'width': int(csv_list[1]),
            'height': int(csv_list[2]),
            'x': int(csv_list[3]),
            'y': int(csv_list[4])
        }
