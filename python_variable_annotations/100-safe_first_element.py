#!/usr/bin/env python3
"""Safe the first element of the lst"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return position one in the lst"""
    if lst:
        return lst[0]
    else:
        return None
