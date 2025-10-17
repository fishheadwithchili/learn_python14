"""
场景 6：多数据源聚合

应用：从多个数据源（数据库、缓存、API）收集数据，按优先级合并
"""

# 模拟不同数据源
def fetch_from_database():
    """数据库：权威数据源，但可能缺少实时信息"""
    return {
        "user_id": 12345,
        "username": "alice",
        "email": "alice@example.com",
        "created_at": "2023-01-01"
    }

def fetch_from_cache():
    """缓存：包含最近更新，但可能不完整"""
    return {
        "username": "alice_updated",  # 用户改名了
        "last_login": "2023-06-15"
    }

def fetch_from_api():
    """外部 API：提供补充信息"""
    return {
        "avatar_url": "https://cdn.example.com/avatars/12345.jpg",
        "bio": "Python developer"
    }

print("=" * 60)
print("场景 6：多数据源聚合")
print("=" * 60)

# 模拟数据获取
print("\n[数据获取]")
db_data = fetch_from_database()
cache_data = fetch_from_cache()
api_data = fetch_from_api()

print(f"数据库数据: {db_data}")
print(f"缓存数据:   {cache_data}")
print(f"API 数据:   {api_data}")

# ❌ 传统方式：逐个 update
print("\n[传统方式] 逐个 update()：\n")
aggregated_old = {}
aggregated_old.update(db_data)
aggregated_old.update(cache_data)
aggregated_old.update(api_data)
print(f"聚合结果: {aggregated_old}")

# ✅ 使用 Python 3.9+ 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符链式合并：\n")
aggregated_new = db_data | cache_data | api_data
print(f"聚合结果: {aggregated_new}")

# 验证结果一致
print(f"\n结果一致: {aggregated_old == aggregated_new}")

# 优先级说明
print("\n[优先级说明]")
print(f"  username 来源:")
print(f"    - 数据库: {db_data.get('username')}")
print(f"    - 缓存:   {cache_data.get('username')}")
print(f"    → 最终:   {aggregated_new['username']} (缓存优先级更高)")

# 不同优先级策略
print("\n[调整优先级示例]")

# 策略 1：API 优先级最高
api_first = api_data | cache_data | db_data
print(f"API 优先: {api_first.get('username', 'N/A')}")

# 策略 2：数据库优先级最高（只用缓存补充）
db_first = cache_data | api_data | db_data
print(f"数据库优先: {db_first.get('username', 'N/A')}")

# 代码对比
print("\n[代码对比]")
print("传统方式需要 4 行：")
print("  result = {}")
print("  result.update(db_data)")
print("  result.update(cache_data)")
print("  result.update(api_data)")
print()
print("新方式只需 1 行：")
print("  result = db_data | cache_data | api_data")

print("\n💡 总结：| 运算符清晰表达数据来源优先级，代码简洁")

