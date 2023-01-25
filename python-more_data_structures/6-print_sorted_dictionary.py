#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

  sorted_keys = list(a_dictionary)
  sorted_keys.sort()
  sorted_dic = {i: a_dictionary[i] for i in sorted_keys}

  print(sorted_dic)
