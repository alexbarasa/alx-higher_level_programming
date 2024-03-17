#!/usr/bin/python3
def no_c(my_string):

    if not my_string:
        return ''
    else:
        c = ''
        for i in my_string:
            if i.lower() != 'c':
                c += i
    return c
