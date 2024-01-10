#!/usr/bin/python3
"""save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        j_string = json.dumps(my_obj)
        return (f.write(j_string))
