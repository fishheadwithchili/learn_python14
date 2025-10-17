"""Demonstrate PEP 584 dict merge/update operators.

Run with Python >=3.9
"""

defaults = {"host": "localhost", "port": 5432, "debug": False}
env = {"port": 5433}
cli = {"debug": True}

merged = defaults | env | cli
print(merged)

cfg = defaults.copy()
cfg |= env
cfg |= cli
print(cfg)


