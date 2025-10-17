"""Typing example spanning Self and PEP 695 type parameters.

Run with Python >=3.12 for the type parameter syntax.
"""

from typing import Self


class Pipeline[T]:
    def __init__(self, data: list[T]) -> None:
        self.data = data

    def map(self, fn: callable[[T], T]) -> Self:
        self.data = [fn(x) for x in self.data]
        return self

    def collect(self) -> list[T]:
        return self.data


print(Pipeline([1, 2, 3]).map(lambda x: x + 1).collect())


