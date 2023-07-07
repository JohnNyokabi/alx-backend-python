#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats
"""
import math
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the mixed list as a float"""
    return (sum(mxd_lst))
