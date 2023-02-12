#!/usr/bin/python3
"""comment"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv
filename = 'add_items.json'
my_list = []

try:
    my_list = load_from_json_file(filename)
except:
    pass
for i in range(1, len(arguments)):
    my_list.append(arguments[i])
save_to_json_file(my_list, filename)
