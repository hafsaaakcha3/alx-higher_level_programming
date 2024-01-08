#!/usr/bin/python3
"""add_attr"""


def add_attribute(obj, name, value):
    """add_attr"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
