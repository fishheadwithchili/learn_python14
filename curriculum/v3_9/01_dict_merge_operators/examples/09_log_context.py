"""
场景 9：日志记录上下文

应用：为日志添加多层上下文信息（应用级、请求级、事件级）
"""

import json
from datetime import datetime

# 应用级上下文（所有日志共享）
APP_CONTEXT = {
    "app_name": "my-web-app",
    "environment": "production",
    "version": "1.2.3"
}

# 请求级上下文
def get_request_context(request_id, user_id=None):
    """获取当前请求的上下文"""
    context = {
        "request_id": request_id,
        "timestamp": datetime.now().isoformat()
    }
    if user_id:
        context["user_id"] = user_id
    return context

# 日志函数
def log_old(level, message, request_context, event_context=None):
    """传统方式：逐步构建日志上下文"""
    log_entry = APP_CONTEXT.copy()
    log_entry.update(request_context)
    if event_context:
        log_entry.update(event_context)
    log_entry["level"] = level
    log_entry["message"] = message
    return log_entry

def log_new(level, message, request_context, event_context=None):
    """Python 3.9+ 方式：使用 | 运算符"""
    return (
        APP_CONTEXT
        | request_context
        | (event_context or {})
        | {"level": level, "message": message}
    )

print("=" * 60)
print("场景 9：日志记录上下文")
print("=" * 60)

# 模拟请求
request_ctx = get_request_context("req-12345", user_id=789)

# 示例 1：简单日志（只有应用和请求上下文）
print("\n[示例 1] 简单日志：\n")

log_entry_1_old = log_old("INFO", "User logged in", request_ctx)
log_entry_1_new = log_new("INFO", "User logged in", request_ctx)

print("传统方式:")
print(json.dumps(log_entry_1_old, indent=2))

print("\n新方式:")
print(json.dumps(log_entry_1_new, indent=2))

print(f"\n结果一致: {log_entry_1_old == log_entry_1_new}")

# 示例 2：带事件上下文的日志
print("\n[示例 2] 带事件上下文的日志：\n")

event_ctx = {
    "action": "purchase",
    "product_id": "prod-456",
    "amount": 99.99,
    "currency": "USD"
}

log_entry_2 = log_new("INFO", "Purchase completed", request_ctx, event_ctx)
print(json.dumps(log_entry_2, indent=2, ensure_ascii=False))

# 示例 3：错误日志
print("\n[示例 3] 错误日志：\n")

error_ctx = {
    "error_type": "ValidationError",
    "error_code": "E1001",
    "field": "email"
}

log_entry_3 = log_new("ERROR", "Invalid email format", request_ctx, error_ctx)
print(json.dumps(log_entry_3, indent=2, ensure_ascii=False))

# 示例 4：多层嵌套上下文
print("\n[示例 4] 多层嵌套上下文：\n")

# 数据库查询上下文
db_ctx = {
    "db_query": "SELECT * FROM users WHERE id = ?",
    "db_duration_ms": 15.3,
    "db_rows": 1
}

# API 调用上下文
api_ctx = {
    "external_api": "stripe",
    "api_duration_ms": 234.5
}

complex_log = (
    APP_CONTEXT
    | request_ctx
    | db_ctx
    | api_ctx
    | {"level": "DEBUG", "message": "Database and API call completed"}
)

print(json.dumps(complex_log, indent=2, ensure_ascii=False))

# 结构化日志聚合示例
print("\n[结构化日志聚合示例]")

logs = [
    log_new("INFO", "Request started", request_ctx),
    log_new("DEBUG", "Database query", request_ctx, db_ctx),
    log_new("DEBUG", "API call", request_ctx, api_ctx),
    log_new("INFO", "Request completed", request_ctx, {"duration_ms": 250})
]

print(f"生成了 {len(logs)} 条日志")
for log in logs:
    print(f"  [{log['level']}] {log['message']}")

# 代码对比
print("\n[代码对比]")
print("传统方式：")
print("  log_entry = APP_CONTEXT.copy()")
print("  log_entry.update(request_context)")
print("  if event_context:")
print("      log_entry.update(event_context)")
print('  log_entry["level"] = level')
print('  log_entry["message"] = message')
print()
print("新方式：")
print("  log_entry = (")
print("      APP_CONTEXT")
print("      | request_context")
print("      | (event_context or {})")
print('      | {"level": level, "message": message}')
print("  )")

print("\n💡 总结：| 运算符让日志上下文层次清晰，便于结构化日志分析")

