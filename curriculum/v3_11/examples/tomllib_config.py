"""Read TOML config using tomllib (PEP 680).

Run with Python >=3.11
"""

import tomllib

CONFIG = b"""
[server]
host = "127.0.0.1"
port = 8080
"""

cfg = tomllib.loads(CONFIG.decode("utf-8"))
print(cfg["server"]["host"], cfg["server"]["port"]) 


