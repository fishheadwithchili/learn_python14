"""Annotated to attach metadata (PEP 593).

Run with Python >=3.9
"""

from typing import Annotated


PositiveInt = Annotated[int, "positive"]


def set_workers(n: PositiveInt) -> None:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be positive int")
    print(f"workers set to {n}")


set_workers(4)


