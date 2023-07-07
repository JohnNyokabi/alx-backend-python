#!/usr/bin/env python3
"""Annotating function parameters"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
