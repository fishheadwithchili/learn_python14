"""Demonstrate structural pattern matching with nested data.

Run with Python >=3.10
"""

commands = [
    ["quit"],
    ["load", "file.txt"],
    ["save", "out.txt"],
    ["draw", {"shape": "circle", "r": 10}],
    ["draw", {"shape": "rect", "w": 5, "h": 8}],
    ["noop"],
]

for cmd in commands:
    match cmd:
        case ["quit"]:
            print("Goodbye!")
        case ["load", filename]:
            print(f"Loading {filename}")
        case ["save", filename]:
            print(f"Saving {filename}")
        case ["draw", {"shape": "circle", "r": r}]:
            area = 3.14159 * r * r
            print(f"Draw circle r={r}, area={area:.2f}")
        case ["draw", {"shape": "rect", "w": w, "h": h}]:
            print(f"Draw rect {w}x{h}, area={w*h}")
        case _:
            print(f"Unknown command: {cmd}")


