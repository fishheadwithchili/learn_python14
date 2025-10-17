"""
场景 4：数据清洗

应用：清理数据中的固定标记、ID前缀、单位后缀等
"""

# 测试数据
data_with_prefixes = [
    "ID:12345",
    "USER:alice",
    "ORDER:ORD-2023-001",
    "PRODUCT:SKU-ABC-123"
]

measurements = [
    "100px",
    "50%",
    "2.5kg",
    "30sec",
    "1000ms"
]

tagged_data = [
    "[URGENT] Server down",
    "[INFO] User logged in",
    "[ERROR] Connection failed",
    "Normal message"
]

print("=" * 60)
print("场景 4：数据清洗")
print("=" * 60)

# 示例 1：移除 ID 前缀
print("\n[示例 1] 移除 ID 前缀：\n")

print("传统方式:")
for data in data_with_prefixes:
    if ":" in data:
        prefix, value = data.split(":", 1)
        print(f"  {data} → 类型: {prefix}, 值: {value}")

print("\nPython 3.9+ 方式:")
for data in data_with_prefixes:
    # 直接移除已知前缀
    value = data.removeprefix("ID:").removeprefix("USER:").removeprefix("ORDER:").removeprefix("PRODUCT:")
    if value != data:
        print(f"  {data} → {value}")

# 示例 2：移除单位后缀
print("\n[示例 2] 提取数值（移除单位）：\n")

for measurement in measurements:
    # 移除常见单位
    numeric = (measurement
               .removesuffix("px")
               .removesuffix("%")
               .removesuffix("kg")
               .removesuffix("sec")
               .removesuffix("ms"))
    
    try:
        value = float(numeric)
        unit = measurement[len(numeric):]
        print(f"  {measurement} → 数值: {value}, 单位: {unit}")
    except ValueError:
        print(f"  {measurement} → 无法解析")

# 示例 3：移除标签前缀
print("\n[示例 3] 移除日志标签：\n")

tags = ["[URGENT]", "[INFO]", "[ERROR]", "[WARNING]"]

for data in tagged_data:
    message = data
    tag = None
    
    # 检测并移除标签
    for t in tags:
        if data.startswith(t):
            tag = t.strip("[]")
            message = data.removeprefix(t).strip()
            break
    
    if tag:
        print(f"  {data}")
        print(f"    标签: {tag}, 消息: {message}")
    else:
        print(f"  {data}")
        print(f"    (无标签)")

# 示例 4：清理 CSV 数据
print("\n[示例 4] CSV 数据清理：\n")

csv_data = [
    '"Alice"',
    '"Bob Smith"',
    ' "Charlie" ',
    'David'
]

print("移除引号和空格:")
for data in csv_data:
    cleaned = data.strip().removeprefix('"').removesuffix('"')
    print(f"  {repr(data)} → {cleaned}")

# 示例 5：移除 Markdown 标记
print("\n[示例 5] 移除 Markdown 标记：\n")

markdown_texts = [
    "**bold text**",
    "*italic text*",
    "`code`",
    "~~strikethrough~~",
    "normal text"
]

for text in markdown_texts:
    # 移除常见 Markdown 标记
    plain = (text
             .removeprefix("**").removesuffix("**")
             .removeprefix("*").removesuffix("*")
             .removeprefix("`").removesuffix("`")
             .removeprefix("~~").removesuffix("~~"))
    
    if plain != text:
        print(f"  {text} → {plain}")
    else:
        print(f"  {text} (无标记)")

# 示例 6：清理电话号码
print("\n[示例 6] 清理电话号码：\n")

phone_numbers = [
    "+86-138-0000-0000",
    "86-139-1111-1111",
    "010-12345678",
    "12345678"
]

print("移除国家代码和区号前缀:")
for phone in phone_numbers:
    # 移除国际前缀
    cleaned = phone.removeprefix("+86-").removeprefix("86-").removeprefix("010-")
    print(f"  {phone} → {cleaned}")

# 示例 7：清理 HTML 实体
print("\n[示例 7] 清理 HTML 编码：\n")

html_texts = [
    "&lt;div&gt;",
    "&amp;",
    "&quot;Hello&quot;",
    "Normal text"
]

# 简化版 HTML 解码（实际应用建议使用 html.unescape）
html_entities = {
    "&lt;": "<",
    "&gt;": ">",
    "&amp;": "&",
    "&quot;": '"'
}

for html_text in html_texts:
    decoded = html_text
    for entity, char in html_entities.items():
        decoded = decoded.replace(entity, char)
    
    if decoded != html_text:
        print(f"  {html_text} → {decoded}")
    else:
        print(f"  {html_text} (无实体)")

# 示例 8：移除货币符号
print("\n[示例 8] 提取货币数值：\n")

prices = [
    "$99.99",
    "€50.00",
    "¥100",
    "£25.50"
]

currency_symbols = ["$", "€", "¥", "£"]

for price in prices:
    numeric = price
    symbol = None
    
    for sym in currency_symbols:
        if price.startswith(sym):
            symbol = sym
            numeric = price.removeprefix(sym)
            break
    
    print(f"  {price} → 符号: {symbol}, 金额: {numeric}")

print("\n💡 总结：removeprefix/removesuffix 简化数据清洗，代码更清晰")

