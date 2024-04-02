#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        for i in my_list[:x]:
            print(i, end='')
        print()
        count = 0
        for i in my_list:
            count += 1
        if x <= count:
            return (x)
        else:
            return (count)
    except IndexError:
        print("Error occurred")
    #return (count)
