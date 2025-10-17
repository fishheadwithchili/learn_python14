"""PEP 701: f-strings formalized; complex/nested expressions are reliable.

Run with Python >=3.12
"""

def twice(x: int) -> int:
    return x * 2

x = 5
print(f"nested: {twice(x)=}")
print(f"braces: {{ and }} stay literal; value={x}")


