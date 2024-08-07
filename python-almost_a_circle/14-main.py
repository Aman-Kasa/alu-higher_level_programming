#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    s1 = Square(5, 3, 6)
    dictionary_r1 = r1.to_dictionary()
    dictionary_s1 = s1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary_r1, dictionary_s1])
    print(dictionary_r1)
    print(dictionary_s1)
    print(json_dictionary)
    print(type(json_dictionary))
