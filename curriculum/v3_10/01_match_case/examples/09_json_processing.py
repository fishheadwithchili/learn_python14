"""
场景 9：JSON 数据处理

应用：处理不确定结构的 JSON 数据，如 API 响应、配置文件
运行要求：Python >= 3.10
"""

import json

print("=" * 60)
print("场景 9：JSON 数据处理")
print("=" * 60)

# 示例 1：处理不同格式的用户数据
print("\n[示例 1] 处理多格式用户数据：\n")

def process_user_data(data):
    """处理不同格式的用户 JSON 数据"""
    match data:
        # 完整的用户信息
        case {"type": "user", "id": uid, "name": name, "email": email, "age": age}:
            return f"✅ 完整用户: {name} ({email}), {age}岁, ID:{uid}"
        
        # 简化的用户信息
        case {"type": "user", "id": uid, "name": name}:
            return f"✅ 简化用户: {name}, ID:{uid}"
        
        # 匿名用户
        case {"type": "user", "id": uid, "anonymous": True}:
            return f"👻 匿名用户, ID:{uid}"
        
        # 用户列表
        case {"type": "users", "data": list(users)}:
            return f"📋 用户列表: {len(users)} 个用户"
        
        # 错误响应
        case {"type": "error", "message": msg}:
            return f"❌ 错误: {msg}"
        
        case _:
            return "⚠️  未知格式"

# 测试用户数据
user_data_samples = [
    {
        "type": "user",
        "id": 123,
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    },
    {
        "type": "user",
        "id": 456,
        "name": "Bob"
    },
    {
        "type": "user",
        "id": 789,
        "anonymous": True
    },
    {
        "type": "users",
        "data": [{"id": 1, "name": "User1"}, {"id": 2, "name": "User2"}]
    },
    {
        "type": "error",
        "message": "User not found"
    }
]

for data in user_data_samples:
    print(f"{json.dumps(data, indent=None)}")
    print(f"  -> {process_user_data(data)}\n")

# 示例 2：处理嵌套的 API 响应
print("[示例 2] 处理嵌套 API 响应：\n")

def process_api_response(response):
    """处理复杂的嵌套 API 响应"""
    match response:
        # 成功响应（带分页）
        case {
            "status": "success",
            "data": data,
            "pagination": {"page": p, "total_pages": t}
        }:
            return f"✅ 第 {p}/{t} 页，{len(data)} 条记录"
        
        # 成功响应（无分页）
        case {"status": "success", "data": data}:
            return f"✅ 获取 {len(data)} 条记录"
        
        # 单个资源响应
        case {"status": "success", "resource": {"id": rid, "type": rtype}}:
            return f"✅ 资源: {rtype} #{rid}"
        
        # 错误响应（带详情）
        case {
            "status": "error",
            "error": {"code": code, "message": msg, "details": details}
        }:
            return f"❌ 错误 {code}: {msg} (详情: {details})"
        
        # 简单错误响应
        case {"status": "error", "message": msg}:
            return f"❌ 错误: {msg}"
        
        # 部分成功
        case {
            "status": "partial",
            "succeeded": s_count,
            "failed": f_count
        }:
            return f"⚠️  部分成功: {s_count} 成功, {f_count} 失败"
        
        case _:
            return "❓ 未知响应格式"

# 测试 API 响应
api_responses = [
    {
        "status": "success",
        "data": [{"id": 1}, {"id": 2}, {"id": 3}],
        "pagination": {"page": 1, "total_pages": 10}
    },
    {
        "status": "success",
        "data": [{"id": 4}, {"id": 5}]
    },
    {
        "status": "success",
        "resource": {"id": 123, "type": "article"}
    },
    {
        "status": "error",
        "error": {
            "code": 404,
            "message": "Not found",
            "details": "Resource does not exist"
        }
    },
    {
        "status": "error",
        "message": "Bad request"
    },
    {
        "status": "partial",
        "succeeded": 8,
        "failed": 2
    }
]

for resp in api_responses:
    print(process_api_response(resp))

# 示例 3：处理配置文件
print("\n[示例 3] 处理多种配置格式：\n")

def process_config(config):
    """处理不同格式的配置"""
    match config:
        # 数据库配置（字符串 URL）
        case {"database": str(url)}:
            return f"📦 数据库 URL: {url}"
        
        # 数据库配置（详细配置）
        case {
            "database": {
                "host": host,
                "port": port,
                "name": db_name,
                **credentials
            }
        }:
            return f"📦 数据库: {host}:{port}/{db_name} (+{len(credentials)} 个认证参数)"
        
        # 日志配置
        case {"logging": {"level": level, "handlers": handlers}}:
            return f"📝 日志级别: {level}, {len(handlers)} 个处理器"
        
        # 缓存配置（Redis）
        case {"cache": {"backend": "redis", "host": h, "port": p}}:
            return f"💾 缓存: Redis {h}:{p}"
        
        # 缓存配置（内存）
        case {"cache": {"backend": "memory", "size_mb": size}}:
            return f"💾 缓存: 内存 {size}MB"
        
        # 功能开关
        case {"features": dict(features)}:
            enabled = [k for k, v in features.items() if v]
            return f"🎛️  功能: {len(enabled)}/{len(features)} 个启用"
        
        case _:
            return "⚠️  未识别的配置"

