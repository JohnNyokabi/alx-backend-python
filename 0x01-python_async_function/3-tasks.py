#!/usr/bin/env python3
"""
Function `task_wait_random` that takes an integer `max_delay`
"""
import asyncio
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """And returns a `asyncio.Task` type"""
    return asyncio.create_task(wait_random(max_delay))
