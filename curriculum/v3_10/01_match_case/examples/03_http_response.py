"""
场景 3：HTTP 响应处理

应用：根据 API 响应的不同结构进行相应处理
运行要求：Python >= 3.10
"""

print("=" * 60)
print("场景 3：HTTP 响应处理")
print("=" * 60)

# 模拟 HTTP 响应数据
from typing import Dict, Any

# 示例 1：基于状态码的响应处理
print("\n[示例 1] 基于状态码的响应处理：\n")

def handle_api_response(response: Dict[str, Any]) -> str:
    """处理 API 响应"""
    match response:
        case {"status": 200, "data": data}:
            return f"✅ 成功获取数据: {data}"
        case {"status": 201, "data": data, "id": resource_id}:
            return f"✅ 资源已创建，ID: {resource_id}"
        case {"status": 204}:
            return "✅ 操作成功（无内容）"
        case {"status": 400, "error": error}:
            return f"❌ 请求错误: {error}"
        case {"status": 401}:
            return "❌ 未授权，请登录"
        case {"status": 403}:
            return "❌ 禁止访问"
        case {"status": 404}:
            return "❌ 资源未找到"
        case {"status": 500, "error": error}:
            return f"❌ 服务器错误: {error}"
        case {"status": code}:
            return f"❓ 未处理的状态码: {code}"
        case _:
            return "❌ 无效的响应格式"

# 测试不同的响应
responses = [
    {"status": 200, "data": {"user": "Alice", "age": 25}},
    {"status": 201, "data": {"name": "New User"}, "id": 12345},
    {"status": 204},
    {"status": 400, "error": "Missing required field: email"},
    {"status": 401},
    {"status": 404},
    {"status": 500, "error": "Database connection failed"},
    {"status": 999},
    {"invalid": "response"}
]

for i, resp in enumerate(responses, 1):
    print(f"响应 {i}: {resp}")
    print(f"  处理结果: {handle_api_response(resp)}\n")

# 示例 2：RESTful API 响应处理
print("[示例 2] RESTful API 响应（带分页）：\n")

def handle_paginated_response(response: Dict[str, Any]) -> str:
    """处理带分页的响应"""
    match response:
        case {"status": 200, "data": items, "pagination": {"page": p, "total": t}}:
            return f"📄 第 {p} 页，共 {t} 页，{len(items)} 条记录"
        case {"status": 200, "data": items}:
            return f"📋 获取 {len(items)} 条记录（无分页）"
        case {"status": 200, "data": []}:
            return "📭 空结果集"
        case {"error": error_msg}:
            return f"❌ 错误: {error_msg}"
        case _:
            return "❌ 未知响应格式"

# 测试分页响应
paginated_responses = [
    {
        "status": 200,
        "data": [{"id": 1}, {"id": 2}, {"id": 3}],
        "pagination": {"page": 1, "total": 10}
    },
    {
        "status": 200,
        "data": [{"id": 4}, {"id": 5}]
    },
    {
        "status": 200,
        "data": []
    },
    {
        "error": "Invalid API key"
    }
]

for resp in paginated_responses:
    print(f"{handle_paginated_response(resp)}")

# 示例 3：GraphQL 风格响应
print("\n[示例 3] GraphQL 风格响应（data + errors）：\n")

def handle_graphql_response(response: Dict[str, Any]) -> str:
    """处理 GraphQL 响应"""
    match response:
        case {"data": data, "errors": errors} if errors:
            return f"⚠️  部分成功: 数据={data}, 错误={len(errors)}个"
        case {"data": data}:
            return f"✅ 成功: {data}"
        case {"errors": errors}:
            error_msgs = [e.get("message", "Unknown") for e in errors]
            return f"❌ 失败: {', '.join(error_msgs)}"
        case _:
            return "❌ 无效响应"

# 测试 GraphQL 响应
graphql_responses = [
    {
        "data": {"user": {"name": "Alice", "email": "alice@example.com"}}
    },
    {
        "data": {"user": {"name": "Bob"}},
        "errors": [{"message": "Email field is missing"}]
    },
    {
        "errors": [
            {"message": "Authentication required"},
            {"message": "Invalid token"}
        ]
    }
]

for resp in graphql_responses:
    print(f"{handle_graphql_response(resp)}\n")

# 示例 4：文件上传响应
print("[示例 4] 文件上传响应处理：\n")

