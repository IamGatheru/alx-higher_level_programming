#!/usr/bin/python3
def only_diff_elements(set1, set2):
    """Returns a set of all elements present in only one set."""
    set3 = set1.difference(set2)
    set4 = set2.difference(set1)
    od_set = set3.union(set4)
    return (od_set)
