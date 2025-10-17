"""
场景 5：覆盖特定键

应用：保持大部分键值不变，只覆盖少量键（不可变更新模式）
"""

# 原始记录
original_record = {
    "id": 101,
    "title": "Python 3.9 新特性",
    "author": "Alice",
    "status": "draft",
    "views": 0,
    "created_at": "2023-06-01",
    "updated_at": "2023-06-01"
}

print("=" * 60)
print("场景 5：覆盖特定键（不可变更新）")
print("=" * 60)

print("\n[原始记录]")
for key, value in original_record.items():
    print(f"  {key}: {value}")

# ❌ 传统方式：复制后修改
print("\n[传统方式] 复制字典后修改：\n")
published_record_old = original_record.copy()
published_record_old["status"] = "published"
published_record_old["updated_at"] = "2023-06-15"
print(f"发布后记录: {published_record_old}")
print(f"原始记录保持不变: {original_record['status']}")

# ✅ 使用 Python 3.9+ 的 | 运算符
print("\n[Python 3.9+] 使用 | 运算符覆盖：\n")
published_record_new = original_record | {
    "status": "published",
    "updated_at": "2023-06-15"
}
print(f"发布后记录: {published_record_new}")
print(f"原始记录保持不变: {original_record['status']}")

# 演示多种状态转换
print("\n[多种状态转换示例]")

# 归档
archived = original_record | {"status": "archived", "updated_at": "2023-12-01"}
print(f"归档状态: {archived['status']}")

# 增加浏览量
with_views = original_record | {"views": 1000}
print(f"浏览量更新: {with_views['views']}")

# 修改作者和标题
edited = original_record | {
    "title": "Python 3.9 完整指南",
    "author": "Bob",
    "updated_at": "2023-07-01"
}
print(f"编辑后标题: {edited['title']}")
print(f"编辑后作者: {edited['author']}")

# 验证原始记录未被修改
print("\n[验证不可变性]")
print(f"原始记录状态: {original_record['status']} (仍是 draft)")
print(f"原始记录标题: {original_record['title']} (未改变)")

# 代码对比
print("\n[代码对比]")
print("传统方式：")
print("  record = original.copy()")
print('  record["status"] = "published"')
print('  record["updated_at"] = "2023-06-15"')
print()
print("新方式：")
print('  record = original | {"status": "published", "updated_at": "2023-06-15"}')

print("\n💡 总结：| 运算符支持不可变更新模式，适合函数式编程风格")

