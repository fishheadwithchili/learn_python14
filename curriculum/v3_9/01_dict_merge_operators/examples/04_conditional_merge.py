"""
场景 4：条件合并

应用：根据条件决定是否添加某些键值对到字典中
"""

# 测试数据
base_params = {
    "page": 1,
    "limit": 20,
    "sort": "created_at"
}

# 条件参数
authenticated = True
is_admin = False
has_filter = True

auth_token = "Bearer abc123xyz"
filter_query = {"category": "tech", "status": "published"}

print("=" * 60)
print("场景 4：条件合并")
print("=" * 60)

print(f"\n[基础参数] {base_params}")
print(f"[条件状态] authenticated={authenticated}, is_admin={is_admin}, has_filter={has_filter}")

# ❌ 传统方式：使用 if-else 分支
print("\n[传统方式] 使用 if-else 分支：\n")
params_old = base_params.copy()
if authenticated:
    params_old["auth"] = auth_token
if is_admin:
    params_old["include_hidden"] = True
if has_filter:
    params_old.update(filter_query)

print(f"结果: {params_old}")

# ✅ 使用 Python 3.9+ 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符条件合并：\n")
params_new = (
    base_params
    | ({"auth": auth_token} if authenticated else {})
    | ({"include_hidden": True} if is_admin else {})
    | (filter_query if has_filter else {})
)

print(f"结果: {params_new}")

# 验证结果一致
print(f"\n结果一致: {params_old == params_new}")

# 代码对比
print("\n[代码对比]")
print("传统方式需要 6 行：")
print("  params = base_params.copy()")
print("  if authenticated:")
print('      params["auth"] = auth_token')
print("  if is_admin:")
print('      params["include_hidden"] = True')
print("  # ...")
print()
print("新方式只需 5 行（且更声明式）：")
print("  params = (")
print("      base_params")
print('      | ({"auth": token} if authenticated else {})')
print('      | ({"include_hidden": True} if is_admin else {})')
print("      | (filter_query if has_filter else {})")
print("  )")

print("\n💡 总结：| 运算符配合条件表达式，实现简洁的条件合并")

