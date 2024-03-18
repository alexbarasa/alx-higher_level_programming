#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if not my_list:
        return
    elif idx >= len(my_list) or idx < 0:
        return my_list
    else:
        return my_list.remove(my_list[idx])
