"""
场景 3：测试断言消息

应用：单元测试失败时提供详细上下文
"""

def calculate_discount(price, rate):
    """计算折扣"""
    return price * (1 - rate)

def validate_email(email):
    """验证邮箱"""
    return '@' in email and '.' in email

print("=" * 60)
print("测试断言消息")
print("=" * 60)

print("\n[测试 1] 折扣计算：\n")

price = 100
rate = 0.2
result = calculate_discount(price, rate)
expected = 80

assert (result := calculate_discount(price, rate)) == expected, \
    f"折扣计算错误：{price=}, {rate=}, {result=}, {expected=}"
print(f"  ✅ 测试通过: {result=}")

print("\n[测试 2] 邮箱验证：\n")

test_cases = [
    ("user@example.com", True),
    ("invalid.email", False),
    ("@example.com", False),
]

for email, should_pass in test_cases:
    result = validate_email(email)
    assert result == should_pass, \
        f"邮箱验证失败：{email=}, {result=}, {should_pass=}"
    status = "✅" if result else "❌"
    print(f"  {status} {email}: {result=}")

print("\n💡 总结：测试失败时自动显示所有相关变量值")

