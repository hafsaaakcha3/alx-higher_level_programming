#!/usr/bin/python3
"""from json to string"""


import json


def from_json_string(my_str):
    """from json to string"""
    j_string = json.loads(my_str)
    return (j_string)
