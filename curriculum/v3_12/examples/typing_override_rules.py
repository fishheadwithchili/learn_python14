"""PEP 698: typing.override to mark intentional override sites.

Run with Python >=3.12
"""

from typing import override


class Base:
    def close(self) -> None:
        print("Base.close")


class Child(Base):
    @override
    def close(self) -> None:
        print("Child.close")


Child().close()


