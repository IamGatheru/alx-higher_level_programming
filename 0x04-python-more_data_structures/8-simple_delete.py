#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    new_dict = a_dictionary.pop(key)
    return (new_dict)
