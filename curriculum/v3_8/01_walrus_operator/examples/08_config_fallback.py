"""
场景 8：配置加载中的回退逻辑

应用：尝试多个配置源，使用第一个成功的
"""

import os
from typing import Optional, Dict

# 模拟不同的配置源
class ConfigSource:
    """配置源基类"""
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
    
    def load(self) -> Optional[Dict]:
        print(f"  [尝试] 从 {self.name} 加载配置...")
        if self.data:
            print(f"  [成功] 找到配置: {self.data}")
            return self.data
        else:
            print(f"  [失败] {self.name} 不可用")
            return None

# 模拟多个配置源
env_config = ConfigSource("环境变量", None)  # 失败
file_config = ConfigSource("配置文件", None)  # 失败
default_config = ConfigSource("默认配置", {
    "database": "sqlite:///default.db",
    "debug": False,
    "port": 8080
})

print("=" * 60)
print("配置加载回退逻辑")
print("=" * 60)

# ❌ 传统方式 - 需要多个 if/else
print("\n[传统方式] 多个 if/else：\n")

config = None
config = env_config.load()
if not config:
    config = file_config.load()
if not config:
    config = default_config.load()

print(f"\n最终配置: {config}\n")

# ✅ 使用 walrus operator - 链式回退
print("=" * 60)
print("[Walrus Operator] 链式回退：\n")

# 重新创建配置源
env_config2 = ConfigSource("环境变量", None)
file_config2 = ConfigSource("用户配置", {"database": "postgresql://localhost", "port": 5432})
default_config2 = ConfigSource("默认配置", {"database": "sqlite:///default.db", "port": 8080})

config = (
    (cfg := env_config2.load()) or
    (cfg := file_config2.load()) or
    (cfg := default_config2.load())
)

print(f"\n最终配置: {config}\n")

print("=" * 60)
print("更实用的示例：数据库连接配置")
print("=" * 60)

def load_from_env() -> Optional[str]:
    """从环境变量加载"""
    print("  [检查] 环境变量 DATABASE_URL")
    db_url = os.getenv('DATABASE_URL')
    if db_url:
        print(f"  [找到] {db_url}")
        return db_url
    print("  [未找到]")
    return None

def load_from_file() -> Optional[str]:
    """从配置文件加载"""
    print("  [检查] 配置文件 database.conf")
    # 模拟文件不存在
    print("  [未找到]")
    return None

def get_default() -> str:
    """默认配置"""
    print("  [使用] 默认配置")
    return "sqlite:///app.db"

print("\n确定数据库连接字符串：\n")

database_url = (
    load_from_env() or
    load_from_file() or
    get_default()
)

print(f"\n✅ 最终使用: {database_url}")

print("\n" + "=" * 60)
print("注意事项")
print("=" * 60)

print("""
⚠️  使用 walrus operator 的回退链要注意可读性：

✅ 好的用法（清晰）:
    config = (
        (cfg := source1.load()) or
        (cfg := source2.load()) or
        default_config
    )

❌ 过度使用（难读）:
    config = (a := f1()) or (b := f2()) or (c := f3()) or (d := f4()) or ...
    （超过3层建议改用 if/else）
""")

print("💡 总结：回退逻辑更紧凑，但不要过度嵌套影响可读性")

