#!/usr/bin/python3
"""comment"""
import json


def load_from_json_file(filename):
    """comment"""
    with open(filename, "r+", encoding="utf-8") as f:
        _obj = f.read()
        return json.loads(_obj)
