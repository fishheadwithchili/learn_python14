"""Use typing.Self for fluent APIs (PEP 673).

Run with Python >=3.11
"""

from typing import Self


class QueryBuilder:
    def __init__(self) -> None:
        self._parts: list[str] = []

    def where(self, condition: str) -> Self:
        self._parts.append(f"WHERE {condition}")
        return self

    def limit(self, n: int) -> Self:
        self._parts.append(f"LIMIT {n}")
        return self

    def build(self) -> str:
        return " ".join(self._parts) or "SELECT *"


sql = QueryBuilder().where("age > 18").limit(10).build()
print(sql)


