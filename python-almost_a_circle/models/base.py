import csv
import os


class Base:
    def __init__(self, id=None):
        self.id = id

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a list of objects to a CSV file."""
        if not list_objs:
            with open(f"{cls.__name__}.csv", "w", newline="") as csvfile:
                csv.writer(csvfile).writerow([])
            return

        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if isinstance(obj, Base):
                    # Import classes inside the method to av imports
                    from models.rectangle import Rectangle
                    from models.square import Square
                    if isinstance(obj, Rectangle):
                        writer.writerow([
                            obj.id, obj.width, obj.height, obj.x, obj.y
                        ])
                    elif isinstance(obj, Square):
                        writer.writerow([
                            obj.id, obj.size, obj.x, obj.y
                        ])

    @classmethod
    def load_from_file_csv(cls):
        """Reads from a CSV file and returns a list of objects."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row or any(not value.strip() for value in row):
                    continue  # Skip empty rows or rows with invalid data
                try:
                    if cls.__name__ == "Rectangle":
                        from models.rectangle import Rectangle
                        instances.append(Rectangle(
                            *map(int, row)
                        ))
                    elif cls.__name__ == "Square":
                        from models.square import Square
                        instances.append(Square(
                            *map(int, row)
                        ))
                except ValueError:
                    print(f"Skipping invalid row: {row}")
            return instances
