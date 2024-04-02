#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    try:
        for i in my_list[:x]:
            try:
                print("{:d}".format(i), end='')
                count += 1
            except ValueError:
                pass
                # print("ValueError occured")
        print()
    except TypeError:
        print()
        # print("Error occured")
        return (count)
    return (count)
