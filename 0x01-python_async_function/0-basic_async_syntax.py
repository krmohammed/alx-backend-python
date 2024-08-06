#!/usr/bin/env python3
""" provides the wait_random functon """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in max_delay, with a default value of 10
    then waits for a random delay between 0 and max_delay

    Args:
        max_delay: maximum sleep time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