# 测试配置
configs = [
    {
        "database": "postgresql://localhost:5432/mydb"
    },
    {
        "database": {
            "host": "db.example.com",
            "port": 5432,
            "name": "production",
            "user": "admin",
            "password": "secret"
        }
    },
    {
        "logging": {
            "level": "INFO",
            "handlers": ["console", "file", "sentry"]
        }
    },
    {
        "cache": {
            "backend": "redis",
            "host": "localhost",
            "port": 6379
        }
    },
    {
        "cache": {
            "backend": "memory",
            "size_mb": 128
        }
    },
    {
        "features": {
            "dark_mode": True,
            "notifications": True,
            "analytics": False
        }
    }
]

for config in configs:
    print(f"{process_config(config)}")

# 示例 4：处理Webhook 事件
print("\n[示例 4] 处理 Webhook 事件：\n")

def process_webhook(event):
    """处理不同类型的 Webhook 事件"""
    match event:
        # GitHub push 事件
        case {
            "event": "push",
            "repository": {"name": repo},
            "commits": commits
        }:
            return f"📤 GitHub: {len(commits)} 次提交到 {repo}"
        
        # GitHub issue 事件
        case {
            "event": "issues",
            "action": action,
            "issue": {"number": num, "title": title}
        }:
            return f"🐛 GitHub Issue #{num} {action}: {title}"
        
        # Stripe 支付事件
        case {
            "type": "payment.succeeded",
            "data": {"amount": amount, "currency": curr}
        }:
            return f"💰 Stripe: 支付成功 {amount/100:.2f} {curr.upper()}"
        
        # Stripe 退款事件
        case {
            "type": "charge.refunded",
            "data": {"amount": amount}
        }:
            return f"↩️  Stripe: 退款 {amount/100:.2f}"
        
        # Slack 消息事件
        case {
            "type": "message",
            "user": user,
            "text": text,
            "channel": channel
        }:
            preview = text[:30] + "..." if len(text) > 30 else text
            return f"💬 Slack: {user} 在 {channel}: {preview}"
        
        case _:
            return "❓ 未知事件类型"

# 测试 Webhook 事件
webhook_events = [
    {
        "event": "push",
        "repository": {"name": "my-repo"},
        "commits": [{"id": "abc123"}, {"id": "def456"}]
    },
    {
        "event": "issues",
        "action": "opened",
        "issue": {"number": 42, "title": "Bug in login form"}
    },
    {
        "type": "payment.succeeded",
        "data": {"amount": 9999, "currency": "usd"}
    },
    {
        "type": "charge.refunded",
        "data": {"amount": 5000}
    },
    {
        "type": "message",
        "user": "alice",
        "text": "Hello team! Just deployed the new feature.",
        "channel": "#general"
    }
]

for event in webhook_events:
    print(process_webhook(event))

# 示例 5：处理多语言数据
print("\n[示例 5] 处理多语言数据：\n")

def process_i18n_data(data):
    """处理国际化数据"""
    match data:
        # 完整翻译
        case {
            "key": key,
            "translations": {
                "en": en,
                "zh": zh,
                "es": es,
                **other
            }
        }:
            return f"🌐 '{key}': 3种主要语言 + {len(other)} 种其他语言"
        
        # 部分翻译
        case {"key": key, "translations": {"en": en, "zh": zh}}:
            return f"🌐 '{key}': 英文和中文"
        
        # 仅英文
        case {"key": key, "translations": {"en": en}}:
            return f"🌐 '{key}': 仅英文"
        
        # 缺少翻译
        case {"key": key, "translations": {}}:
            return f"⚠️  '{key}': 没有翻译"
        
        case _:
            return "❌ 无效的国际化数据"

# 测试国际化数据
i18n_data = [
    {
        "key": "welcome_message",
        "translations": {
            "en": "Welcome",
            "zh": "欢迎",
            "es": "Bienvenido",
            "fr": "Bienvenue",
            "de": "Willkommen"
        }
    },
    {
        "key": "logout",
        "translations": {
            "en": "Logout",
            "zh": "退出"
        }
    },
    {
        "key": "help",
        "translations": {
            "en": "Help"
        }
    },
    {
        "key": "new_feature",
        "translations": {}
    }
]

for data in i18n_data:
    print(process_i18n_data(data))

# 示例 6：综合 JSON 处理器
print("\n[示例 6] 综合 JSON 数据处理器：\n")

class JSONProcessor:
    """JSON 数据处理器"""
    
    def process(self, data):
        """根据数据类型分发到相应的处理器"""
        match data:
            case {"_type": "user", **user_data}:
                return ("user", process_user_data({"type": "user", **user_data}))
            case {"_type": "api_response", **resp_data}:
                return ("api", process_api_response(resp_data))
            case {"_type": "config", **config_data}:
                return ("config", process_config(config_data))
            case {"_type": "webhook", **event_data}:
                return ("webhook", process_webhook(event_data))
            case {"_type": "i18n", **i18n_data}:
                return ("i18n", process_i18n_data(i18n_data))
            case _:
                return ("unknown", "未知数据类型")

# 测试综合处理器
processor = JSONProcessor()

mixed_data = [
    {"_type": "user", "id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
    {"_type": "api_response", "status": "success", "data": [1, 2, 3]},
    {"_type": "config", "database": "postgresql://localhost/db"},
    {"_type": "webhook", "type": "payment.succeeded", "data": {"amount": 1999, "currency": "usd"}},
    {"_type": "i18n", "key": "hello", "translations": {"en": "Hello", "zh": "你好"}}
]

for data in mixed_data:
    data_type, result = processor.process(data)
    print(f"[{data_type.upper()}] {result}")

print("\n💡 总结：match/case 简化了复杂 JSON 数据的处理逻辑")

