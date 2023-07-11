#!/usr/bin/env python3
"""
Coroutine that loops 10 times asynchronously
waiting 1 second and yields a random number
between 0 and 10
"""
import asyncio
from random import uniform


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
