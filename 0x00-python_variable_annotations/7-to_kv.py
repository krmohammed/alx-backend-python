#!/usr/bin/env python3
"""provides the function to_kv"""
from typing import Tuple, Union


# that takes a string k and an int OR float v
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv function """
    return (k, v ** 2)
