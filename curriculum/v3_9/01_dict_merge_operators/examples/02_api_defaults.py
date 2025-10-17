"""
场景 2：API 参数默认值设置

应用：函数接收可选参数字典，需要与默认值合并，避免可变默认参数陷阱
"""

DEFAULT_OPTIONS = {
    "method": "GET",
    "timeout": 30,
    "retry": 3,
    "verify_ssl": True,
    "headers": {}
}

def make_request_old(url, options=None):
    """传统方式：使用 update() 或解包"""
    # 不能用 options={} 作为默认值（可变默认参数陷阱）
    if options is None:
        options = {}
    
    # 方法 1: 使用 update()
    opts = DEFAULT_OPTIONS.copy()
    opts.update(options)
    return opts

def make_request_new(url, options=None):
    """Python 3.9+ 方式：使用 | 运算符"""
    opts = DEFAULT_OPTIONS | (options or {})
    return opts

print("=" * 60)
print("场景 2：API 参数默认值设置")
print("=" * 60)

# 测试用例 1：只提供部分参数
user_options_1 = {"method": "POST", "timeout": 60}

print("\n[测试 1] 用户只提供部分参数：")
print(f"  用户参数: {user_options_1}")

result_old = make_request_old("https://api.example.com", user_options_1)
result_new = make_request_new("https://api.example.com", user_options_1)

print(f"\n  传统方式结果: {result_old}")
print(f"  新方式结果:   {result_new}")
print(f"  结果一致: {result_old == result_new}")

# 测试用例 2：不提供参数（使用全部默认值）
print("\n[测试 2] 不提供参数（使用全部默认值）：")

result_old_2 = make_request_old("https://api.example.com")
result_new_2 = make_request_new("https://api.example.com")

print(f"  传统方式结果: {result_old_2}")
print(f"  新方式结果:   {result_new_2}")
print(f"  结果一致: {result_old_2 == result_new_2}")

# 代码对比
print("\n[代码对比]")
print("  传统方式：")
print("    opts = DEFAULT_OPTIONS.copy()")
print("    opts.update(options)")
print()
print("  新方式：")
print("    opts = DEFAULT_OPTIONS | (options or {})")

print("\n💡 总结：| 运算符让默认参数合并更简洁，一行完成")

