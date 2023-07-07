#!/usr/bin/env python3
"""
Type-annotated function to_kv that takes a
string k and an int OR float v as arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes in a string and an int/float and returns a tuple"""
    return (k, v ** 2)
