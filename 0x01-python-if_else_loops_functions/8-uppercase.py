#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(chr(ord(char.upper())), end="")
    print()
