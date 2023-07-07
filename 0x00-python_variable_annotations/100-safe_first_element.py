#!/usr/bin/env python3
"""Duck-typed annotations"""
from typing import Any, Optional


def safe_first_element(lst: list) -> Optional[Any]:
    """annotations logic"""
    if lst:
        return lst[0]
    else:
        return None
