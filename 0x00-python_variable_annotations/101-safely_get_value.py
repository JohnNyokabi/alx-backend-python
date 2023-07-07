#!/usr/bin/env python3
"""add type annotations to the function"""
from typing import TypeVar, Dict, Optional

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
