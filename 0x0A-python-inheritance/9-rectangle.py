#!/usr/bin/python3
"""import Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle child class"""


class Rectangle(BaseGeometry):
    """Rectangle child class"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", height)

    def area(self):
        """area implemented"""
        res = self.__width * self.__height
        return (res)

    def __str__(self):
        """str"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
