#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers
using async comprehension over async generator
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Returns the 10 random numbers"""
    return [i async for i in async_generator()]
