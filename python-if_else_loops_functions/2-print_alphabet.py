#!/usr/bin/python3
import string

for letter in string.ascii_lowercase:
    letter.replace("e", "q")
    print("{}".format(letter), end="")
