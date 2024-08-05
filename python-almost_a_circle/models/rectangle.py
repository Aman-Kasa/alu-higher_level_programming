# models/rectangle.py


class Rectangle:
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        # Add validation and other initializations as needed

    # Add other methods and properties as needed

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """Update method to handle args and kwargs"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
