#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list."""
    set_sum = sum(set(my_list))
    return set_sum
