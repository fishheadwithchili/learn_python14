"""
场景 8：配置文件处理

应用：处理环境变量、配置键名、ini文件等
"""

import os

# 测试数据
env_vars = [
    ("APP_DATABASE_URL", "postgresql://localhost/mydb"),
    ("APP_SECRET_KEY", "secret123"),
    ("APP_DEBUG", "true"),
    ("DATABASE_HOST", "localhost"),
    ("REDIS_URL", "redis://localhost:6379")
]

ini_lines = [
    "[database]",
    "host=localhost",
    "port=5432",
    "[server]",
    "host=0.0.0.0",
    "port=8000"
]

print("=" * 60)
print("场景 8：配置文件处理")
print("=" * 60)

# 示例 1：环境变量前缀分组
print("\n[示例 1] 环境变量前缀分组：\n")

app_prefix = "APP_"
db_prefix = "DATABASE_"

app_config = {}
db_config = {}
other_config = {}

for key, value in env_vars:
    if key.startswith(app_prefix):
        clean_key = key.removeprefix(app_prefix).lower()
        app_config[clean_key] = value
    elif key.startswith(db_prefix):
        clean_key = key.removeprefix(db_prefix).lower()
        db_config[clean_key] = value
    else:
        other_config[key.lower()] = value

print("应用配置 (APP_*):")
for key, value in app_config.items():
    print(f"  {key}: {value}")

print("\n数据库配置 (DATABASE_*):")
for key, value in db_config.items():
    print(f"  {key}: {value}")

print("\n其他配置:")
for key, value in other_config.items():
    print(f"  {key}: {value}")

# 示例 2：INI 文件解析
print("\n[示例 2] INI 文件解析：\n")

current_section = None
ini_config = {}

for line in ini_lines:
    line = line.strip()
    
    # 检测节（section）
    if line.startswith("[") and line.endswith("]"):
        current_section = line.removeprefix("[").removesuffix("]")
        ini_config[current_section] = {}
    # 解析键值对
    elif "=" in line and current_section:
        key, value = line.split("=", 1)
        ini_config[current_section][key.strip()] = value.strip()

print("解析结果:")
for section, values in ini_config.items():
    print(f"\n[{section}]")
    for key, value in values.items():
        print(f"  {key} = {value}")

# 示例 3：点号分隔的配置键
print("\n[示例 3] 嵌套配置键处理：\n")

dotted_keys = [
    "database.host",
    "database.port",
    "database.credentials.username",
    "database.credentials.password",
    "server.host",
    "server.port"
]

def parse_dotted_key(key):
    """解析点号分隔的配置键为嵌套字典"""
    parts = key.split(".")
    result = {}
    current = result
    
    for i, part in enumerate(parts[:-1]):
        current[part] = {}
        current = current[part]
    
    current[parts[-1]] = f"<value for {key}>"
    return result

print("点号配置键:")
for key in dotted_keys[:3]:
    print(f"  {key}")

# 示例 4：配置继承
print("\n[示例 4] 配置继承（移除 base. 前缀）：\n")

config_with_inheritance = [
    "base.timeout=30",
    "base.retry=3",
    "production.timeout=60",  # 覆盖 base
    "production.host=prod.example.com"
]

base_config = {}
prod_config = {}

for item in config_with_inheritance:
    key, value = item.split("=")
    
    if key.startswith("base."):
        clean_key = key.removeprefix("base.")
        base_config[clean_key] = value
    elif key.startswith("production."):
        clean_key = key.removeprefix("production.")
        prod_config[clean_key] = value

# 生产环境配置 = 基础配置 + 覆盖
final_prod_config = {**base_config, **prod_config}

print("基础配置:")
for k, v in base_config.items():
    print(f"  {k}: {v}")

print("\n生产环境配置:")
for k, v in final_prod_config.items():
    source = "(覆盖)" if k in prod_config else "(继承)"
    print(f"  {k}: {v} {source}")

# 示例 5：配置命名空间
print("\n[示例 5] 配置命名空间提取：\n")

namespaced_config = {
    "app:database:host": "localhost",
    "app:database:port": "5432",
    "app:cache:host": "redis",
    "app:cache:port": "6379",
    "log:level": "INFO"
}

def extract_namespace(config, namespace):
    """提取特定命名空间的配置"""
    prefix = f"{namespace}:"
    result = {}
    
    for key, value in config.items():
        if key.startswith(prefix):
            clean_key = key.removeprefix(prefix)
            result[clean_key] = value
    
    return result

db_ns = extract_namespace(namespaced_config, "app:database")
cache_ns = extract_namespace(namespaced_config, "app:cache")

print("数据库命名空间 (app:database):")
for k, v in db_ns.items():
    print(f"  {k}: {v}")

print("\n缓存命名空间 (app:cache):")
for k, v in cache_ns.items():
    print(f"  {k}: {v}")

# 示例 6：配置类型转换
print("\n[示例 6] 环境变量类型推断：\n")

typed_env_vars = [
    "PORT=8000",
    "DEBUG=true",
    "TIMEOUT=30.5",
    "APP_NAME=MyApp"
]

def parse_env_value(value_str):
    """推断并转换环境变量值的类型"""
    value_str = value_str.strip()
    
    # 布尔值
    if value_str.lower() in ["true", "false"]:
        return value_str.lower() == "true"
    
    # 整数
    try:
        return int(value_str)
    except ValueError:
        pass
    
    # 浮点数
    try:
        return float(value_str)
    except ValueError:
        pass
    
    # 字符串
    return value_str

print("类型推断:")
for env_var in typed_env_vars:
    key, value_str = env_var.split("=")
    value = parse_env_value(value_str)
    print(f"  {key}: {value} (类型: {type(value).__name__})")

print("\n💡 总结：removeprefix/removesuffix 简化配置文件处理和命名空间管理")

