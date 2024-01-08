#!/usr/bin/python3
"""is kind of class"""


def is_kind_of_class(obj, a_class):
    """is kind of class"""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
