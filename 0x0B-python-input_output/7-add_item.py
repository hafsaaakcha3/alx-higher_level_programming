#!/usr/bin/python3
"""save to json"""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
file = "add_item.json"

if os.path.exists(file):
    plist = load_from_json_file(file)
else:
    plist = []

plist += args

save_to_json_file(plist, file)
