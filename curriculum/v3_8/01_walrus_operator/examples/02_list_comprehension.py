"""
场景 2：列表推导式中复用计算结果

应用：数据转换后需要同时用于过滤和结果构造，避免重复计算
"""

import time

# 模拟一个计算密集的转换函数
def expensive_transform(x):
    """耗时的数据转换（模拟）"""
    time.sleep(0.01)  # 模拟 10ms 计算时间
    result = x ** 2 if x % 2 == 0 else None
    return result

# 测试数据
data = list(range(10))

print("=" * 50)
print("列表推导式中复用计算结果")
print("=" * 50)

# ❌ 传统方式 - transform 被调用两次！
print("\n[传统方式] 重复计算：")
start = time.time()
results_old = [expensive_transform(x) for x in data 
               if expensive_transform(x) is not None]
elapsed_old = time.time() - start
print(f"结果: {results_old}")
print(f"耗时: {elapsed_old:.3f}s")

# ✅ 使用 walrus operator - transform 只调用一次
print("\n[Walrus Operator] 复用结果：")
start = time.time()
results_new = [y for x in data 
               if (y := expensive_transform(x)) is not None]
elapsed_new = time.time() - start
print(f"结果: {results_new}")
print(f"耗时: {elapsed_new:.3f}s")

# 性能对比
speedup = elapsed_old / elapsed_new
print(f"\n💡 性能提升: {speedup:.1f}x (快了 {(speedup-1)*100:.0f}%)")
print(f"   传统方式: {elapsed_old:.3f}s")
print(f"   Walrus:   {elapsed_new:.3f}s")

