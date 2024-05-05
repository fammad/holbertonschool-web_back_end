#!/usr/bin/env python3
"""Async function called"""
import asyncio
from typing import List
wait_r = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Task wait n'''
    dictwait = []
    for i in range(n):
        dictwait.append(await wait_r(max_delay))
    return sorted(dictwait)
