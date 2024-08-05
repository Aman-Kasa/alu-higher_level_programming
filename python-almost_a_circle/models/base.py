import csv

class Base:
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of instances to a CSV file."""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                writer.writerow(obj.to_csv_list())  # Ensure this method is defined in your subclasses

    @classmethod
    def load_from_file_csv(cls):
        """Read a list of instances from a CSV file."""
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                list_objs = []
                for row in reader:
                    dictionary = cls.from_csv_list(row)  # Ensure this method is defined in your subclasses
                    obj = cls.create(**dictionary)
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []
