#!/usr/bin/env python3

"""Measure the runtime of async_comprehension"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    tasks = [async_comprehension() for _ in range(4)]
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
