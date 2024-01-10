#!/usr/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, 'a', encoding='UTF-8') as f:
        return (f.write(text))
