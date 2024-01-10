#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json method"""
        res = {}
        key = 0
        if attrs is None:
            return (vars(self))
        else:
            for key in attrs:
                if hasattr(self, key):
                    res[key] = getattr(self, key)
            return (res)

    def reload_from_json(self, json):
        """reload from json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
