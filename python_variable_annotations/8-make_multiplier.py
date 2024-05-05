#!/usr/bin/env python3
'''Variable Annotations'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Main Function'''
    def func(n: float) -> float:
        '''Return n with multification of multiplier'''
        return n * multiplier
    return func
