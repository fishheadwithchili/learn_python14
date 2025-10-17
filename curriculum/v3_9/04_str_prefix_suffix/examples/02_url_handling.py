"""
场景 2：URL 路由处理

应用：从完整 URL 中提取路由路径、域名等信息
"""

# 测试数据
urls = [
    "https://api.example.com/v1/users/123",
    "https://api.example.com/v1/products",
    "http://localhost:8000/api/health",
    "https://www.example.com/blog/2023/python-tips"
]

print("=" * 60)
print("场景 2：URL 路由处理")
print("=" * 60)

# 示例 1：移除协议前缀
print("\n[示例 1] 移除协议前缀：\n")

print("传统方式:")
for url in urls:
    # 需要检查多种协议
    if url.startswith("https://"):
        domain_path = url[8:]  # len("https://") = 8
    elif url.startswith("http://"):
        domain_path = url[7:]  # len("http://") = 7
    else:
        domain_path = url
    print(f"  {url}")
    print(f"  → {domain_path}")

print("\nPython 3.9+ 方式:")
for url in urls:
    # 链式调用，优雅处理
    domain_path = url.removeprefix("https://").removeprefix("http://")
    print(f"  {url}")
    print(f"  → {domain_path}")

# 示例 2：提取路由路径
print("\n[示例 2] 提取 API 路由路径：\n")

api_base = "https://api.example.com"

api_urls = [
    "https://api.example.com/v1/users/123",
    "https://api.example.com/v1/products",
    "https://api.example.com/v2/orders"
]

print(f"API 基础 URL: {api_base}\n")

for url in api_urls:
    route = url.removeprefix(api_base)
    print(f"  完整 URL: {url}")
    print(f"  路由路径: {route}")

# 示例 3：移除版本前缀
print("\n[示例 3] 移除 API 版本前缀：\n")

versioned_routes = [
    "/v1/users",
    "/v1/products",
    "/v2/orders",
    "/v2/payments"
]

print("移除 /v1 前缀:")
for route in versioned_routes:
    clean_route = route.removeprefix("/v1")
    if clean_route != route:
        print(f"  {route} → {clean_route}")

print("\n移除所有版本前缀:")
for route in versioned_routes:
    # 移除多个可能的版本
    clean_route = route.removeprefix("/v1").removeprefix("/v2").removeprefix("/v3")
    print(f"  {route} → {clean_route}")

# 示例 4：查询参数处理
print("\n[示例 4] 移除查询参数：\n")

urls_with_params = [
    "https://example.com/search?q=python&page=1",
    "https://example.com/users?id=123",
    "https://example.com/products"
]

for url in urls_with_params:
    # 分离 URL 和查询参数
    if "?" in url:
        base_url = url.split("?")[0]
        query = url.split("?")[1]
        print(f"  URL: {url}")
        print(f"  基础: {base_url}")
        print(f"  参数: {query}")
    else:
        print(f"  URL: {url}")
        print(f"  无查询参数")

# 示例 5：移除尾部斜杠
print("\n[示例 5] 移除尾部斜杠：\n")

urls_with_slash = [
    "https://example.com/",
    "https://example.com/api/",
    "https://example.com/users",
    "https://example.com/products/"
]

print("规范化 URL（移除尾部斜杠）:")
for url in urls_with_slash:
    normalized = url.removesuffix("/")
    changed = " (已修改)" if normalized != url else ""
    print(f"  {url} → {normalized}{changed}")

# 示例 6：提取域名
print("\n[示例 6] 提取域名：\n")

def extract_domain(url):
    """提取域名（不含协议和路径）"""
    # 移除协议
    without_protocol = url.removeprefix("https://").removeprefix("http://")
    # 提取域名部分（在第一个斜杠之前）
    domain = without_protocol.split("/")[0]
    return domain

for url in urls:
    domain = extract_domain(url)
    print(f"  {url}")
    print(f"  域名: {domain}")

print("\n💡 总结：removeprefix/removesuffix 简化 URL 解析和处理")

