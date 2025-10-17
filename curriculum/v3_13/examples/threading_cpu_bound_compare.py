"""Compare scaling of CPU-bound threads under regular vs. free-threaded builds.

Run with Python >=3.13 (free-threaded build optional)
"""

import math
import time
from concurrent.futures import ThreadPoolExecutor


def work(n: int) -> int:
    s = 0
    for i in range(1, n):
        s += int(math.sqrt(i))
    return s


def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    r = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return r, t1 - t0


def run_threads(work_items: int, reps: int, threads: int) -> float:
    with ThreadPoolExecutor(max_workers=threads) as ex:
        _, dur = timed(list, ex.map(work, [work_items] * reps))
    return dur


for threads in (1, 2, 4, 8):
    duration = run_threads(work_items=80_000, reps=threads, threads=threads)
    print(f"threads={threads} duration={duration:.3f}s")


