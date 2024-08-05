import csv
import json

class Base:
    """Base class for other models"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file"""
        filename = cls.__name__ + '.json'
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a JSON file"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to a CSV file"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                writer.writerow(obj.to_csv_list())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of instances from a CSV file"""
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                list_objs = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(*map(int, row))
                    elif cls.__name__ == 'Square':
                        obj = cls(*map(int, row))
                    list_objs.append(obj)
            return list_objs
        except FileNotFoundError:
            return []
