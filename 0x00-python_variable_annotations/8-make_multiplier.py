#!/usr/bin/env python3
"""provides the function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier function """
    def multiplier_func(val: float) -> float:
        """multiplier function"""
        return float(val * multiplier)
    return multiplier_func
