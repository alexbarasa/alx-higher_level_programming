#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if not (my_list or search or replace):
        return
    new_list = my_list[:]
    for i in new_list:
        if i == search:
            new_list[new_list.index(search)] = replace
    return new_list
