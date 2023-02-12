#!/usr/bin/python3
"""
THis module reads argumends and appends them to a list in json format
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv
filename = 'add_items.json'

"""module is documented"""
with open(filename, "a+", encoding="utf-8") as f:
    """append arguments to a list"""
    my_list = []
    for i in len(arguments):
        my_list.extend(arguments[i])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
