#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

def main():
    # Case: bg = BaseGeometry() print(dir(bg))
    bg = BaseGeometry()
    print(dir(bg))

    # Case: bg = BaseGeometry() bg.integer_validator("myint", 12)
    bg.integer_validator("myint", 12)

    # Case: bg = BaseGeometry() bg.integer_validator("myint", 12) bg.integer_validator("width", 89)
    bg.integer_validator("myint", 12)
    bg.integer_validator("width", 89)

    # Case: bg = BaseGeometry() bg.integer_validator("name", "John")
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    # Case: bg = BaseGeometry() bg.integer_validator("age", 0)
    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    # Case: bg = BaseGeometry() bg.integer_validator("age", -4)
    try:
        bg.integer_validator("age", -4)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    # Case: bg = BaseGeometry() bg.integer_validator("age", 13.5)
    try:
        bg.integer_validator("age", 13.5)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    # Case: bg = BaseGeometry() bg.area()
    try:
        bg.area()
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

if __name__ == "__main__":
    main()
