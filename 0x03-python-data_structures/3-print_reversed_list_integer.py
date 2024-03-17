#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    my_new_list = my_list[::-1]
    for i in my_new_list:
        print(str.format("{:d}", i))
    return
