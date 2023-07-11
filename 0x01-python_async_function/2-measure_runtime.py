#!/usr/bin/env python3
"""
Function measure_time  with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay) function
"""
import asyncio
import time
from random import uniform
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the total runtime/n as float"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
