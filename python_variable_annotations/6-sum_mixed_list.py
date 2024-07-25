#!/usr/bin/env python3

"""
type-annotated function sum_mixed_list that takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of a list of integers and floats"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
