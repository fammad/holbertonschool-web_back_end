#!/usr/bin/env python3
'''Variable Annotations'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''something with tuple'''
    return (k, v * v)
