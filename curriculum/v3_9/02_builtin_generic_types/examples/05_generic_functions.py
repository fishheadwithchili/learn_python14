"""
场景 5：泛型函数

应用：编写支持多种类型的通用函数，保持类型安全
"""

from typing import TypeVar

# 定义类型变量
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# ✅ Python 3.9+ 方式：配合内置泛型

def first_or_none(items: list[T]) -> T | None:
    """获取列表第一个元素，如果为空则返回 None"""
    return items[0] if items else None


def last_or_default(items: list[T], default: T) -> T:
    """获取列表最后一个元素，如果为空则返回默认值"""
    return items[-1] if items else default


def group_by(items: list[T], key_func: callable) -> dict[str, list[T]]:
    """按指定键函数分组"""
    result: dict[str, list[T]] = {}
    for item in items:
        key = str(key_func(item))
        result.setdefault(key, []).append(item)
    return result


def merge_dicts(dict1: dict[K, V], dict2: dict[K, V]) -> dict[K, V]:
    """合并两个字典（Python 3.9+ 可以直接用 | 运算符）"""
    return dict1 | dict2


def chunk_list(items: list[T], size: int) -> list[list[T]]:
    """将列表分块"""
    return [items[i:i + size] for i in range(0, len(items), size)]


def flatten(nested: list[list[T]]) -> list[T]:
    """展平嵌套列表"""
    result: list[T] = []
    for sublist in nested:
        result.extend(sublist)
    return result


def zip_dicts(keys: list[K], values: list[V]) -> dict[K, V]:
    """将两个列表组合成字典"""
    return dict(zip(keys, values))


def safe_get(data: dict[K, V], key: K, default: V) -> V:
    """安全获取字典值"""
    return data.get(key, default)


print("=" * 60)
print("场景 5：泛型函数")
print("=" * 60)

# 示例 1：first_or_none
print("\n[示例 1] 获取第一个元素：\n")

numbers = [1, 2, 3, 4, 5]
empty_list: list[int] = []

print(f"列表: {numbers}")
print(f"第一个元素: {first_or_none(numbers)}")

print(f"\n空列表: {empty_list}")
print(f"第一个元素: {first_or_none(empty_list)}")

strings = ["hello", "world"]
print(f"\n字符串列表: {strings}")
print(f"第一个元素: {first_or_none(strings)}")

# 示例 2：last_or_default
print("\n[示例 2] 获取最后一个元素（带默认值）：\n")

print(f"列表: {numbers}")
print(f"最后一个元素: {last_or_default(numbers, 0)}")

print(f"\n空列表: {empty_list}")
print(f"最后一个元素（默认值0）: {last_or_default(empty_list, 0)}")

# 示例 3：group_by
print("\n[示例 3] 分组：\n")

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"}
]

by_grade = group_by(students, lambda s: s["grade"])
print(f"按成绩分组:")
for grade, group in by_grade.items():
    names = [s["name"] for s in group]
    print(f"  {grade}: {names}")

# 示例 4：chunk_list
print("\n[示例 4] 列表分块：\n")

items = list(range(1, 11))
print(f"原始列表: {items}")

chunked = chunk_list(items, 3)
print(f"分块（每组3个）: {chunked}")

# 示例 5：flatten
print("\n[示例 5] 展平嵌套列表：\n")

nested_list = [[1, 2], [3, 4], [5, 6, 7]]
print(f"嵌套列表: {nested_list}")

flattened = flatten(nested_list)
print(f"展平后: {flattened}")

# 示例 6：zip_dicts
print("\n[示例 6] 组合键值列表为字典：\n")

keys_list = ["name", "age", "city"]
values_list = ["Alice", 30, "Beijing"]

print(f"键列表: {keys_list}")
print(f"值列表: {values_list}")

result_dict = zip_dicts(keys_list, values_list)
print(f"组合结果: {result_dict}")

# 示例 7：类型安全演示
print("\n[示例 7] 类型安全演示：\n")

# IDE 和类型检查器可以推断出类型
int_result = first_or_none([1, 2, 3])  # 推断为 int | None
str_result = first_or_none(["a", "b"])  # 推断为 str | None

print(f"整数列表第一个元素: {int_result} (类型: {type(int_result).__name__})")
print(f"字符串列表第一个元素: {str_result} (类型: {type(str_result).__name__})")

# 示例 8：复杂泛型函数
print("\n[示例 8] 复杂泛型函数：\n")

def transform_values(
    data: dict[K, V],
    transformer: callable
) -> dict[K, V]:
    """转换字典的所有值"""
    return {k: transformer(v) for k, v in data.items()}

prices = {"apple": 10, "banana": 5, "orange": 8}
print(f"原始价格: {prices}")

# 价格加倍
doubled = transform_values(prices, lambda x: x * 2)
print(f"价格加倍: {doubled}")

print("\n[泛型函数的优势]")
print("  ✅ 代码复用性高")
print("  ✅ 类型安全")
print("  ✅ IDE 提供准确的类型提示")
print("  ✅ 减少类型转换错误")

print("\n💡 总结：泛型函数 + 内置泛型类型 = 类型安全的通用函数")

