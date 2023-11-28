#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
