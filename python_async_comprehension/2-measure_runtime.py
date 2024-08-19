#!/usr/bin/env python3

"""Measure the runtime of async_comprehension"""

from typing import List
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    task = [async_comprehension() for _ in range(4)]
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*task)
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
