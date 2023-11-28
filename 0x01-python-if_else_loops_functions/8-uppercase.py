#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for char in str:
        upper_char = char
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(upper_char), end="")
    print()

if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")
