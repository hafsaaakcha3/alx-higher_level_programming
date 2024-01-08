#!/usr/bin/python3
"""import Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle child class"""


class Rectangle(BaseGeometry):
    """Rectangle child class"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
