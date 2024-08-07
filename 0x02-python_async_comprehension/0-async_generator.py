#!/usr/bin/env python3
"""provides the function async_generator"""
import asyncio
import random


async def async_generator():
    """coroutine: async_generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
