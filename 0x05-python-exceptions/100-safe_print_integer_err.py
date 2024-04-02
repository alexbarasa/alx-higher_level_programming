#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        # Attempt to convert the value to an integer
        integer_value = int(value)
        # Print the integer value followed by a newline
        print("{:d}".format(integer_value))
        return (True)
    except ValueError:
        # If conversion fails, print an error message to stderr
        print("Exception: ValueError occurred: Unknown format code 'd' for object of type '{}'".format(type(value).__name__), file=sys.stderr)
        # print(f"Exception: Unknown format code {value} for object of type 'str'", file=sys.stderr)
        return (False)
    except Exception as e:
        # If any other exception occurs, print an error message to stderr
        print("Exception:", e, file=sys.stderr)
        return (False)
