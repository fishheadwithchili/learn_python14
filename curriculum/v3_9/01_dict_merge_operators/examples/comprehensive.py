"""
综合示例：配置管理系统

场景：构建一个应用程序配置管理系统，需要处理多层配置来源、
环境变量覆盖、用户自定义配置和运行时配置更新。

展示了字典合并运算符在实际应用中的综合运用。
"""

import os
from typing import Dict, Any

# ============= 配置定义 =============

# 1. 应用默认配置
DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "workers": 4
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "pool_size": 10
    },
    "features": {
        "cache": True,
        "metrics": False,
        "auth": True
    }
}

# 2. 环境特定配置
DEVELOPMENT_CONFIG = {
    "debug": True,
    "log_level": "DEBUG",
    "server": {
        "port": 3000,
        "workers": 1
    },
    "features": {
        "metrics": True
    }
}

PRODUCTION_CONFIG = {
    "log_level": "WARNING",
    "server": {
        "workers": 8
    },
    "database": {
        "pool_size": 50
    },
    "features": {
        "cache": True,
        "metrics": True
    }
}

# 3. 模拟从环境变量读取的配置
def load_env_config() -> Dict[str, Any]:
    """从环境变量加载配置（优先级最高）"""
    config = {}
    
    # 模拟环境变量
    env_vars = {
        "APP_DEBUG": "true",
        "APP_SERVER_PORT": "9000",
        "APP_DB_HOST": "db.example.com"
    }
    
    if env_vars.get("APP_DEBUG") == "true":
        config["debug"] = True
    
    if "APP_SERVER_PORT" in env_vars:
        config.setdefault("server", {})["port"] = int(env_vars["APP_SERVER_PORT"])
    
    if "APP_DB_HOST" in env_vars:
        config.setdefault("database", {})["host"] = env_vars["APP_DB_HOST"]
    
    return config

# ============= 配置管理类 =============

class ConfigManager:
    """配置管理器"""
    
    def __init__(self, environment: str = "development"):
        self.environment = environment
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """加载配置（传统方式对比）"""
        # 选择环境配置
        env_config = {
            "development": DEVELOPMENT_CONFIG,
            "production": PRODUCTION_CONFIG
        }.get(self.environment, {})
        
        # 加载环境变量配置
        env_vars_config = load_env_config()
        
        # ✅ 使用 | 运算符合并配置（优先级递增）
        config = DEFAULT_CONFIG | env_config | env_vars_config
        
        return config
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值（支持点号分隔的嵌套键）"""
        keys = key.split(".")
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def update(self, updates: Dict[str, Any]) -> None:
        """运行时更新配置"""
        # ✅ 使用 |= 就地更新
        self.config |= updates
    
    def override(self, **kwargs) -> Dict[str, Any]:
        """创建临时覆盖配置（不修改原配置）"""
        # ✅ 使用 | 创建新配置
        return self.config | kwargs
    
    def to_dict(self) -> Dict[str, Any]:
        """返回配置字典"""
        return self.config.copy()


# ============= 示例使用 =============

def main():
    print("=" * 70)
    print("综合示例：配置管理系统")
    print("=" * 70)
    
    # 场景 1：开发环境配置
    print("\n[场景 1] 加载开发环境配置\n")
    
    dev_config = ConfigManager("development")
    
    print(f"应用名称: {dev_config.get('app_name')}")
    print(f"调试模式: {dev_config.get('debug')}")
    print(f"日志级别: {dev_config.get('log_level')}")
    print(f"服务器端口: {dev_config.get('server.port')}")
    print(f"数据库主机: {dev_config.get('database.host')}")
    print(f"工作进程数: {dev_config.get('server.workers')}")
    
    # 场景 2：生产环境配置
    print("\n[场景 2] 加载生产环境配置\n")
    
    prod_config = ConfigManager("production")
    
    print(f"调试模式: {prod_config.get('debug')}")
    print(f"日志级别: {prod_config.get('log_level')}")
    print(f"工作进程数: {prod_config.get('server.workers')}")
    print(f"数据库连接池: {prod_config.get('database.pool_size')}")
    
    # 场景 3：运行时更新配置
    print("\n[场景 3] 运行时更新配置\n")
    
    print(f"更新前的日志级别: {dev_config.get('log_level')}")
    
    # ✅ 使用 |= 批量更新
    dev_config.update({
        "log_level": "ERROR",
        "features": {"cache": False, "metrics": True}
    })
    
    print(f"更新后的日志级别: {dev_config.get('log_level')}")
    print(f"缓存功能: {dev_config.get('features.cache')}")
    print(f"指标功能: {dev_config.get('features.metrics')}")
    
    # 场景 4：临时覆盖配置（不修改原配置）
    print("\n[场景 4] 临时覆盖配置（用于测试）\n")
    
    # ✅ 使用 | 创建临时配置
    test_config = prod_config.override(
        debug=True,
        log_level="DEBUG",
        database={"host": "test-db.local", "name": "test_db"}
    )
    
    print(f"测试配置调试模式: {test_config.get('debug')}")
    print(f"测试配置数据库: {test_config.get('database')}")
    print(f"原配置调试模式: {prod_config.get('debug')} (未被修改)")
    
    # 场景 5：多层配置合并示例
    print("\n[场景 5] 配置优先级演示\n")
    
    print("配置合并顺序（优先级递增）：")
    print("  1. 默认配置 (DEFAULT_CONFIG)")
    print("  2. 环境配置 (DEVELOPMENT_CONFIG / PRODUCTION_CONFIG)")
    print("  3. 环境变量配置 (load_env_config)")
    print()
    
    # 追踪 server.port 的值变化
    print(f"默认端口: {DEFAULT_CONFIG['server']['port']}")
    print(f"开发环境端口: {DEVELOPMENT_CONFIG.get('server', {}).get('port', '未设置')}")
    print(f"环境变量端口: {load_env_config().get('server', {}).get('port', '未设置')}")
    print(f"→ 最终端口: {dev_config.get('server.port')} (环境变量优先级最高)")
    
    # 场景 6：配置快照和还原
    print("\n[场景 6] 配置快照和还原\n")
    
    # 保存快照
    snapshot = dev_config.to_dict()
    print(f"保存快照: log_level={snapshot['log_level']}")
    
    # 修改配置
    dev_config.update({"log_level": "CRITICAL", "debug": False})
    print(f"修改后: log_level={dev_config.get('log_level')}, debug={dev_config.get('debug')}")
    
    # 还原配置（使用 | 创建新的配置管理器）
    dev_config.config = DEFAULT_CONFIG | snapshot
    print(f"还原后: log_level={dev_config.get('log_level')}, debug={dev_config.get('debug')}")
    
    # 总结
    print("\n" + "=" * 70)
    print("💡 总结")
    print("=" * 70)
    print()
    print("字典合并运算符的优势：")
    print("  ✅ 清晰表达配置优先级：config = default | env | user")
    print("  ✅ 简洁的运行时更新：config |= updates")
    print("  ✅ 不可变配置副本：test_config = config | overrides")
    print("  ✅ 代码可读性高：一眼看出配置来源和优先级")
    print()
    print("适用场景：")
    print("  • 应用程序配置管理")
    print("  • 环境变量覆盖")
    print("  • 多租户配置")
    print("  • 特性开关系统")
    print("  • A/B 测试配置")


if __name__ == "__main__":
    main()

