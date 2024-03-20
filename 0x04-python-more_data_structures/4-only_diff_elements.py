#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    if not (set_1 or set_2):
        return None
    diff = set_1.symmetric_difference(set_2)
    return diff
