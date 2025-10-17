"""Demonstrate union types with X | Y (PEP 604).

Run with Python >=3.10
"""

def stringify(value: int | float | str) -> str:
    if isinstance(value, (int, float)):
        return f"number:{value}"
    return f"text:{value}"


print(stringify(1))
print(stringify(3.14))
print(stringify("hello"))


