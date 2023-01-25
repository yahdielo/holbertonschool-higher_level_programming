#!/usr/bin/python3


def search_replace(my_list, search, replace):

    _list = list(my_list)

    for i in range(len(my_list)):
        print(i)
        if my_list[i] is search:
            _list[i] = replace
    return _list
