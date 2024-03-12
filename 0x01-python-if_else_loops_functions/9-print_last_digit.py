#!/usr/bin/python3
def print_last_digit(number):

    remainder = abs(number) % 10
    print("{}".format(remainder),end='')
    return(remainder)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
