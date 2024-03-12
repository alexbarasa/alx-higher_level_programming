#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - ord('a') + ord('A'))
        else:
            result += i
    print("{}".format(result))
