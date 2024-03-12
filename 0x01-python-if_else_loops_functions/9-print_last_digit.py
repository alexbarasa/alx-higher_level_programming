#!/usr/bin/python3
def print_last_digit(number):
    remainder = abs(number) % 10
    if number < 0:
        return(-(remainder))
    else:
        return(remainder)
