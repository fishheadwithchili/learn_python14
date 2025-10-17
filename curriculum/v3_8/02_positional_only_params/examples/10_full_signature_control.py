"""
场景 10: 完整的参数分层设计

应用：结合 /, * 设计清晰的函数签名
"""

print("=" * 60)
print("完整的参数分层")
print("=" * 60)

def process_data(
    data,           # 仅位置：核心数据
    /,
    format='json',  # 位置或关键字：常用参数
    encoding='utf-8',
    *,              # 以下仅关键字
    validate=True,  # 仅关键字：可选配置
    strict=False,
    timeout=30
):
    """
    处理数据（完整的参数分层示例）
    
    参数层次：
        data: 仅位置（核心）
        format, encoding: 位置或关键字（常用）
        validate, strict, timeout: 仅关键字（可选配置）
    """
    print(f"  处理数据:")
    print(f"    数据: {data[:50]}..." if len(data) > 50 else f"    数据: {data}")
    print(f"    格式: {format}")
    print(f"    编码: {encoding}")
    print(f"    验证: {validate}")
    print(f"    严格模式: {strict}")
    print(f"    超时: {timeout}s")

print("\n各种调用方式：\n")

# 最简调用
print("[方式 1] 最简：")
process_data('{"name": "Alice"}')

print("\n[方式 2] 指定格式：")
process_data('{"name": "Bob"}', 'json')

print("\n[方式 3] 使用关键字：")
process_data('{"name": "Charlie"}', format='json', encoding='utf-8')

print("\n[方式 4] 完整配置：")
process_data(
    '{"name": "David"}',
    'json',
    'utf-8',
    validate=True,
    strict=True,
    timeout=60
)

print("\n" + "=" * 60)
print("Web 请求处理")
print("=" * 60)

def handle_request(
    method, url,    # 仅位置：核心请求参数
    /,
    headers=None,   # 位置或关键字
    params=None,
    *,              # 以下仅关键字
    timeout=30,     # 仅关键字：请求配置
    verify_ssl=True,
    follow_redirects=True,
    max_retries=3
):
    """
    处理 HTTP 请求
    
    参数层次：
        method, url: 仅位置（必需）
        headers, params: 位置或关键字（常用）
        timeout, verify_ssl等: 仅关键字（高级配置）
    """
    print(f"  {method} {url}")
    if headers:
        print(f"  Headers: {headers}")
    if params:
        print(f"  Params: {params}")
    print(f"  [配置] 超时:{timeout}s, SSL验证:{verify_ssl}, 重试:{max_retries}次")

print("\n发送请求：\n")

handle_request(
    'GET',
    'https://api.example.com/users',
    headers={'Authorization': 'Bearer token'},
    timeout=60,
    max_retries=5
)

print("\n" + "=" * 60)
print("数据库查询构建器")
print("=" * 60)

def query(
    table,          # 仅位置：表名
    /,
    columns=None,   # 位置或关键字
    where=None,
    *,              # 以下仅关键字
    order_by=None,  # 仅关键字：高级选项
    limit=None,
    offset=None,
    group_by=None
):
    """
    构建 SQL 查询
    
    参数层次：
        table: 仅位置（核心）
        columns, where: 位置或关键字（常用）
        order_by, limit等: 仅关键字（高级）
    """
    cols = ', '.join(columns) if columns else '*'
    sql = f"SELECT {cols} FROM {table}"
    
    if where:
        sql += f" WHERE {where}"
    if group_by:
        sql += f" GROUP BY {group_by}"
    if order_by:
        sql += f" ORDER BY {order_by}"
    if limit:
        sql += f" LIMIT {limit}"
    if offset:
        sql += f" OFFSET {offset}"
    
    print(f"  SQL: {sql}")
    return sql

print("\n查询示例：\n")

query('users')
print()

query('users', ['id', 'name'], 'age > 18')
print()

query(
    'orders',
    columns=['user_id', 'total'],
    where='status = "completed"',
    order_by='created_at DESC',
    limit=10
)

print("\n" + "=" * 60)
print("参数分层的优势")
print("=" * 60)

print("""
完整的参数分层设计：

    def func(核心, /, 常用, *, 高级):
        pass

优势：
✅ 核心参数（仅位置）：强制位置，避免冗余
✅ 常用参数（灵活）：可位置可关键字，使用方便
✅ 高级参数（仅关键字）：避免位置错乱，提高可读性

示例：
    process_data(data)                    # 简单
    process_data(data, 'xml')             # 常用
    process_data(data, validate=False)    # 高级
    process_data(
        data,
        format='json',
        validate=True,
        strict=True
    )  # 完整配置，清晰易读
""")

print("💡 总结：合理使用 / 和 * 设计清晰的函数签名，提升 API 可用性")

