# In models/square.py
class Square(Rectangle):  # Assuming Square inherits Rectangle
    def to_csv_list(self):
        return [self.id, self.size, self.x, self.y]

    @staticmethod
    def from_csv_list(csv_list):
        return {
            'id': int(csv_list[0]),
            'size': int(csv_list[1]),
            'x': int(csv_list[2]),
            'y': int(csv_list[3])
        }
