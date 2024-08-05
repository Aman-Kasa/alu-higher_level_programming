import json
import os


class Base:
    """Base class for other classes"""
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as file:
            file.write(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set"""
        dummy = cls(1, 1)  # Adjust the dummy attributes as needed
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file"""
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        
        with open(filename, "r") as file:
            json_string = file.read()
        
        list_dictionaries = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dictionaries]
