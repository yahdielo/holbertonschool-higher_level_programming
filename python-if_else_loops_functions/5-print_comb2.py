#!/usr/bin/python3


for n in range (00, 100):
    if n < 99:
        if n < 10:
            i = 0
        else:
            i = ""
        print("{}{}, ".format(i, n), end="")
    else:
        print("{}".format(n))
