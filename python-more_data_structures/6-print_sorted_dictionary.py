#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

  sorted_keys = list(a_dictionary)
  sorted_keys.sort()
  for i in sorted_keys:
    print("{}: {}".format(i, a_dictionary.get(i)))
