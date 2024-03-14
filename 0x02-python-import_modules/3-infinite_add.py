#!/usr/bin/python3
import sys


def add_args():

    total = 0
    args = sys.argv[1:]
    for i in args:
        total += int(i)
    print(total)


if __name__ == "__main__":

    add_args()
