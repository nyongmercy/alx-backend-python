#!/usr/bin/env python3
"""Task 2. Measure the runtime
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time should measure the total execution time
        for wait_n(n, max_delay), and return total_time / n.
        Your function should return a float.
        """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
