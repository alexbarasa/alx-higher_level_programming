#!/usr/bin/python3
def element_at(my_list, idx):

    if idx > len(my_list) - 1:
        return None
    elif idx < 0:
        return None
    else:
        print(my_list[idx])
