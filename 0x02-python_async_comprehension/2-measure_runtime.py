#!/usr/bin/env python3
"""provides the function measure_runtime"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    runtime = time.perf_counter() - start_time
    return runtime
