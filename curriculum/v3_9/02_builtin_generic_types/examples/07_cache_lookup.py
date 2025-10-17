"""
场景 7：缓存和查找表

应用：定义缓存数据结构的类型，提升数据访问效率
"""

from datetime import datetime, timedelta
from typing import TypeVar

T = TypeVar('T')

# ✅ Python 3.9+ 方式：使用内置泛型

class LRUCache:
    """LRU 缓存"""
    
    _cache: dict[str, tuple[float, str]]  # key -> (timestamp, value)
    _access_order: list[str]  # 访问顺序
    max_size: int
    
    def __init__(self, max_size: int = 100):
        self._cache = {}
        self._access_order = []
        self.max_size = max_size
    
    def get(self, key: str) -> str | None:
        """获取缓存值"""
        if key in self._cache:
            # 更新访问顺序
            self._access_order.remove(key)
            self._access_order.append(key)
            return self._cache[key][1]
        return None
    
    def put(self, key: str, value: str) -> None:
        """设置缓存值"""
        # 如果缓存满了，移除最旧的项
        if len(self._cache) >= self.max_size and key not in self._cache:
            oldest = self._access_order.pop(0)
            del self._cache[oldest]
        
        # 更新缓存
        self._cache[key] = (datetime.now().timestamp(), value)
        
        # 更新访问顺序
        if key in self._access_order:
            self._access_order.remove(key)
        self._access_order.append(key)
    
    def size(self) -> int:
        """缓存大小"""
        return len(self._cache)


class TTLCache:
    """带过期时间的缓存"""
    
    _cache: dict[str, tuple[datetime, str]]  # key -> (expiry_time, value)
    _default_ttl: int  # 默认TTL（秒）
    
    def __init__(self, default_ttl: int = 300):
        self._cache = {}
        self._default_ttl = default_ttl
    
    def get(self, key: str) -> str | None:
        """获取缓存值（自动清理过期项）"""
        if key in self._cache:
            expiry, value = self._cache[key]
            if datetime.now() < expiry:
                return value
            else:
                # 过期，删除
                del self._cache[key]
        return None
    
    def put(self, key: str, value: str, ttl: int | None = None) -> None:
        """设置缓存值"""
        ttl_seconds = ttl if ttl is not None else self._default_ttl
        expiry = datetime.now() + timedelta(seconds=ttl_seconds)
        self._cache[key] = (expiry, value)
    
    def cleanup(self) -> int:
        """清理过期项，返回清理数量"""
        now = datetime.now()
        expired_keys = [
            key for key, (expiry, _) in self._cache.items()
            if now >= expiry
        ]
        for key in expired_keys:
            del self._cache[key]
        return len(expired_keys)


class IndexedData:
    """带多索引的数据存储"""
    
    _data: dict[int, dict[str, str | int]]  # id -> record
    _email_index: dict[str, int]  # email -> id
    _name_index: dict[str, list[int]]  # name -> [ids]
    
    def __init__(self):
        self._data = {}
        self._email_index = {}
        self._name_index = {}
    
    def add(self, record: dict[str, str | int]) -> None:
        """添加记录（自动创建索引）"""
        record_id = int(record["id"])
        self._data[record_id] = record
        
        # 更新索引
        email = str(record.get("email", ""))
        if email:
            self._email_index[email] = record_id
        
        name = str(record.get("name", ""))
        if name:
            self._name_index.setdefault(name, []).append(record_id)
    
    def get_by_id(self, record_id: int) -> dict[str, str | int] | None:
        """通过ID查询"""
        return self._data.get(record_id)
    
    def get_by_email(self, email: str) -> dict[str, str | int] | None:
        """通过邮箱查询"""
        record_id = self._email_index.get(email)
        return self._data.get(record_id) if record_id else None
    
    def get_by_name(self, name: str) -> list[dict[str, str | int]]:
        """通过名字查询（可能有多个）"""
        ids = self._name_index.get(name, [])
        return [self._data[rid] for rid in ids if rid in self._data]


print("=" * 60)
print("场景 7：缓存和查找表")
print("=" * 60)

