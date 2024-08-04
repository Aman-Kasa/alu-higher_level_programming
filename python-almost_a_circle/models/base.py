#!/usr/bin/python3
"""Base module"""
import csv
import os


class Base:
    """Base class with id management and CSV methods"""
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
        """Serialize list of objects to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if isinstance(obj, cls):
                    writer.writerow(cls.to_csv_list(obj))

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        if not os.path.isfile(filename):
            return []
        
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            objs = []
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    obj = cls(*map(int, row))
                elif cls.__name__ == 'Square':
                    obj = cls(*map(int, row))
                objs.append(obj)
        return objs

    @staticmethod
    def to_csv_list(obj):
        """Convert an object to a CSV list (to be implemented by subclasses)"""
        raise NotImplementedError("Subclasses must implement this method")
