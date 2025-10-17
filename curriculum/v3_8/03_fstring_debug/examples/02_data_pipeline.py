"""
场景 2：数据处理管道追踪

应用：在数据转换的多个步骤中追踪中间结果
"""

print("=" * 60)
print("数据处理管道追踪")
print("=" * 60)

# 原始数据
raw_data = [10, -5, 20, 0, -3, 15, 8]
print(f"\n原始数据: {raw_data}")

print("\n处理步骤：\n")

# 步骤 1：过滤负数
filtered = [x for x in raw_data if x > 0]
print(f"{len(filtered)=}, {filtered=}")

# 步骤 2：归一化
max_val = max(filtered)
normalized = [x / max_val for x in filtered]
print(f"{max_val=}, {normalized=}")

# 步骤 3：计算统计量
avg = sum(normalized) / len(normalized)
print(f"{avg=:.3f}")

# 步骤 4：标准化
std = (sum((x - avg) ** 2 for x in normalized) / len(normalized)) ** 0.5
print(f"{std=:.3f}")

print("\n💡 总结：清晰展示每个处理步骤的输出，便于调试")

