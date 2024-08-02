#!/usr/bin/env python3
"""provides safely_get_value function """
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default:Union[TypeVar, None]=None) -> Union[Any, TypeVar]:
    """ safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
