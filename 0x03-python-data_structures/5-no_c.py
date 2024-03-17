#!/usr/bin/python
def no_c(my_string):

    if not my_string:
        return
    c = ''
    for i in my_string:
        if i in 'Cc':
            pass
        else:
            c += i
    return c
