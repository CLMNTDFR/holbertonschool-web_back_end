#!/usr/bin/env python3

"""function that measures the total execution time for wait_n(n, max_delay)"""

import asyncio
import random
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time for wait_n(n, max_delay)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
