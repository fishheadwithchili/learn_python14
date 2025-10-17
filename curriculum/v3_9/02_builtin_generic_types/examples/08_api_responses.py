"""
场景 8：API 响应类型

应用：定义 API 返回的数据结构，确保数据格式的一致性
"""

from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T')

# ✅ Python 3.9+ 方式：使用内置泛型

@dataclass
class APIResponse:
    """通用 API 响应"""
    success: bool
    message: str
    data: dict[str, str | int | list | dict] | list | None = None
    errors: list[str] | None = None


@dataclass
class PaginatedResponse:
    """分页响应"""
    items: list[dict[str, str | int]]
    total: int
    page: int
    page_size: int
    has_next: bool
    has_prev: bool
    
    def total_pages(self) -> int:
        """计算总页数"""
        return (self.total + self.page_size - 1) // self.page_size


@dataclass
class UserResponse:
    """用户信息响应"""
    id: int
    username: str
    email: str
    profile: dict[str, str]
    permissions: list[str]
    created_at: str


@dataclass
class SearchResult:
    """搜索结果"""
    query: str
    results: list[dict[str, str | int | float]]
    facets: dict[str, list[tuple[str, int]]]  # 分面统计
    total_hits: int
    search_time_ms: float


def create_success_response(data: dict | list | None = None) -> APIResponse:
    """创建成功响应"""
    return APIResponse(
        success=True,
        message="操作成功",
        data=data
    )


def create_error_response(message: str, errors: list[str] | None = None) -> APIResponse:
    """创建错误响应"""
    return APIResponse(
        success=False,
        message=message,
        errors=errors or []
    )


def fetch_users(page: int = 1, page_size: int = 10) -> PaginatedResponse:
    """获取用户列表（模拟）"""
    # 模拟数据
    all_users = [
        {"id": i, "name": f"User{i}", "age": 20 + i}
        for i in range(1, 26)
    ]
    
    start = (page - 1) * page_size
    end = start + page_size
    
    items = all_users[start:end]
    total = len(all_users)
    
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        has_next=end < total,
        has_prev=page > 1
    )


def search_products(query: str) -> SearchResult:
    """搜索产品（模拟）"""
    # 模拟搜索结果
    results = [
        {"id": 1, "name": "Python 编程", "category": "book", "price": 99.9, "score": 0.95},
        {"id": 2, "name": "Python 实战", "category": "book", "price": 79.9, "score": 0.88},
        {"id": 3, "name": "Python 笔记本", "category": "stationery", "price": 29.9, "score": 0.75}
    ]
    
    # 模拟分面统计
    facets = {
        "category": [("book", 2), ("stationery", 1)],
        "price_range": [("0-50", 1), ("50-100", 2)]
    }
    
    return SearchResult(
        query=query,
        results=results,
        facets=facets,
        total_hits=len(results),
        search_time_ms=15.3
    )


print("=" * 60)
print("场景 8：API 响应类型")
print("=" * 60)

# 示例 1：成功响应
print("\n[示例 1] 成功响应：\n")

user_data = {
    "id": 123,
    "username": "alice",
    "email": "alice@example.com"
}

response = create_success_response(user_data)
print(f"响应状态: {response.success}")
print(f"消息: {response.message}")
print(f"数据: {response.data}")

# 示例 2：错误响应
print("\n[示例 2] 错误响应：\n")

error_response = create_error_response(
    "验证失败",
    errors=["邮箱格式不正确", "密码长度不足"]
)

print(f"响应状态: {error_response.success}")
print(f"消息: {error_response.message}")
print(f"错误列表: {error_response.errors}")

# 示例 3：分页响应
print("\n[示例 3] 分页响应：\n")

# 获取第1页
page1 = fetch_users(page=1, page_size=10)
print(f"第 {page1.page} 页:")
print(f"  总记录数: {page1.total}")
print(f"  当前页记录数: {len(page1.items)}")
print(f"  总页数: {page1.total_pages()}")
print(f"  有下一页: {page1.has_next}")
print(f"  有上一页: {page1.has_prev}")

print(f"\n前3个用户:")
for user in page1.items[:3]:
    print(f"  - ID: {user['id']}, 姓名: {user['name']}, 年龄: {user['age']}")

# 获取第3页
page3 = fetch_users(page=3, page_size=10)
print(f"\n第 {page3.page} 页:")
print(f"  当前页记录数: {len(page3.items)}")
print(f"  有下一页: {page3.has_next}")
print(f"  有上一页: {page3.has_prev}")

# 示例 4：用户响应
print("\n[示例 4] 用户详细信息响应：\n")

user_detail = UserResponse(
    id=123,
    username="alice",
    email="alice@example.com",
    profile={
        "full_name": "Alice Wang",
        "bio": "Python developer",
        "location": "Beijing"
    },
    permissions=["read", "write", "admin"],
    created_at="2023-01-01T00:00:00Z"
)

print(f"用户ID: {user_detail.id}")
print(f"用户名: {user_detail.username}")
print(f"邮箱: {user_detail.email}")
print(f"个人资料: {user_detail.profile}")
print(f"权限: {user_detail.permissions}")

# 示例 5：搜索响应
print("\n[示例 5] 搜索响应：\n")

search_result = search_products("Python")

print(f"搜索关键词: {search_result.query}")
print(f"总匹配数: {search_result.total_hits}")
print(f"搜索耗时: {search_result.search_time_ms}ms")

print(f"\n搜索结果:")
for item in search_result.results:
    print(f"  - {item['name']} (分类: {item['category']}, 价格: ¥{item['price']})")

print(f"\n分面统计:")
for facet_name, counts in search_result.facets.items():
    print(f"  {facet_name}:")
    for value, count in counts:
        print(f"    - {value}: {count} 项")

# 示例 6：嵌套响应
print("\n[示例 6] 嵌套响应：\n")

complex_response = create_success_response({
    "user": user_data,
    "posts": [
        {"id": 1, "title": "第一篇文章", "views": 100},
        {"id": 2, "title": "第二篇文章", "views": 50}
    ],
    "stats": {
        "total_posts": 2,
        "total_views": 150
    }
})

print(f"响应成功: {complex_response.success}")

if complex_response.data:
    print(f"用户: {complex_response.data.get('user')}")
    print(f"文章数: {len(complex_response.data.get('posts', []))}")
    print(f"统计: {complex_response.data.get('stats')}")

print("\n[类型注解的优势]")
print("  ✅ API 契约清晰")
print("  ✅ 前后端类型一致")
print("  ✅ 自动生成 API 文档")
print("  ✅ 减少数据格式错误")

print("\n💡 总结：内置泛型让 API 响应类型定义简洁且安全")

