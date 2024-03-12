#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            upper = chr(ord(i) - ord('a') + ord('A'))
            print("{}".format(upper), end='')
        else:
            print("{}".format(i), end='')
