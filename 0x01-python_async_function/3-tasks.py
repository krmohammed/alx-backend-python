#!/usr/bin/env python3
""" provides the function task_wait_random """
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    """
    return asyncio.ensure_future(wait_random(max_delay))
