#!/usr/bin/env python3
"""provides the function async_generator"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """coroutine: async_generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
