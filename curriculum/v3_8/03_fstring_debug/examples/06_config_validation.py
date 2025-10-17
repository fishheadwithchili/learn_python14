"""
场景 6：配置验证输出

应用：系统启动时验证配置项
"""

class Config:
    def __init__(self):
        self.database_url = "postgresql://localhost/mydb"
        self.cache_size = 1000
        self.debug_mode = True
        self.max_connections = 100
        self.timeout = 30

print("=" * 60)
print("配置验证")
print("=" * 60)

config = Config()

print("\n配置项检查：\n")
print(f"{config.database_url=}")
print(f"{config.cache_size=}")
print(f"{config.debug_mode=}")
print(f"{config.max_connections=}")
print(f"{config.timeout=}")

print("\n验证规则：\n")

# 验证缓存大小
assert config.cache_size > 0, f"{config.cache_size=} 必须为正数"
print(f"  ✅ cache_size 验证通过")

# 验证连接数
assert 1 <= config.max_connections <= 1000, \
    f"{config.max_connections=} 必须在 1-1000 之间"
print(f"  ✅ max_connections 验证通过")

# 验证超时
assert config.timeout > 0, f"{config.timeout=} 必须为正数"
print(f"  ✅ timeout 验证通过")

print("\n💡 总结：配置问题一目了然，快速修复")

