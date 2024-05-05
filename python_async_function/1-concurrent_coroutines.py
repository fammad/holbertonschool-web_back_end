#!/usr/bin/env python3
'''Async functions'''
from typing import List
import random
import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''random'''
    dictwait = []
    for i in range(n):
        dictwait.append(await wait_r(max_delay))
    return sorted(dictwait)
