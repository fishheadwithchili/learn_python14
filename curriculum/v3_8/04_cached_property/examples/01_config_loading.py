"""
场景 1：配置对象的惰性解析

应用：应用启动时加载配置，某些配置项可能不会被使用
"""

from functools import cached_property
import time

class AppConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        print(f"  [初始化] 配置文件: {config_file}")
    
    @cached_property
    def database_url(self):
        """解析数据库配置（耗时操作）"""
        print(f"  [解析] database_url...")
        time.sleep(0.1)  # 模拟解析耗时
        return "postgresql://localhost/mydb"
    
    @cached_property
    def redis_url(self):
        """解析 Redis 配置"""
        print(f"  [解析] redis_url...")
        time.sleep(0.1)
        return "redis://localhost:6379"
    
    @cached_property
    def secret_key(self):
        """解析密钥"""
        print(f"  [解析] secret_key...")
        time.sleep(0.1)
        return "super-secret-key-12345"

print("=" * 60)
print("配置惰性加载")
print("=" * 60)

print("\n创建配置对象：\n")
config = AppConfig("config.yaml")

print("\n首次访问 database_url：\n")
print(f"  {config.database_url}")

print("\n再次访问 database_url（从缓存）：\n")
print(f"  {config.database_url}")

print("\n访问其他配置：\n")
print(f"  Redis: {config.redis_url}")
print(f"  Secret: {config.secret_key}")

print("\n💡 总结：配置按需加载，启动速度更快")

