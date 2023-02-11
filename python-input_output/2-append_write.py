#!/usr/bin/python3
"""comment"""


def append_write(filename="", text=""):
    """comment"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return  len(text)