#!/usr/bin/python3
"""import base class"""


from models.base import Base


"""Rectangle child class"""


class Rectangle(Base):
    """Rectangle child class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle attr"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """property setter width"""
        self.__width = value
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """property height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """property setter height"""
        self.__height = value
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """property x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """property setter x"""
        self.__x = value
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """property y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """property setter y"""
        self.__y = value
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calculate and return rectangle area method"""
        return (self.height * self.width)

    def display(self):
        """Display rectangle if width and height are greater than 0"""
        if self.height == 0 or self.width == 0:
            print("")
        else:
            for i in range(self.y):
                print()
            for i in range(self.height):
                print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """update rectangle class"""
        if args:
            if (len(args)) >= 1:
                self.id = args[0]
            if (len(args)) >= 2:
                self.width = args[1]
            if (len(args)) >= 3:
                self.height = args[2]
            if (len(args)) >= 4:
                self.x = args[3]
            if (len(args)) >= 5:
                self.y = args[4]
        elif kwargs:
            the_keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in kwargs.items():
                if key in the_keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width})
