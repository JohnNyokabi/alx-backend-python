#!/usr/bin/env python3
"""Syntax for coroutine wait_random"""
import asyncio
import random


async def wait_random(max_delay=10):
    """async/await logic"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
