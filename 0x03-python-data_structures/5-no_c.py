#!/usr/bin/python
def no_c(my_string):

    if not my_string:
        return
    s = "AlexbarasaNyongesa"
    c = ''
    for i in s:
        if i in 'Aa':
            pass
        else:
            c += i
    return c
