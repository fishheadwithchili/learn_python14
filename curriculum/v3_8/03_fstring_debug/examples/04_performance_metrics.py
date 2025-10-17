"""
场景 4：性能分析输出

应用：记录关键性能指标
"""

import time

print("=" * 60)
print("性能指标记录")
print("=" * 60)

def process_dataset(data, chunk_size):
    """模拟数据处理"""
    time.sleep(0.1)  # 模拟处理时间
    return len(data) // chunk_size

print("\n处理数据集：\n")

dataset_size = 10000
chunk_size = 100

start = time.time()
chunks_processed = process_dataset(range(dataset_size), chunk_size)
elapsed = time.time() - start

# 性能指标
items_per_sec = dataset_size / elapsed
print(f"{dataset_size=}")
print(f"{chunk_size=}")
print(f"{chunks_processed=}")
print(f"{elapsed=:.3f}s")
print(f"{items_per_sec=:.1f} items/s")

# 内存使用（模拟）
memory_mb = dataset_size * 8 / 1024 / 1024
print(f"{memory_mb=:.2f} MB")

print("\n💡 总结：性能指标一目了然，格式统一")

