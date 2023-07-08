#!/usr/bin/env python3
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """zoom-in logic"""
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


"""change array from list to tuple"""
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)