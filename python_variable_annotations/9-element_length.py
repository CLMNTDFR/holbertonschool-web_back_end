#!/usr/bin/env python3

"""
type-annotated function element_length that takes a list L of strings as
argument and returns a list of tuples where each tuple’s first element is
the string from L and the second element is the length of the string.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """Return a list of tuples where each tuple’s first element is string"""
    return [(i, len(i)) for i in lst]
