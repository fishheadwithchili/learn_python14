"""
场景 5：配置参数说明

应用：为配置项附加说明、默认值和环境变量名
"""

from typing import Annotated, get_type_hints
from dataclasses import dataclass, field

class ConfigMeta:
    """配置元数据"""
    def __init__(self, description, default=None, env_var=None):
        self.description = description
        self.default = default
        self.env_var = env_var

# ✅ 使用 Annotated 定义配置

@dataclass
class AppConfig:
    """应用配置"""
    host: Annotated[str, ConfigMeta("服务器地址", default="0.0.0.0", env_var="APP_HOST")] = "0.0.0.0"
    port: Annotated[int, ConfigMeta("服务器端口", default=8000, env_var="APP_PORT")] = 8000
    debug: Annotated[bool, ConfigMeta("调试模式", default=False, env_var="APP_DEBUG")] = False
    db_url: Annotated[str, ConfigMeta("数据库URL", env_var="DATABASE_URL")] = "sqlite:///app.db"
    secret_key: Annotated[str, ConfigMeta("密钥", env_var="SECRET_KEY")] = "dev-secret"
    max_workers: Annotated[int, ConfigMeta("最大工作进程数", default=4)] = 4

def print_config_doc(config_class):
    """打印配置文档"""
    hints = get_type_hints(config_class, include_extras=True)
    
    print(f"配置类: {config_class.__name__}\n")
    for field_name, field_type in hints.items():
        if hasattr(field_type, '__metadata__'):
            for metadata in field_type.__metadata__:
                if isinstance(metadata, ConfigMeta):
                    print(f"{field_name}:")
                    print(f"  说明: {metadata.description}")
                    if metadata.default is not None:
                        print(f"  默认: {metadata.default}")
                    if metadata.env_var:
                        print(f"  环境变量: {metadata.env_var}")
                    print()

print("=" * 60)
print("场景 5：配置参数说明")
print("=" * 60)

# 示例 1：打印配置文档
print("\n[示例 1] 应用配置文档：\n")
print_config_doc(AppConfig)

# 示例 2：使用配置
print("[示例 2] 使用配置：\n")
config = AppConfig()
print(f"服务器: {config.host}:{config.port}")
print(f"调试模式: {config.debug}")
print(f"数据库: {config.db_url}")

print("\n💡 总结：Annotated 让配置自带文档，便于理解和维护")

