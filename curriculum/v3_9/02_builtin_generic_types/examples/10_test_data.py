"""
场景 10：测试数据类型

应用：定义测试数据的类型，确保测试数据的一致性和正确性
"""

from typing import TypeVar
from dataclasses import dataclass

T = TypeVar('T')

# ✅ Python 3.9+ 方式：使用内置泛型

@dataclass
class TestCase:
    """测试用例"""
    name: str
    input_data: dict[str, int | str | list]
    expected_output: dict[str, int | str] | list | str | int
    description: str = ""


@dataclass
class MockUser:
    """模拟用户数据"""
    id: int
    username: str
    email: str
    roles: list[str]
    metadata: dict[str, str]


# 测试数据集合
TEST_USERS: list[MockUser] = [
    MockUser(
        id=1,
        username="alice",
        email="alice@example.com",
        roles=["user", "admin"],
        metadata={"department": "engineering"}
    ),
    MockUser(
        id=2,
        username="bob",
        email="bob@example.com",
        roles=["user"],
        metadata={"department": "sales"}
    ),
    MockUser(
        id=3,
        username="charlie",
        email="charlie@example.com",
        roles=["user", "moderator"],
        metadata={"department": "support"}
    )
]

# API 测试用例
API_TEST_CASES: list[TestCase] = [
    TestCase(
        name="test_user_creation",
        input_data={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "secure123"
        },
        expected_output={"status": 201, "message": "User created"},
        description="测试用户创建"
    ),
    TestCase(
        name="test_invalid_email",
        input_data={
            "username": "testuser",
            "email": "invalid-email",
            "password": "pass123"
        },
        expected_output={"status": 400, "error": "Invalid email"},
        description="测试无效邮箱"
    ),
    TestCase(
        name="test_duplicate_username",
        input_data={
            "username": "alice",
            "email": "alice2@example.com",
            "password": "pass123"
        },
        expected_output={"status": 409, "error": "Username already exists"},
        description="测试用户名重复"
    )
]

# 数据验证测试
VALIDATION_TEST_CASES: list[dict[str, str | list[str] | bool]] = [
    {
        "input": "valid@email.com",
        "expected": True,
        "test_type": "email_validation"
    },
    {
        "input": "invalid-email",
        "expected": False,
        "test_type": "email_validation"
    },
    {
        "input": "short",
        "expected": False,
        "test_type": "password_strength",
        "errors": ["密码长度不足"]
    }
]


def run_test_case(test: TestCase) -> dict[str, bool | str]:
    """运行测试用例（模拟）"""
    print(f"  运行测试: {test.name}")
    print(f"    描述: {test.description}")
    print(f"    输入: {test.input_data}")
    print(f"    预期: {test.expected_output}")
    
    # 模拟测试结果
    return {
        "passed": True,
        "message": "测试通过"
    }


def get_user_by_role(role: str) -> list[MockUser]:
    """按角色筛选用户"""
    return [user for user in TEST_USERS if role in user.roles]


def group_users_by_department() -> dict[str, list[MockUser]]:
    """按部门分组用户"""
    result: dict[str, list[MockUser]] = {}
    
    for user in TEST_USERS:
        dept = user.metadata.get("department", "unknown")
        result.setdefault(dept, []).append(user)
    
    return result


print("=" * 60)
print("场景 10：测试数据类型")
print("=" * 60)

# 示例 1：测试用户数据
print("\n[示例 1] 测试用户数据：\n")

print(f"总测试用户数: {len(TEST_USERS)}")

for user in TEST_USERS:
    print(f"  - {user.username} (ID: {user.id})")
    print(f"    邮箱: {user.email}")
    print(f"    角色: {user.roles}")
    print(f"    部门: {user.metadata.get('department')}")

# 示例 2：按角色筛选
print("\n[示例 2] 按角色筛选用户：\n")

admin_users = get_user_by_role("admin")
print(f"管理员用户: {[u.username for u in admin_users]}")

moderator_users = get_user_by_role("moderator")
print(f"版主用户: {[u.username for u in moderator_users]}")

# 示例 3：按部门分组
print("\n[示例 3] 按部门分组用户：\n")

by_department = group_users_by_department()
for dept, users in by_department.items():
    print(f"{dept} 部门: {[u.username for u in users]}")

# 示例 4：运行 API 测试用例
print("\n[示例 4] 运行 API 测试用例：\n")

print(f"测试用例总数: {len(API_TEST_CASES)}\n")

passed_count = 0
for test_case in API_TEST_CASES:
    result = run_test_case(test_case)
    if result["passed"]:
        passed_count += 1
    print()

print(f"测试结果: {passed_count}/{len(API_TEST_CASES)} 通过")

# 示例 5：数据验证测试
print("\n[示例 5] 数据验证测试：\n")

print(f"验证测试用例: {len(VALIDATION_TEST_CASES)}\n")

for i, test in enumerate(VALIDATION_TEST_CASES, 1):
    print(f"测试 {i}:")
    print(f"  类型: {test['test_type']}")
    print(f"  输入: {test['input']}")
    print(f"  预期结果: {'✅ 通过' if test['expected'] else '❌ 失败'}")
    if "errors" in test:
        print(f"  预期错误: {test['errors']}")

# 示例 6：测试数据工厂
print("\n[示例 6] 测试数据工厂：\n")

def create_mock_users(count: int) -> list[MockUser]:
    """创建指定数量的模拟用户"""
    users: list[MockUser] = []
    
    for i in range(count):
        user = MockUser(
            id=1000 + i,
            username=f"test_user_{i}",
            email=f"test{i}@example.com",
            roles=["user"],
            metadata={"created_by": "test_factory"}
        )
        users.append(user)
    
    return users

mock_users = create_mock_users(5)
print(f"生成了 {len(mock_users)} 个模拟用户:")
for user in mock_users[:3]:
    print(f"  - {user.username} ({user.email})")
print("  ...")

# 示例 7：参数化测试数据
print("\n[示例 7] 参数化测试数据：\n")

# 边界值测试数据
BOUNDARY_TESTS: list[tuple[int, bool]] = [
    (-1, False),  # 负数
    (0, True),    # 零
    (1, True),    # 正数
    (100, True),  # 正常值
    (999, True),  # 边界值
    (1000, False) # 超出边界
]

print("边界值测试（0-999 有效）:")
for value, expected_valid in BOUNDARY_TESTS:
    status = "✅ 有效" if expected_valid else "❌ 无效"
    print(f"  值 {value:4d}: {status}")

# 示例 8：测试数据组合
print("\n[示例 8] 测试数据组合：\n")

# 组合测试矩阵
test_matrix: list[dict[str, str | bool]] = [
    {"browser": "chrome", "os": "windows", "mobile": False},
    {"browser": "firefox", "os": "linux", "mobile": False},
    {"browser": "safari", "os": "macos", "mobile": False},
    {"browser": "chrome", "os": "android", "mobile": True},
    {"browser": "safari", "os": "ios", "mobile": True}
]

print("跨平台测试矩阵:")
for i, config in enumerate(test_matrix, 1):
    device_type = "移动端" if config["mobile"] else "桌面端"
    print(f"  配置 {i}: {config['browser']} on {config['os']} ({device_type})")

print("\n[类型注解的优势]")
print("  ✅ 测试数据结构清晰")
print("  ✅ 确保测试数据一致性")
print("  ✅ IDE 自动补全测试数据字段")
print("  ✅ 减少测试数据错误")

print("\n💡 总结：内置泛型让测试数据定义更安全、更规范")

