#!/usr/bin/env python3
"""Duck-typed annotations"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """annotations logic"""
    if lst:
        return lst[0]
    else:
        return None
