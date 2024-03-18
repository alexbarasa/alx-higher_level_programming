#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None
    l_max = my_list[0]
    for i in my_list:
        if i > l_max:
            l_max = i
    return l_max
