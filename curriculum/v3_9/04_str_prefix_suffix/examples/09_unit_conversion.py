"""
场景 9：单位转换

应用：从带单位的字符串中提取数值和单位，进行转换
"""

# 测试数据
measurements = [
    "100px",
    "50%",
    "2.5kg",
    "30sec",
    "1000ms",
    "5.5GB",
    "100cm",
    "72dpi"
]

css_values = [
    "width: 100px;",
    "height: 50%;",
    "margin: 2em;",
    "padding: 10rem;"
]

print("=" * 60)
print("场景 9：单位转换")
print("=" * 60)

# 示例 1：提取数值和单位
print("\n[示例 1] 提取数值和单位：\n")

units = ["px", "%", "kg", "sec", "ms", "GB", "MB", "KB", "cm", "m", "dpi"]

def parse_measurement(text):
    """解析带单位的测量值"""
    for unit in sorted(units, key=len, reverse=True):  # 长单位优先
        if text.endswith(unit):
            numeric_part = text.removesuffix(unit)
            try:
                value = float(numeric_part)
                return value, unit
            except ValueError:
                pass
    return None, None

print("解析结果:")
for measurement in measurements:
    value, unit = parse_measurement(measurement)
    if value is not None:
        print(f"  {measurement} → 数值: {value}, 单位: {unit}")
    else:
        print(f"  {measurement} → 无法解析")

# 示例 2：单位转换
print("\n[示例 2] 单位转换：\n")

# 时间单位转换为秒
time_values = ["30sec", "1000ms", "2min", "1.5h"]

def convert_to_seconds(time_str):
    """转换为秒"""
    conversions = {
        "ms": 0.001,
        "sec": 1,
        "min": 60,
        "h": 3600
    }
    
    for unit, factor in conversions.items():
        if time_str.endswith(unit):
            numeric = time_str.removesuffix(unit)
            try:
                return float(numeric) * factor
            except ValueError:
                return None
    return None

print("转换为秒:")
for time_val in time_values:
    seconds = convert_to_seconds(time_val)
    if seconds is not None:
        print(f"  {time_val} = {seconds} 秒")

# 示例 3：存储单位转换
print("\n[示例 3] 存储单位转换：\n")

storage_values = ["5.5GB", "100MB", "512KB"]

def convert_to_bytes(storage_str):
    """转换为字节"""
    conversions = {
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4
    }
    
    for unit, factor in conversions.items():
        if storage_str.endswith(unit):
            numeric = storage_str.removesuffix(unit)
            try:
                return float(numeric) * factor
            except ValueError:
                return None
    return None

print("转换为字节:")
for storage in storage_values:
    bytes_val = convert_to_bytes(storage)
    if bytes_val is not None:
        print(f"  {storage} = {bytes_val:,.0f} 字节")

# 示例 4：CSS 单位处理
print("\n[示例 4] CSS 单位处理：\n")

css_units = ["px", "%", "em", "rem", "vw", "vh"]

def parse_css_value(css_property):
    """解析 CSS 属性值"""
    # 移除分号和空格
    value_part = css_property.split(":", 1)[1].strip().removesuffix(";")
    
    for unit in css_units:
        if value_part.endswith(unit):
            numeric = value_part.removesuffix(unit)
            try:
                return float(numeric), unit
            except ValueError:
                pass
    return None, None

print("解析 CSS 值:")
for css_val in css_values:
    prop_name = css_val.split(":")[0].strip()
    value, unit = parse_css_value(css_val)
    if value is not None:
        print(f"  {prop_name}: {value}{unit}")

# 示例 5：长度单位转换
print("\n[示例 5] 长度单位转换：\n")

lengths = ["100cm", "2m", "500mm"]

def convert_to_meters(length_str):
    """转换为米"""
    conversions = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }
    
    for unit, factor in conversions.items():
        if length_str.endswith(unit):
            numeric = length_str.removesuffix(unit)
            try:
                return float(numeric) * factor
            except ValueError:
                return None
    return None

print("转换为米:")
for length in lengths:
    meters = convert_to_meters(length)
    if meters is not None:
        print(f"  {length} = {meters} 米")

# 示例 6：温度单位识别
print("\n[示例 6] 温度单位识别：\n")

temperatures = ["25°C", "77°F", "298K"]

def parse_temperature(temp_str):
    """解析温度值"""
    units = ["°C", "°F", "K"]
    
    for unit in units:
        if temp_str.endswith(unit):
            numeric = temp_str.removesuffix(unit)
            try:
                return float(numeric), unit
            except ValueError:
                pass
    return None, None

print("温度解析:")
for temp in temperatures:
    value, unit = parse_temperature(temp)
    if value is not None:
        print(f"  {temp} → {value} {unit}")

# 示例 7：货币单位处理
print("\n[示例 7] 货币单位处理：\n")

prices_with_currency = ["$99.99", "€50.00", "¥100"]

# 注意：货币符号在前面，需要用 removeprefix
currency_symbols = ["$", "€", "¥", "£"]

def parse_price(price_str):
    """解析价格"""
    for symbol in currency_symbols:
        if price_str.startswith(symbol):
            numeric = price_str.removeprefix(symbol)
            try:
                return symbol, float(numeric)
            except ValueError:
                pass
    return None, None

print("价格解析:")
for price in prices_with_currency:
    symbol, value = parse_price(price)
    if value is not None:
        print(f"  {price} → 货币: {symbol}, 金额: {value}")

# 示例 8：百分比计算
print("\n[示例 8] 百分比值处理：\n")

percentages = ["50%", "75.5%", "100%"]

def parse_percentage(percent_str):
    """解析百分比为小数"""
    if percent_str.endswith("%"):
        numeric = percent_str.removesuffix("%")
        try:
            return float(numeric) / 100
        except ValueError:
            return None
    return None

print("百分比转小数:")
for percent in percentages:
    decimal = parse_percentage(percent)
    if decimal is not None:
        print(f"  {percent} = {decimal}")

print("\n💡 总结：removesuffix 简化单位提取和转换，代码更清晰")

