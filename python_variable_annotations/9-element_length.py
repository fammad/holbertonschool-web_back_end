#!/usr/bin/env python3
'''Variable Annotations'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''A  function that ititrate and calcualte of'''
    return [(i, len(i)) for i in lst]
