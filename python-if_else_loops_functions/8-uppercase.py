#!/usr/bin/python3


def uppercase(str):

    for i in str:
        character = ord(i)

        if character >= 97 and character <= 122:
            character = character - 32
            char = chr(character)

        else:
            char = chr(character)
        print("{}".format(char), end="")

    print("")
