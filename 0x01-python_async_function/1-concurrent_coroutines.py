#!/usr/bin/env python3
""" provides the routine wait_n """
from typing import List
import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function waits for n seconds
    then returns a list of n random integers in the range [0, max_delay]

    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay in seconds
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays