#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if not my_list:
        return
    new_list = my_list[:]
    for in in new_list:
        if i == search:
            new_list[new_list.index(search)] = replace
    return new_list
