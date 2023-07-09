#!/usr/bin/env python3
"""add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Fetches value from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
