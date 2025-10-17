"""Variadic generics with TypeVarTuple and Unpack (PEP 646).

Run with Python >=3.11
"""

from typing import TypeVarTuple, Unpack


Ts = TypeVarTuple("Ts")


def row(*values: Unpack[tuple[*Ts]]) -> tuple[*Ts]:
    return values  # runtime: just returns tuple; type checkers keep shape


print(row(1, "x", 2.0))


