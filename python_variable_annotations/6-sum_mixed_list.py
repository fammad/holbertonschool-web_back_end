#!/usr/bin/env python3
'''Variable Annotation'''
from typing import List, Union


def  sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''takes a list mxd_lst of integers and floats and returns their sum as a floa'''
    return sum(mxd_lst)
