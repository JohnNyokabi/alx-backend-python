#!/usr/bin/env python3
"""Annotating function parameters"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