def handle_upload_response(response: Dict[str, Any]) -> str:
    """处理文件上传响应"""
    match response:
        case {"status": "success", "file": {"name": n, "size": s, "url": url}}:
            size_mb = s / (1024 * 1024)
            return f"✅ 上传成功: {n} ({size_mb:.2f}MB)\n   URL: {url}"
        case {"status": "success", "files": files}:
            total_size = sum(f["size"] for f in files)
            size_mb = total_size / (1024 * 1024)
            return f"✅ 批量上传成功: {len(files)} 个文件 ({size_mb:.2f}MB)"
        case {"status": "error", "reason": "file_too_large", "max_size": max_size}:
            return f"❌ 文件太大（最大 {max_size / (1024*1024)}MB）"
        case {"status": "error", "reason": "invalid_type", "allowed": types}:
            return f"❌ 文件类型不支持（允许: {', '.join(types)}）"
        case {"status": "error", "reason": reason}:
            return f"❌ 上传失败: {reason}"
        case _:
            return "❌ 未知响应"

# 测试上传响应
upload_responses = [
    {
        "status": "success",
        "file": {
            "name": "document.pdf",
            "size": 2 * 1024 * 1024,  # 2MB
            "url": "https://cdn.example.com/files/abc123.pdf"
        }
    },
    {
        "status": "success",
        "files": [
            {"name": "image1.jpg", "size": 500 * 1024},
            {"name": "image2.jpg", "size": 600 * 1024}
        ]
    },
    {
        "status": "error",
        "reason": "file_too_large",
        "max_size": 5 * 1024 * 1024
    },
    {
        "status": "error",
        "reason": "invalid_type",
        "allowed": ["jpg", "png", "pdf"]
    }
]

for resp in upload_responses:
    print(f"{handle_upload_response(resp)}\n")

# 示例 5：WebSocket 消息处理
print("[示例 5] WebSocket 消息处理：\n")

def handle_websocket_message(message: Dict[str, Any]) -> str:
    """处理 WebSocket 消息"""
    match message:
        case {"type": "connection", "status": "open"}:
            return "🔗 连接已建立"
        case {"type": "connection", "status": "close", "reason": reason}:
            return f"🔌 连接已关闭: {reason}"
        case {"type": "ping"}:
            return "🏓 发送 pong"
        case {"type": "message", "from": sender, "text": text}:
            return f"💬 {sender}: {text}"
        case {"type": "notification", "level": "info", "message": msg}:
            return f"ℹ️  {msg}"
        case {"type": "notification", "level": "error", "message": msg}:
            return f"❌ {msg}"
        case {"type": "user_joined", "username": user}:
            return f"👋 {user} 加入了"
        case {"type": "user_left", "username": user}:
            return f"👋 {user} 离开了"
        case _:
            return f"❓ 未知消息: {message.get('type', 'no type')}"

# 测试 WebSocket 消息
ws_messages = [
    {"type": "connection", "status": "open"},
    {"type": "ping"},
    {"type": "message", "from": "Alice", "text": "Hello everyone!"},
    {"type": "notification", "level": "info", "message": "Server update in 5 minutes"},
    {"type": "notification", "level": "error", "message": "Connection unstable"},
    {"type": "user_joined", "username": "Bob"},
    {"type": "user_left", "username": "Charlie"},
    {"type": "connection", "status": "close", "reason": "timeout"}
]

for msg in ws_messages:
    print(f"{handle_websocket_message(msg)}")

# 示例 6：带重试信息的响应
print("\n[示例 6] 带重试信息的响应：\n")

def handle_rate_limited_response(response: Dict[str, Any]) -> str:
    """处理限流响应"""
    match response:
        case {"status": 429, "retry_after": seconds}:
            return f"⏳ 请求过于频繁，请 {seconds} 秒后重试"
        case {"status": 429, "rate_limit": {"remaining": 0, "reset": reset_time}}:
            return f"⏳ API 配额用尽，将在 {reset_time} 重置"
        case {"status": 503, "retry_after": seconds}:
            return f"🔧 服务维护中，请 {seconds} 秒后重试"
        case {"status": code} if 200 <= code < 300:
            return f"✅ 请求成功 (状态码: {code})"
        case _:
            return "❌ 请求失败"

# 测试限流响应
rate_limited_responses = [
    {"status": 429, "retry_after": 60},
    {"status": 429, "rate_limit": {"remaining": 0, "reset": "2023-06-15T10:30:00Z"}},
    {"status": 503, "retry_after": 300},
    {"status": 200}
]

for resp in rate_limited_responses:
    print(f"{handle_rate_limited_response(resp)}")

print("\n💡 总结：match/case 可以优雅地处理各种 API 响应格式")

