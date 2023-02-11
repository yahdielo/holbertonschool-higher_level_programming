#!/usr/bin/python3
"""comment"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv
filename = 'add_items.json'

with open(filename, "a+", encoding="utf-8") as f:
    my_list = []
    my_list.append(arguments[1])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
