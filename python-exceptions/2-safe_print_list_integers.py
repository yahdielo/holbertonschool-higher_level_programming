#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is not int:
                continue
            else:
                count += 1
                print("{}".format(my_list[i]), end="")
        print()
        return count
    except ValueError:
        count = 0
        for i in my_list:
            count += 1
            if count == x:
                break
            else:
                print()
                return