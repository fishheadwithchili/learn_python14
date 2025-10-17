"""
场景 7：协议处理

应用：移除或识别协议前缀，支持多种协议
"""

# 测试数据
urls = [
    "https://example.com/page",
    "http://localhost:8000",
    "ftp://files.example.com/document.pdf",
    "ws://socket.example.com:9000",
    "file:///home/user/document.txt"
]

email_addresses = [
    "mailto:user@example.com",
    "user@example.com"
]

phone_numbers = [
    "tel:+1-555-0123",
    "sms:+1-555-0456"
]

print("=" * 60)
print("场景 7：协议处理")
print("=" * 60)

# 示例 1：统一移除协议
print("\n[示例 1] 移除各种协议前缀：\n")

protocols = ["https://", "http://", "ftp://", "ws://", "wss://", "file://"]

for url in urls:
    clean_url = url
    detected_protocol = None
    
    # 检测并移除协议
    for protocol in protocols:
        if url.startswith(protocol):
            detected_protocol = protocol.rstrip("://")
            clean_url = url.removeprefix(protocol)
            break
    
    print(f"  原始: {url}")
    print(f"  协议: {detected_protocol or '无'}")
    print(f"  地址: {clean_url}")
    print()

# 示例 2：协议转换
print("[示例 2] HTTP 到 HTTPS 转换：\n")

http_urls = [
    "http://example.com",
    "http://api.example.com/v1",
    "https://secure.example.com"  # 已经是 https
]

print("转换为 HTTPS:")
for url in http_urls:
    if url.startswith("http://"):
        # 移除 http:// 并添加 https://
        https_url = "https://" + url.removeprefix("http://")
        print(f"  {url} → {https_url}")
    elif url.startswith("https://"):
        print(f"  {url} (已经是 HTTPS)")
    else:
        print(f"  {url} (未知协议)")

# 示例 3：邮件协议处理
print("\n[示例 3] 邮件地址协议处理：\n")

for email in email_addresses:
    address = email.removeprefix("mailto:")
    has_protocol = email.startswith("mailto:")
    
    print(f"  {email}")
    print(f"    地址: {address}")
    print(f"    包含协议: {has_protocol}")

# 示例 4：电话协议处理
print("\n[示例 4] 电话号码协议处理：\n")

for phone in phone_numbers:
    # 移除协议前缀
    number = phone.removeprefix("tel:").removeprefix("sms:")
    
    # 检测协议类型
    if phone.startswith("tel:"):
        protocol = "电话"
    elif phone.startswith("sms:"):
        protocol = "短信"
    else:
        protocol = "无协议"
    
    print(f"  {phone}")
    print(f"    类型: {protocol}")
    print(f"    号码: {number}")

# 示例 5：数据库连接字符串
print("\n[示例 5] 数据库连接字符串解析：\n")

db_urls = [
    "postgresql://user:pass@localhost:5432/mydb",
    "mysql://root@localhost/testdb",
    "sqlite:///path/to/database.db",
    "mongodb://localhost:27017/admin"
]

db_protocols = ["postgresql://", "mysql://", "sqlite:///", "mongodb://"]

for db_url in db_urls:
    db_type = None
    connection_string = db_url
    
    for protocol in db_protocols:
        if db_url.startswith(protocol):
            db_type = protocol.rstrip("://").rstrip("/")
            connection_string = db_url.removeprefix(protocol)
            break
    
    print(f"  连接字符串: {db_url}")
    print(f"  数据库类型: {db_type}")
    print(f"  连接信息: {connection_string}")
    print()

# 示例 6：自定义协议支持
print("[示例 6] 自定义应用协议：\n")

custom_urls = [
    "myapp://open/document/123",
    "myapp://settings/account",
    "myapp://share?url=https://example.com"
]

app_protocol = "myapp://"

for url in custom_urls:
    if url.startswith(app_protocol):
        action = url.removeprefix(app_protocol)
        print(f"  协议调用: {url}")
        print(f"  应用动作: {action}")

# 示例 7：协议版本处理
print("\n[示例 7] 协议版本处理：\n")

versioned_protocols = [
    "http/1.1://example.com",
    "http/2://example.com",
    "http/3://example.com"
]

for url in versioned_protocols:
    # 提取协议版本
    if "://" in url:
        protocol_part = url.split("://")[0]
        address = url.split("://", 1)[1]
        
        print(f"  URL: {url}")
        print(f"  协议: {protocol_part}")
        print(f"  地址: {address}")

# 示例 8：安全协议检查
print("\n[示例 8] 安全协议检查：\n")

mixed_urls = [
    "https://secure.example.com",
    "http://insecure.example.com",
    "ftp://files.example.com",
    "ftps://secure-files.example.com"
]

secure_protocols = ["https://", "ftps://", "wss://"]

for url in mixed_urls:
    is_secure = any(url.startswith(p) for p in secure_protocols)
    status = "✅ 安全" if is_secure else "⚠️ 不安全"
    
    print(f"  {url}")
    print(f"    {status}")

print("\n💡 总结：removeprefix 简化协议识别和转换")

