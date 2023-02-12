#!/usr/bin/python3
"""comment"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv
filename = 'add_item.json'
my_list = []

try:
    my = load_from_json_file(filename)
except:
    pass
for i in arguments[1:]:
    my_list.append(i)
save_to_json_file(my_list, filename)
