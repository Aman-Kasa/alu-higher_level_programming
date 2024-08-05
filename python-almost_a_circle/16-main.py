#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle
from models.base import Base


if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Base.to_json_string(list_input)  # Use Base class here
    list_output = Base.from_json_string(json_list_input)  # Use Base class here
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
