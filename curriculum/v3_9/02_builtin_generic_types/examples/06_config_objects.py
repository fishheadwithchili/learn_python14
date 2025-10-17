"""
场景 6：配置对象

应用：定义应用程序配置的类型，确保配置数据结构的正确性
"""

from dataclasses import dataclass, field

# ✅ Python 3.9+ 方式：使用内置泛型定义配置类型

@dataclass
class DatabaseConfig:
    """数据库配置"""
    connections: dict[str, dict[str, str | int]]
    pool_settings: dict[str, int]
    migrations: list[str] = field(default_factory=list)
    
    def get_connection(self, name: str) -> dict[str, str | int] | None:
        """获取连接配置"""
        return self.connections.get(name)


@dataclass
class CacheConfig:
    """缓存配置"""
    servers: list[tuple[str, int]]  # (host, port)
    ttl: dict[str, int]  # 各类数据的TTL
    options: dict[str, bool] = field(default_factory=dict)


@dataclass
class APIConfig:
    """API 配置"""
    endpoints: dict[str, str]
    rate_limits: dict[str, int]
    timeout_seconds: int = 30
    retry_policy: dict[str, int] = field(default_factory=lambda: {"max_retries": 3, "backoff": 2})


@dataclass
class AppConfig:
    """应用配置（组合多个子配置）"""
    app_name: str
    version: str
    environment: str
    database: DatabaseConfig
    cache: CacheConfig
    api: APIConfig
    feature_flags: dict[str, bool] = field(default_factory=dict)
    
    def is_feature_enabled(self, feature: str) -> bool:
        """检查特性是否启用"""
        return self.feature_flags.get(feature, False)


def load_config() -> AppConfig:
    """加载应用配置"""
    db_config = DatabaseConfig(
        connections={
            "primary": {"host": "localhost", "port": 5432, "database": "myapp"},
            "replica": {"host": "replica.local", "port": 5432, "database": "myapp"}
        },
        pool_settings={
            "min_size": 5,
            "max_size": 20,
            "timeout": 30
        },
        migrations=["001_initial.sql", "002_add_users.sql"]
    )
    
    cache_config = CacheConfig(
        servers=[("redis1", 6379), ("redis2", 6379)],
        ttl={
            "user_session": 3600,
            "api_response": 300,
            "page_cache": 600
        },
        options={"enable_compression": True}
    )
    
    api_config = APIConfig(
        endpoints={
            "auth": "https://auth.example.com/api/v1",
            "users": "https://api.example.com/users",
            "payments": "https://api.example.com/payments"
        },
        rate_limits={
            "auth": 100,
            "users": 1000,
            "payments": 50
        }
    )
    
    return AppConfig(
        app_name="MyApp",
        version="1.0.0",
        environment="production",
        database=db_config,
        cache=cache_config,
        api=api_config,
        feature_flags={
            "new_ui": True,
            "beta_features": False,
            "analytics": True
        }
    )


print("=" * 60)
print("场景 6：配置对象")
print("=" * 60)

# 加载配置
config = load_config()

# 示例 1：访问数据库配置
print("\n[示例 1] 数据库配置：\n")
print(f"应用: {config.app_name} v{config.version}")
print(f"环境: {config.environment}")

primary_db = config.database.get_connection("primary")
print(f"\n主数据库: {primary_db}")
print(f"连接池设置: {config.database.pool_settings}")
print(f"迁移文件数: {len(config.database.migrations)}")

# 示例 2：缓存配置
print("\n[示例 2] 缓存配置：\n")
print(f"缓存服务器: {config.cache.servers}")
print(f"TTL 设置:")
for cache_type, ttl in config.cache.ttl.items():
    print(f"  {cache_type}: {ttl}秒")
print(f"压缩: {config.cache.options.get('enable_compression', False)}")

# 示例 3：API 配置
print("\n[示例 3] API 配置：\n")
print(f"API 端点:")
for service, url in config.api.endpoints.items():
    print(f"  {service}: {url}")

print(f"\nAPI 速率限制:")
for service, limit in config.api.rate_limits.items():
    print(f"  {service}: {limit} 请求/分钟")

print(f"\n超时: {config.api.timeout_seconds}秒")
print(f"重试策略: {config.api.retry_policy}")

# 示例 4：特性开关
print("\n[示例 4] 特性开关：\n")
features = ["new_ui", "beta_features", "analytics", "dark_mode"]

for feature in features:
    enabled = config.is_feature_enabled(feature)
    status = "✅ 启用" if enabled else "❌ 禁用"
    print(f"  {feature}: {status}")

# 示例 5：配置验证
print("\n[示例 5] 配置验证：\n")

def validate_config(cfg: AppConfig) -> list[str]:
    """验证配置有效性"""
    errors: list[str] = []
    
    # 验证数据库配置
    if not cfg.database.connections:
        errors.append("至少需要一个数据库连接")
    
    # 验证缓存配置
    if not cfg.cache.servers:
        errors.append("至少需要一个缓存服务器")
    
    # 验证API配置
    if cfg.api.timeout_seconds <= 0:
        errors.append("API 超时必须大于0")
    
    return errors

validation_errors = validate_config(config)
if validation_errors:
    print("配置错误:")
    for error in validation_errors:
        print(f"  ❌ {error}")
else:
    print("✅ 配置验证通过")

# 示例 6：动态更新配置
print("\n[示例 6] 动态更新配置：\n")

print(f"更新前: beta_features = {config.feature_flags.get('beta_features')}")

# 更新特性开关
config.feature_flags["beta_features"] = True
config.feature_flags["experimental"] = True

print(f"更新后: beta_features = {config.feature_flags.get('beta_features')}")
print(f"新增: experimental = {config.feature_flags.get('experimental')}")

print("\n[类型注解的优势]")
print("  ✅ 配置结构清晰可见")
print("  ✅ IDE 自动补全配置项")
print("  ✅ 类型检查防止配置错误")
print("  ✅ 便于生成配置文档")

print("\n💡 总结：内置泛型让配置对象类型安全且易于维护")

