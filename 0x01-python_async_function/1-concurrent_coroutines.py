#!/usr/bin/env python3
"""
Concurrent routine that spawns wait_random
n times with the specified max_delay
"""
import asyncio
from typing import List
from random import randint
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays
    sorted in ASC order as floats
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
