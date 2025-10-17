"""
场景 4：配置文件验证

应用：验证和解析各种格式的配置数据
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 4：配置文件验证")
print("=" * 60)

# 示例 1：数据库配置验证
print("\n[示例 1] 数据库配置验证：\n")

def validate_database_config(config):
    """验证数据库配置"""
    match config:
        case {"type": "sqlite", "path": str(db_path)}:
            return f"✅ SQLite 配置有效: {db_path}"
        case {"type": "postgres", "host": str(h), "port": int(p), "database": str(db)}:
            return f"✅ PostgreSQL 配置有效: {h}:{p}/{db}"
        case {"type": "mysql", "host": str(h), "user": str(u), "password": str(pwd)}:
            return f"✅ MySQL 配置有效: {u}@{h}"
        case {"type": "mongodb", "url": str(url)}:
            return f"✅ MongoDB 配置有效: {url}"
        case {"type": db_type}:
            return f"❌ 不支持的数据库类型: {db_type}"
        case _:
            return "❌ 无效的数据库配置"

# 测试数据库配置
db_configs = [
    {"type": "sqlite", "path": "/data/app.db"},
    {"type": "postgres", "host": "localhost", "port": 5432, "database": "myapp"},
    {"type": "mysql", "host": "192.168.1.100", "user": "root", "password": "secret"},
    {"type": "mongodb", "url": "mongodb://localhost:27017/mydb"},
    {"type": "oracle"},
    {"invalid": "config"}
]

for config in db_configs:
    print(f"配置: {config}")
    print(f"  {validate_database_config(config)}\n")

# 示例 2：服务器配置验证（带默认值）
print("[示例 2] 服务器配置（支持默认值）：\n")

def validate_server_config(config):
    """验证服务器配置，支持默认值"""
    match config:
        case {"host": str(h), "port": int(p), "workers": int(w)} if 1 <= p <= 65535 and w > 0:
            return f"✅ 服务器配置: {h}:{p}，{w} 个工作进程"
        case {"host": str(h), "port": int(p)}:
            return f"✅ 服务器配置: {h}:{p}（默认 4 个工作进程）"
        case {"port": int(p)} if 1 <= p <= 65535:
            return f"✅ 端口 {p}（默认主机 0.0.0.0）"
        case {}:
            return "✅ 使用全部默认值：0.0.0.0:8000，4 个工作进程"
        case {"port": bad_port}:
            return f"❌ 无效的端口号: {bad_port}"
        case _:
            return "❌ 无效的配置"

# 测试服务器配置
server_configs = [
    {"host": "localhost", "port": 8000, "workers": 8},
    {"host": "0.0.0.0", "port": 3000},
    {"port": 5000},
    {},
    {"port": 99999},
    {"host": "localhost"}
]

for config in server_configs:
    print(f"{str(config):50s} -> {validate_server_config(config)}")

# 示例 3：日志配置验证
print("\n[示例 3] 日志配置验证：\n")

def validate_logging_config(config):
    """验证日志配置"""
    match config:
        case {"level": level, "file": str(path)} if level in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            return f"✅ 日志级别 {level}，输出到文件: {path}"
        case {"level": level, "console": True} if level in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            return f"✅ 日志级别 {level}，输出到控制台"
        case {"level": level, "handlers": handlers} if isinstance(handlers, list):
            return f"✅ 日志级别 {level}，{len(handlers)} 个处理器"
        case {"level": bad_level}:
            return f"❌ 无效的日志级别: {bad_level}"
        case _:
            return "❌ 无效的日志配置"

# 测试日志配置
logging_configs = [
    {"level": "INFO", "file": "/var/log/app.log"},
    {"level": "DEBUG", "console": True},
    {"level": "ERROR", "handlers": ["file", "email", "sentry"]},
    {"level": "TRACE"},
    {"file": "/tmp/app.log"}
]

for config in logging_configs:
    print(f"{validate_logging_config(config)}")

# 示例 4：缓存配置验证
print("\n[示例 4] 缓存配置验证：\n")

def validate_cache_config(config):
    """验证缓存配置"""
    match config:
        case {"backend": "memory", "size": int(s)} if s > 0:
            return f"✅ 内存缓存: {s}MB"
        case {"backend": "redis", "host": str(h), "port": int(p), "db": int(db)}:
            return f"✅ Redis 缓存: {h}:{p} DB{db}"
        case {"backend": "memcached", "servers": list(servers)} if servers:
            return f"✅ Memcached: {len(servers)} 个服务器"
        case {"backend": "disabled"}:
            return "⚠️  缓存已禁用"
        case {"backend": backend}:
            return f"❌ 不支持的缓存后端: {backend}"
        case _:
            return "❌ 无效的缓存配置"

# 测试缓存配置
cache_configs = [
    {"backend": "memory", "size": 128},
    {"backend": "redis", "host": "localhost", "port": 6379, "db": 0},
    {"backend": "memcached", "servers": ["10.0.0.1:11211", "10.0.0.2:11211"]},
    {"backend": "disabled"},
    {"backend": "filesystem"},
    {}
]

for config in cache_configs:
    print(f"{validate_cache_config(config)}")

# 示例 5：安全配置验证
print("\n[示例 5] 安全配置验证：\n")

def validate_security_config(config):
    """验证安全配置"""
    match config:
        case {"https": True, "cert": str(cert), "key": str(key)}:
            return f"✅ HTTPS 启用: cert={cert}, key={key}"
        case {"https": False}:
            return "⚠️  HTTPS 未启用（不安全）"
        case {"auth": {"type": "jwt", "secret": str(s), "expires": int(exp)}}:
            return f"✅ JWT 认证: 过期时间 {exp} 秒"
        case {"auth": {"type": "basic", "username": str(u), "password": str(p)}}:
            return f"✅ Basic 认证: 用户 {u}"
        case {"auth": {"type": "oauth2", "provider": str(prov)}}:
            return f"✅ OAuth2 认证: 提供商 {prov}"
        case {"cors": {"allowed_origins": list(origins)}}:
            return f"✅ CORS 配置: {len(origins)} 个允许的来源"
        case _:
            return "❌ 无效的安全配置"

# 测试安全配置
security_configs = [
    {"https": True, "cert": "/etc/ssl/cert.pem", "key": "/etc/ssl/key.pem"},
    {"https": False},
    {"auth": {"type": "jwt", "secret": "my-secret-key", "expires": 3600}},
    {"auth": {"type": "basic", "username": "admin", "password": "admin123"}},
    {"auth": {"type": "oauth2", "provider": "google"}},
    {"cors": {"allowed_origins": ["https://app.example.com", "https://api.example.com"]}}
]

for config in security_configs:
    print(f"{validate_security_config(config)}\n")

# 示例 6：完整应用配置验证
print("[示例 6] 完整应用配置验证：\n")

def validate_app_config(config):
    """验证完整的应用配置"""
    match config:
        case {
            "app_name": str(name),
            "environment": env,
            "database": db_conf,
            "server": server_conf
        } if env in ["development", "staging", "production"]:
            return {
                "valid": True,
                "name": name,
                "env": env,
                "db_valid": validate_database_config(db_conf),
                "server_valid": validate_server_config(server_conf)
            }
        case {"app_name": str(name), "environment": env}:
            return {
                "valid": False,
                "error": f"缺少必需的配置项（环境: {env}）"
            }
        case _:
            return {
                "valid": False,
                "error": "配置格式完全无效"
            }

# 测试完整配置
app_config = {
    "app_name": "MyApp",
    "environment": "production",
    "database": {
        "type": "postgres",
        "host": "db.example.com",
        "port": 5432,
        "database": "myapp_prod"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "workers": 16
    }
}

result = validate_app_config(app_config)
print(f"应用配置验证结果:")
for key, value in result.items():
    print(f"  {key}: {value}")

# 测试不完整配置
incomplete_config = {
    "app_name": "IncompleteApp",
    "environment": "development"
}

result2 = validate_app_config(incomplete_config)
print(f"\n不完整配置验证结果:")
for key, value in result2.items():
    print(f"  {key}: {value}")

print("\n💡 总结：match/case 非常适合配置验证，支持复杂的嵌套结构")

