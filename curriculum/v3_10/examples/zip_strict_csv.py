"""Show zip(strict=True) to detect mismatched lengths.

Run with Python >=3.10
"""

headers = ["id", "name", "age"]
row_good = ["1", "Alice", "30"]
row_bad = ["2", "Bob"]

for k, v in zip(headers, row_good, strict=True):
    print(f"{k}={v}")

try:
    for _ in zip(headers, row_bad, strict=True):
        pass
except ValueError as e:
    print(f"mismatch detected: {e}")


