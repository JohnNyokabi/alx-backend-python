#!/usr/bin/env python3
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """zoom-in logic"""
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


"""change array from list to tuple"""
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
