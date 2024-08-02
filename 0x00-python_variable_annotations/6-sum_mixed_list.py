#!/usr/bin/env python3
"""provides the function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums a mixed list """
    return sum(mxd_lst)
