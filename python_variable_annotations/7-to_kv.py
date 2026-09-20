#!/usr/bin/env python3
"""
Complex types - tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a number."""
    return (k, v ** 2)
