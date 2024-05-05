#!/usr/bin/env python3
'''Variable Annotation'''
from typing import List, Union


def  sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''takes a list mxd_lst returns their sum'''
    return sum(mxd_lst)
