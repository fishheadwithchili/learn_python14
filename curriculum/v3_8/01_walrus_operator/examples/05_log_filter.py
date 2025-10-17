"""
场景 5：日志过滤与统计

应用：需要同时判断长度并记录长度值，避免重复计算
"""

# 模拟的日志数据
LOGS = [
    "INFO: Application started",
    "DEBUG: Loading configuration from /etc/app/config.yaml with extensive parameters and settings",
    "WARNING: Deprecated API usage detected",
    "ERROR: Database connection timeout after multiple retry attempts with exponential backoff strategy",
    "INFO: Request processed",
    "CRITICAL: Out of memory exception occurred during large dataset processing operation",
]

print("=" * 70)
print("日志过滤：找出超长日志行")
print("=" * 70)

THRESHOLD = 60  # 字符数阈值

# ❌ 传统方式 - len() 被调用多次
print("\n[传统方式] 重复计算长度：\n")
long_logs_old = []
for log in LOGS:
    if len(log) > THRESHOLD:  # 第一次调用 len()
        long_logs_old.append({
            'log': log[:50] + '...',
            'length': len(log)  # 第二次调用 len()！
        })

for item in long_logs_old:
    print(f"  长度 {item['length']:3d}: {item['log']}")

# ✅ 使用 walrus operator - len() 只调用一次
print("\n[Walrus Operator] 复用长度计算：\n")
long_logs_new = []
for log in LOGS:
    if (length := len(log)) > THRESHOLD:  # 计算并判断
        long_logs_new.append({
            'log': log[:50] + '...',
            'length': length  # 直接使用已计算的值
        })

for item in long_logs_new:
    print(f"  长度 {item['length']:3d}: {item['log']}")

print("\n" + "=" * 70)
print("高级用法：列表推导式中的过滤和统计")
print("=" * 70)

# 一行代码实现过滤 + 格式化
long_logs_compact = [
    f"[{n}字符] {log[:40]}..." 
    for log in LOGS 
    if (n := len(log)) > THRESHOLD
]

print("\n紧凑的列表推导式：\n")
for log in long_logs_compact:
    print(f"  {log}")

# 统计信息
print("\n" + "=" * 70)
print("统计信息")
print("=" * 70)

total_logs = len(LOGS)
long_logs_count = len(long_logs_new)
percentage = (long_logs_count / total_logs) * 100

print(f"\n总日志数: {total_logs}")
print(f"超长日志: {long_logs_count} ({percentage:.1f}%)")
print(f"阈值: {THRESHOLD} 字符")

print("\n💡 总结：在过滤条件中复用计算结果，代码更简洁高效")

