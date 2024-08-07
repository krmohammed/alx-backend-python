#!/usr/bin/env python3
"""provides the measure_time function"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    initial = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    now = time.perf_counter() - initial
    return float(now / n)
