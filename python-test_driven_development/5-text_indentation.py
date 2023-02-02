#!/usr/bin/python3


def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in text:
        if i == "." or i == "?" or i == ":":
            print(f"{i}", end="")
            print("")
            print("")
        else:
            print(f"{i}", end="")
