"""Structured concurrency with asyncio.TaskGroup and except*.

Run with Python >=3.11
"""

import asyncio


async def ok_task():
    await asyncio.sleep(0.1)
    return "ok"


async def failing_task():
    await asyncio.sleep(0.05)
    raise ValueError("boom")


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(ok_task())
            tg.create_task(failing_task())
    except* ValueError as eg:
        print("caught ValueError group:", eg)


asyncio.run(main())


