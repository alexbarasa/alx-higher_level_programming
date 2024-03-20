#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    keys_sorted = sorted(a_dictionary.keys())
    for i in keys_sorted:
        print("{}: {}".format(i, a_dictionary[i]))
