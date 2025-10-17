"""
场景 8：测试数据构造

应用：基于基准数据创建多个测试用例的变体，避免重复定义
"""

# 基准测试数据
BASE_USER = {
    "role": "user",
    "status": "active",
    "email_verified": True,
    "created_at": "2023-01-01",
    "preferences": {
        "theme": "light",
        "notifications": True
    }
}

print("=" * 60)
print("场景 8：测试数据构造")
print("=" * 60)

print("\n[基准测试数据]")
for key, value in BASE_USER.items():
    print(f"  {key}: {value}")

# ❌ 传统方式：每个测试用例重复定义所有字段
print("\n[传统方式] 每个用例重复定义所有字段：\n")

test_cases_old = [
    # 测试用例 1：普通用户
    {
        "role": "user",
        "status": "active",
        "email_verified": True,
        "created_at": "2023-01-01",
        "preferences": {"theme": "light", "notifications": True},
        "username": "alice"
    },
    # 测试用例 2：管理员
    {
        "role": "admin",  # 只有这个不同
        "status": "active",
        "email_verified": True,
        "created_at": "2023-01-01",
        "preferences": {"theme": "light", "notifications": True},
        "username": "bob"
    },
    # ... 代码重复
]

print(f"传统方式创建了 {len(test_cases_old)} 个测试用例")
print(f"第一个用例: {test_cases_old[0]}")

# ✅ 使用 Python 3.9+ 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符创建变体：\n")

test_cases_new = [
    # 测试用例 1：普通用户
    BASE_USER | {"username": "alice", "id": 1},
    
    # 测试用例 2：管理员
    BASE_USER | {"username": "bob", "id": 2, "role": "admin"},
    
    # 测试用例 3：未验证邮箱的用户
    BASE_USER | {"username": "charlie", "id": 3, "email_verified": False},
    
    # 测试用例 4：停用的用户
    BASE_USER | {"username": "david", "id": 4, "status": "suspended"},
    
    # 测试用例 5：VIP 用户
    BASE_USER | {
        "username": "eve",
        "id": 5,
        "role": "vip",
        "preferences": {"theme": "dark", "notifications": True}
    }
]

print(f"新方式创建了 {len(test_cases_new)} 个测试用例\n")
for i, case in enumerate(test_cases_new, 1):
    print(f"测试用例 {i}: {case['username']} (role={case['role']}, status={case['status']})")

# 验证所有用例都包含基准字段
print("\n[验证基准字段存在]")
for i, case in enumerate(test_cases_new, 1):
    has_all_base = all(key in case for key in BASE_USER.keys())
    print(f"用例 {i} 包含所有基准字段: {has_all_base}")

# 参数化测试示例
print("\n[参数化测试示例]")

def validate_user(user):
    """简单的用户验证函数"""
    errors = []
    
    if user["role"] not in ["user", "admin", "vip"]:
        errors.append(f"无效角色: {user['role']}")
    
    if user["status"] not in ["active", "suspended"]:
        errors.append(f"无效状态: {user['status']}")
    
    return len(errors) == 0, errors

for i, test_case in enumerate(test_cases_new, 1):
    is_valid, errors = validate_user(test_case)
    status = "✅ 通过" if is_valid else f"❌ 失败: {errors}"
    print(f"  用例 {i} ({test_case['username']}): {status}")

# 代码对比
print("\n[代码对比]")
print("传统方式需要重复所有字段：")
print("  {")
print('      "role": "user",')
print('      "status": "active",')
print('      "email_verified": True,')
print("      # ... 所有字段")
print('      "username": "alice"')
print("  }")
print()
print("新方式只需指定差异：")
print('  BASE_USER | {"username": "alice", "id": 1}')

print("\n💡 总结：| 运算符让测试数据构造更简洁，突出用例差异")

