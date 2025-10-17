"""
场景 6：金融交易时间

应用：记录和显示金融市场交易的准确时区时间
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, time

print("=" * 60)
print("场景 6：金融交易时间")
print("=" * 60)

# 全球主要交易所时区
EXCHANGES = {
    "NYSE": ("America/New_York", "纽约证券交易所"),
    "LSE": ("Europe/London", "伦敦证券交易所"),
    "SSE": ("Asia/Shanghai", "上海证券交易所"),
    "TSE": ("Asia/Tokyo", "东京证券交易所"),
    "ASX": ("Australia/Sydney", "澳大利亚证券交易所")
}

# 示例 1：记录交易时间
print("\n[示例 1] 记录交易时间（带时区）：\n")

def record_trade(symbol, price, exchange_code):
    """记录交易（使用交易所本地时区）"""
    tz_name, exchange_name = EXCHANGES[exchange_code]
    trade_time = datetime.now(ZoneInfo(tz_name))
    
    return {
        "symbol": symbol,
        "price": price,
        "exchange": exchange_name,
        "local_time": trade_time,
        "utc_time": trade_time.astimezone(ZoneInfo("UTC"))
    }

# 记录几笔交易
trades = [
    record_trade("AAPL", 150.25, "NYSE"),
    record_trade("600000.SS", 10.52, "SSE"),
    record_trade("7203.T", 1850, "TSE")
]

for trade in trades:
    print(f"{trade['symbol']:12s} @ {trade['exchange']}")
    print(f"  本地时间: {trade['local_time'].strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"  UTC 时间: {trade['utc_time'].strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print()

# 示例 2：市场开盘时间
print("[示例 2] 各市场开盘时间（同一 UTC 时刻）：\n")

# 假设 UTC 时间为 2023-06-15 01:30（上海开盘时间）
utc_time = datetime(2023, 6, 15, 1, 30, tzinfo=ZoneInfo("UTC"))

print(f"UTC 基准时间: {utc_time.strftime('%Y-%m-%d %H:%M %Z')}\n")

for code, (tz_name, exchange_name) in EXCHANGES.items():
    local_time = utc_time.astimezone(ZoneInfo(tz_name))
    print(f"{exchange_name:20s}: {local_time.strftime('%H:%M %Z')}")

# 示例 3：交易窗口检查
print("\n[示例 3] 检查交易所是否开市：\n")

def is_market_open(exchange_code, check_time=None):
    """检查市场是否在交易时间内"""
    if check_time is None:
        check_time = datetime.now(ZoneInfo("UTC"))
    
    tz_name, _ = EXCHANGES[exchange_code]
    local_time = check_time.astimezone(ZoneInfo(tz_name))
    
    # 简化版：只检查工作日和时间（实际需要考虑节假日）
    weekday = local_time.weekday()
    hour = local_time.hour
    
    # 定义交易时间（示例）
    trading_hours = {
        "NYSE": (9, 16),   # 9:30-16:00（简化为整点）
        "SSE": (9, 15),    # 9:30-15:00
        "TSE": (9, 15),    # 9:00-15:00
        "LSE": (8, 16),    # 8:00-16:30
        "ASX": (10, 16)    # 10:00-16:00
    }
    
    if weekday >= 5:  # 周六周日
        return False
    
    start_hour, end_hour = trading_hours.get(exchange_code, (0, 24))
    return start_hour <= hour < end_hour

# 检查当前时间各市场状态
current_utc = datetime.now(ZoneInfo("UTC"))
print(f"检查时间: {current_utc.strftime('%Y-%m-%d %H:%M %Z')}\n")

for code, (tz_name, exchange_name) in EXCHANGES.items():
    local_time = current_utc.astimezone(ZoneInfo(tz_name))
    is_open = is_market_open(code, current_utc)
    status = "✅ 开市" if is_open else "❌ 休市"
    
    print(f"{exchange_name:20s}: {local_time.strftime('%H:%M %Z')} {status}")

# 示例 4：跨时区交易对账
print("\n[示例 4] 跨时区交易对账：\n")

# 纽约交易员的记录（纽约时间）
ny_record = datetime(2023, 6, 15, 10, 30, tzinfo=ZoneInfo("America/New_York"))
print(f"纽约记录: {ny_record.strftime('%Y-%m-%d %H:%M %Z')}")

# 上海交易员的记录（上海时间）
sh_record = datetime(2023, 6, 15, 22, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"上海记录: {sh_record.strftime('%Y-%m-%d %H:%M %Z')}")

# 转换到 UTC 对账
ny_utc = ny_record.astimezone(ZoneInfo("UTC"))
sh_utc = sh_record.astimezone(ZoneInfo("UTC"))

print(f"\nUTC 对账:")
print(f"  纽约: {ny_utc.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"  上海: {sh_utc.strftime('%Y-%m-%d %H:%M %Z')}")
print(f"  时间一致: {ny_utc == sh_utc}")

print("\n💡 总结：金融系统必须准确记录时区，避免交易时间歧义")

