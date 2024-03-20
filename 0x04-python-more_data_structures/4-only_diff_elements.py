#!/usr/bin/python3
def common_elements(set_1, set_2):

    if not (set_1 or set_2):
        return
    diff = set_1.symmetric_difference(set_2)
    return diff
