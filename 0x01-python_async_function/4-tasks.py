#!/usr/bin/env python3
"""
Function `task_wait_n` that is nearly identical
to `wait_n` and calls `task_wait_random`.
"""
import asyncio
from typing import List
from random import randint
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays
    sorted in ASC order as floats
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
