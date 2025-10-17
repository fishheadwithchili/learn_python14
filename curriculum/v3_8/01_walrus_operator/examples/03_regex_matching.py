"""
场景 3：正则匹配后直接使用结果

应用：正则匹配成功后需要提取分组内容，避免二次匹配
"""

import re

# 测试数据：包含各种格式的文本
texts = [
    "订单号：ORD-12345，金额：1500元",
    "普通文本，没有订单信息",
    "订单号：ORD-67890，金额：2800元",
    "另一段无关文本",
]

# 正则表达式：匹配订单号和金额
pattern = r'订单号：(ORD-\d+)，金额：(\d+)元'

print("=" * 60)
print("正则匹配后直接使用结果")
print("=" * 60)

# ❌ 传统方式 - 需要两次匹配
print("\n[传统方式] 两次匹配：\n")
for text in texts:
    if re.search(pattern, text):  # 第一次匹配
        match = re.search(pattern, text)  # 第二次匹配！
        order_id = match.group(1)
        amount = match.group(2)
        print(f"  订单: {order_id}, 金额: {amount}元")

# ✅ 使用 walrus operator - 只匹配一次
print("\n[Walrus Operator] 一次匹配：\n")
for text in texts:
    if (match := re.search(pattern, text)):  # 匹配并赋值
        order_id = match.group(1)
        amount = match.group(2)
        print(f"  订单: {order_id}, 金额: {amount}元")

print("\n" + "=" * 60)
print("更复杂的示例：提取多个字段")
print("=" * 60)

# 更复杂的文本解析
log_line = "2024-01-15 10:30:45 [ERROR] Database connection failed: timeout after 30s"
log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'

if (m := re.search(log_pattern, log_line)):
    timestamp = m.group(1)
    level = m.group(2)
    message = m.group(3)
    
    print(f"\n解析结果:")
    print(f"  时间: {timestamp}")
    print(f"  级别: {level}")
    print(f"  消息: {message}")

print("\n💡 总结：避免重复正则匹配，提升性能和可读性")

