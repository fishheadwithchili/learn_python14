"""Use ParamSpec to preserve wrapped function parameter types.

Run with Python >=3.10
"""

from typing import Callable, ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def with_logging(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@with_logging
def power(base: float, exponent: float = 2.0) -> float:
    return base ** exponent


print(power(3))
print(power(2, exponent=3))


