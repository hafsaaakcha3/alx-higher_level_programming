#!/usr/bin/python3
"""MyIint class"""


class MyInt(int):
    """MyInt"""
    def __eq__(self, other):
        """eq methode Override the == operator to invert its behavior"""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """ne methode Override the != operator to invert its behavior"""
        return (not super().__ne__(other))
