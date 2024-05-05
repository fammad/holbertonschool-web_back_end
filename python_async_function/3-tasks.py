#!/usr/bin/env python3
'''Async functions'''
import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Task wait Random'''
    return asyncio.create_task(wait_r(max_delay))
