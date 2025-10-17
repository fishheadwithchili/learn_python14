"""Built-in generics (PEP 585): list[int], dict[str, float], etc.

Run with Python >=3.9
"""

def greet_all(names: list[str]) -> None:
    for name in names:
        print(f"Hello, {name}")


greet_all(["Alice", "Bob"]) 


