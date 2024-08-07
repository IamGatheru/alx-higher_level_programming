#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2 != 0:
        char = chr(char - 32)
    else:
        char = chr(char)
    print("{}".format(char[-1]), end='')
