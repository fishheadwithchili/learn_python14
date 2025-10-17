"""
场景 1：函数签名类型注解

应用：为函数参数和返回值添加类型提示，提升代码可读性和 IDE 支持
"""

# Python 3.9+ 无需从 typing 导入 List, Dict 等

# ❌ Python 3.8 方式（需要导入）
print("=" * 60)
print("场景 1：函数签名类型注解")
print("=" * 60)

print("\n[Python 3.8 方式] 需要从 typing 导入：\n")
print("from typing import List, Dict, Tuple")
print()
print("def process_scores(scores: List[int]) -> Dict[str, float]:")
print("    return {")
print("        'average': sum(scores) / len(scores),")
print("        'max': float(max(scores)),")
print("        'min': float(min(scores))")
print("    }")

# ✅ Python 3.9+ 方式（直接使用内置类型）
print("\n[Python 3.9+ 方式] 直接使用内置类型：\n")

def process_scores(scores: list[int]) -> dict[str, float]:
    """计算分数统计信息"""
    return {
        'average': sum(scores) / len(scores),
        'max': float(max(scores)),
        'min': float(min(scores))
    }

def filter_by_threshold(
    data: dict[str, int],
    threshold: int
) -> list[tuple[str, int]]:
    """筛选超过阈值的项"""
    return [(k, v) for k, v in data.items() if v > threshold]

def group_by_category(
    items: list[dict[str, str | int]]
) -> dict[str, list[dict[str, str | int]]]:
    """按类别分组"""
    result: dict[str, list[dict[str, str | int]]] = {}
    for item in items:
        category = str(item.get('category', 'unknown'))
        result.setdefault(category, []).append(item)
    return result

# 测试数据
scores = [85, 92, 78, 95, 88]
print(f"分数列表: {scores}")

result = process_scores(scores)
print(f"统计结果: {result}")

print("\n[示例 2] 筛选数据：")
data = {"apple": 10, "banana": 5, "orange": 15, "grape": 8}
print(f"原始数据: {data}")

filtered = filter_by_threshold(data, 7)
print(f"筛选结果 (>7): {filtered}")

print("\n[示例 3] 分组数据：")
items = [
    {"name": "apple", "category": "fruit", "price": 10},
    {"name": "carrot", "category": "vegetable", "price": 5},
    {"name": "banana", "category": "fruit", "price": 8}
]
print(f"原始数据: {items}")

grouped = group_by_category(items)
print(f"分组结果:")
for category, group_items in grouped.items():
    print(f"  {category}: {len(group_items)} 项")

print("\n💡 总结：Python 3.9+ 无需导入 typing 模块，类型注解更简洁")

