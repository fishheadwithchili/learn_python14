"""
场景 3：批量字典更新

应用：需要同时更新多个字段，使用 |= 替代多次赋值或 update()
"""

from datetime import datetime

# 模拟用户资料
user_profile = {
    "id": 12345,
    "username": "alice",
    "email": "alice@example.com",
    "created_at": "2023-01-01",
    "version": 1,
    "status": "active"
}

print("=" * 60)
print("场景 3：批量字典更新")
print("=" * 60)

print(f"\n[原始用户资料]")
for key, value in user_profile.items():
    print(f"  {key}: {value}")

# ❌ 传统方式 1：多次赋值
print("\n[传统方式 1] 多次赋值：")
user_profile_copy1 = user_profile.copy()
user_profile_copy1["updated_at"] = datetime.now().isoformat()
user_profile_copy1["version"] = user_profile_copy1["version"] + 1
user_profile_copy1["status"] = "verified"
print("  代码：")
print('    user_profile["updated_at"] = datetime.now().isoformat()')
print('    user_profile["version"] = user_profile["version"] + 1')
print('    user_profile["status"] = "verified"')

# ❌ 传统方式 2：使用 update()
print("\n[传统方式 2] 使用 update()：")
user_profile_copy2 = user_profile.copy()
user_profile_copy2.update({
    "updated_at": datetime.now().isoformat(),
    "version": user_profile_copy2["version"] + 1,
    "status": "verified"
})
print("  代码：")
print("    user_profile.update({")
print('        "updated_at": datetime.now().isoformat(),')
print('        "version": user_profile["version"] + 1,')
print('        "status": "verified"')
print("    })")

# ✅ 使用 Python 3.9+ 的 |= 运算符
print("\n[Python 3.9+] 使用 |= 运算符：")
user_profile_new = user_profile.copy()
user_profile_new |= {
    "updated_at": datetime.now().isoformat(),
    "version": user_profile_new["version"] + 1,
    "status": "verified"
}
print("  代码：")
print("    user_profile |= {")
print('        "updated_at": datetime.now().isoformat(),')
print('        "version": user_profile["version"] + 1,')
print('        "status": "verified"')
print("    }")

print(f"\n[更新后的用户资料]")
for key, value in user_profile_new.items():
    print(f"  {key}: {value}")

print("\n💡 总结：|= 运算符语法简洁，所有更新字段集中在一个字典中")

