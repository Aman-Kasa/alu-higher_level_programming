import csv
import os


class Base:
    """Base class for all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list of objects to a CSV file"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y]
                    )

    @classmethod
    def load_from_file_csv(cls):
        """Loads list of objects from a CSV file"""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            list_objs = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    id, width, height, x, y = map(int, row)
                    obj = cls(width, height, x, y, id)
                elif cls.__name__ == "Square":
                    id, size, x, y = map(int, row)
                    obj = cls(size, x, y, id)
                list_objs.append(obj)
            return list_objs
