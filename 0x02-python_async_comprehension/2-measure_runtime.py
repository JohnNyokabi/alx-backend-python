#!/usr/bin/env python3
"""
Coroutine that executes `async_comprehension` 4 times
in a parallel using `asyncio.gather`
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime and returns it"""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()

    total_runtime = end_time - start_time
    return total_runtime
