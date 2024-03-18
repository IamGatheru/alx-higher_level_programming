#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b_list = []
    if len(my_list) != 0:
        for num in my_list:
            if num % 2 == 0:
                b_list.append(True)
            else:
                b_list.append(False)
        return b_list
