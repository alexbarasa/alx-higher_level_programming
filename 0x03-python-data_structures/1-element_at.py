#!/usr/bin/python3
def element_at(my_list, idx):

    if idx >= len(my_list):
        return
    elif idx < 0:
        return
    else:
        print(my_list[idx])
