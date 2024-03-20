#!/usr/bin/python3
def uniq_add(my_list=[]):

    if not my_list:
        return
    new = set(my_list)
    return sum(new)
