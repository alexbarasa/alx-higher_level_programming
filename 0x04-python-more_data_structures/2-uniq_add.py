#!/usr/bin/python3
def uniq_add(my_list=[]):

    if not my_list:
        return
    new = set()
    for i in my_list:
        new.add(i)
    total = sum(new)
    return total
