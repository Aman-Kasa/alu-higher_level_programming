#!/usr/bin/python3
"""
Base class for all models in the project.

This module contains the Base class which provides methods for saving
and loading objects from CSV files.
"""

import csv
import os


class Base:
    """
    Base class for all models.

    This class provides the base functionality for saving and loading
    objects to and from CSV files.
    """
    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): The ID of the instance.
        """
        self.id = id

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to serialize.
        """
        if not list_objs:
            with open(f"{cls.__name__}.csv", "w", newline="") as csvfile:
                csv.writer(csvfile).writerow([])
            return

        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if isinstance(obj, Base):
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
        """
        Deserializes objects from a CSV file.

        Returns:
            list: A list of deserialized objects.
        """
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
