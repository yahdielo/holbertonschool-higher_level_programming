#!/usr/bin/python3
"""comment"""
import json

def save_to_json_file(my_obj, filename):
    """comment"""
    with open(filename, "w", encoding="utf-8") as f:
        myjson_string = json.dumps(my_obj)
        return f.write(myjson_string)