# 示例 1：LRU 缓存
print("\n[示例 1] LRU 缓存：\n")

lru = LRUCache(max_size=3)

# 添加缓存项
lru.put("user:1", "Alice")
lru.put("user:2", "Bob")
lru.put("user:3", "Charlie")

print(f"缓存大小: {lru.size()}")
print(f"获取 user:1: {lru.get('user:1')}")
print(f"获取 user:2: {lru.get('user:2')}")

# 添加第4项（会移除最旧的 user:3）
lru.put("user:4", "David")

print(f"\n添加 user:4 后:")
print(f"  user:3 (应该被移除): {lru.get('user:3')}")
print(f"  user:1 (仍然存在): {lru.get('user:1')}")
print(f"  user:4 (新添加): {lru.get('user:4')}")

# 示例 2：TTL 缓存
print("\n[示例 2] TTL 缓存：\n")

ttl_cache = TTLCache(default_ttl=2)  # 默认2秒过期

# 添加缓存项
ttl_cache.put("session:abc", "user_123", ttl=1)  # 1秒过期
ttl_cache.put("session:def", "user_456", ttl=10)  # 10秒过期

print(f"立即获取 session:abc: {ttl_cache.get('session:abc')}")
print(f"立即获取 session:def: {ttl_cache.get('session:def')}")

import time
print("\n等待2秒...")
time.sleep(2)

print(f"2秒后获取 session:abc (1秒TTL): {ttl_cache.get('session:abc')}")
print(f"2秒后获取 session:def (10秒TTL): {ttl_cache.get('session:def')}")

cleaned = ttl_cache.cleanup()
print(f"清理过期项: {cleaned} 项")

# 示例 3：多索引数据存储
print("\n[示例 3] 多索引数据存储：\n")

indexed_data = IndexedData()

# 添加数据
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25},
    {"id": 3, "name": "Alice", "email": "alice2@example.com", "age": 28}
]

for user in users:
    indexed_data.add(user)

print("添加了 3 个用户")

# 通过ID查询
print(f"\n通过 ID 查询 (id=1): {indexed_data.get_by_id(1)}")

# 通过邮箱查询
print(f"通过邮箱查询 (email=bob@example.com): {indexed_data.get_by_email('bob@example.com')}")

# 通过名字查询（可能有多个）
alice_users = indexed_data.get_by_name("Alice")
print(f"通过名字查询 (name=Alice): 找到 {len(alice_users)} 个用户")
for user in alice_users:
    print(f"  - ID: {user['id']}, Email: {user['email']}")

# 示例 4：组合使用缓存和索引
print("\n[示例 4] 缓存 + 索引组合使用：\n")

# 用 TTL 缓存存储查询结果
query_cache: dict[str, tuple[datetime, list[dict[str, str | int]]]] = {}

def cached_search_by_name(name: str) -> list[dict[str, str | int]]:
    """带缓存的名字查询"""
    cache_key = f"search:{name}"
    
    # 检查缓存
    if cache_key in query_cache:
        expiry, cached_result = query_cache[cache_key]
        if datetime.now() < expiry:
            print(f"  [缓存命中] {cache_key}")
            return cached_result
    
    # 缓存未命中，执行查询
    print(f"  [缓存未命中] {cache_key}")
    result = indexed_data.get_by_name(name)
    
    # 缓存结果（5秒过期）
    expiry = datetime.now() + timedelta(seconds=5)
    query_cache[cache_key] = (expiry, result)
    
    return result

# 第一次查询
print("第一次查询 Alice:")
result1 = cached_search_by_name("Alice")
print(f"  结果: {len(result1)} 个用户")

# 第二次查询（命中缓存）
print("\n第二次查询 Alice:")
result2 = cached_search_by_name("Alice")
print(f"  结果: {len(result2)} 个用户")

print("\n[类型注解的优势]")
print("  ✅ 缓存数据结构清晰")
print("  ✅ 索引类型明确")
print("  ✅ 防止类型错误")
print("  ✅ IDE 自动补全准确")

print("\n💡 总结：内置泛型让缓存和索引实现更安全、更高效")

