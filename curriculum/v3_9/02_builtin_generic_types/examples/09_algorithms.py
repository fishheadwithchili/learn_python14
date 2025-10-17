"""
场景 9：算法实现

应用：实现算法时指定数据类型，确保类型安全
"""

# ✅ Python 3.9+ 方式：使用内置泛型

def binary_search(arr: list[int], target: int) -> int:
    """二分查找（返回索引，未找到返回 -1）"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    """合并两个有序列表"""
    result: list[int] = []
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    # 添加剩余元素
    result.extend(a[i:])
    result.extend(b[j:])
    
    return result


def quick_sort(arr: list[int]) -> list[int]:
    """快速排序"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def find_duplicates(arr: list[int]) -> set[int]:
    """查找重复元素"""
    seen: set[int] = set()
    duplicates: set[int] = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return duplicates


def group_anagrams(words: list[str]) -> dict[str, list[str]]:
    """分组字母异位词"""
    groups: dict[str, list[str]] = {}
    
    for word in words:
        # 使用排序后的字符串作为键
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    
    return groups


def longest_common_prefix(strings: list[str]) -> str:
    """查找最长公共前缀"""
    if not strings:
        return ""
    
    # 以第一个字符串为基准
    prefix = strings[0]
    
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


def build_frequency_map(items: list[str]) -> dict[str, int]:
    """构建频率映射"""
    freq: dict[str, int] = {}
    
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    
    return freq


def topological_sort(graph: dict[str, list[str]]) -> list[str] | None:
    """拓扑排序（返回排序结果，有环返回 None）"""
    # 计算入度
    in_degree: dict[str, int] = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    # 找到所有入度为0的节点
    queue: list[str] = [node for node, degree in in_degree.items() if degree == 0]
    result: list[str] = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        # 减少邻居节点的入度
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果所有节点都处理了，说明没有环
    return result if len(result) == len(in_degree) else None


print("=" * 60)
print("场景 9：算法实现")
print("=" * 60)

# 示例 1：二分查找
print("\n[示例 1] 二分查找：\n")

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

print(f"数组: {sorted_array}")
print(f"查找: {target}")

index = binary_search(sorted_array, target)
print(f"结果: 索引 {index} (值: {sorted_array[index] if index != -1 else 'N/A'})")

# 示例 2：合并有序列表
print("\n[示例 2] 合并有序列表：\n")

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print(f"列表1: {list1}")
print(f"列表2: {list2}")

merged = merge_sorted_lists(list1, list2)
print(f"合并结果: {merged}")

# 示例 3：快速排序
print("\n[示例 3] 快速排序：\n")

unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"原始数组: {unsorted}")

sorted_array = quick_sort(unsorted)
print(f"排序结果: {sorted_array}")

# 示例 4：查找重复元素
print("\n[示例 4] 查找重复元素：\n")

numbers = [1, 2, 3, 2, 4, 5, 3, 6]
print(f"数组: {numbers}")

duplicates = find_duplicates(numbers)
print(f"重复元素: {duplicates}")

# 示例 5：字母异位词分组
print("\n[示例 5] 字母异位词分组：\n")

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"单词列表: {words}")

anagram_groups = group_anagrams(words)
print(f"分组结果:")
for key, group in anagram_groups.items():
    print(f"  {group}")

# 示例 6：最长公共前缀
print("\n[示例 6] 最长公共前缀：\n")

strings = ["flower", "flow", "flight"]
print(f"字符串列表: {strings}")

common_prefix = longest_common_prefix(strings)
print(f"最长公共前缀: '{common_prefix}'")

# 示例 7：频率统计
print("\n[示例 7] 频率统计：\n")

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"水果列表: {fruits}")

freq_map = build_frequency_map(fruits)
print(f"频率统计:")
for fruit, count in freq_map.items():
    print(f"  {fruit}: {count}")

# 示例 8：拓扑排序
print("\n[示例 8] 拓扑排序（任务依赖）：\n")

# 任务依赖图：A依赖B和C，B依赖D，C依赖D
task_graph: dict[str, list[str]] = {
    "D": [],
    "B": ["D"],
    "C": ["D"],
    "A": ["B", "C"]
}

print("任务依赖:")
for task, deps in task_graph.items():
    if deps:
        print(f"  {task} 依赖: {deps}")
    else:
        print(f"  {task} 无依赖")

sorted_tasks = topological_sort(task_graph)
print(f"\n执行顺序: {sorted_tasks}")

# 检测环
cyclic_graph: dict[str, list[str]] = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print("\n检测环形依赖:")
result = topological_sort(cyclic_graph)
print(f"结果: {'存在环形依赖' if result is None else '无环'}")

print("\n[类型注解的优势]")
print("  ✅ 算法输入输出类型明确")
print("  ✅ 减少类型错误")
print("  ✅ IDE 自动补全准确")
print("  ✅ 代码可读性更高")

print("\n💡 总结：内置泛型让算法实现更安全、更清晰")

