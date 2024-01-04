#!/usr/bin/python3
"""Define a class named Rectangle to represent a rectangle."""


class Rectangle:
    """Constructor method to initialize a Rectangle object."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle width the given width."""
        self.width = width
        self.height = height

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
        if value < 0:
            raise ValueError("width must be >= 0")

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
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Calculate and return the area of the rectangle."""
        area = self.width * self.height
        return (area)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.height == 0 or self.width == 0:
            perimeter = 0
        else:
            perimeter = self.width * 2 + self.height * 2
        return (perimeter)

    def __str__(self):
        rectangle_str = ""
        if self.height == 0 or self.width == 0:
            return ("")
        for idx in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return (rectangle_str.rstrip("\n"))
