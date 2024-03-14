#!/usr/bin/python3
import sys

if __name__ == "__manin__":
    arg = sys.argv[1:]
    if len(arg) == 1:
        print("{} argument".format(len(arg)))
    else:
        print("{} arguments".format(len(arg)))
    for i, j in enumerate(arg):
        print("{}{} {}".format(i + 1, ':', j))
