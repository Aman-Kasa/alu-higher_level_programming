class Rectangle:
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_integer("width", value)
        self.__validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_integer("height", value)
        self.__validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_integer("y", value)
        self.__validate_non_negative("y", value)
        self.__y = value

    def __validate_integer(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def __validate_positive(self, name, value):
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __validate_non_negative(self, name, value):
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
