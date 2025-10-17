"""PEP 692: TypedDict for **kwargs to specify accepted keys.

Run with Python >=3.12
"""

from typing import TypedDict


class Opts(TypedDict, total=False):
    timeout: float
    retries: int


def connect(**opts: Opts) -> None:
    print("connecting with:", opts)


connect(timeout=1.0)
connect(timeout=1.0, retries=3)


