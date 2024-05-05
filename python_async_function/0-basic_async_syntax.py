#!/usr/bin/env python3
'''Async'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """The basics of async"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
