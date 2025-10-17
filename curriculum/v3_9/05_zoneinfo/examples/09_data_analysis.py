"""
场景 9：数据分析时区处理

应用：处理带时区的时间序列数据，统一时区便于分析
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("需要 Python 3.9+ 或 pip install tzdata")
    exit(1)

from datetime import datetime, timedelta
from collections import defaultdict

print("=" * 60)
print("场景 9：数据分析时区处理")
print("=" * 60)

# 示例数据：全球服务器日志（不同时区）
server_logs = [
    {"server": "US-East", "timezone": "America/New_York", "timestamp": datetime(2023, 6, 15, 10, 0), "requests": 1250},
    {"server": "US-East", "timezone": "America/New_York", "timestamp": datetime(2023, 6, 15, 11, 0), "requests": 1580},
    {"server": "US-East", "timezone": "America/New_York", "timestamp": datetime(2023, 6, 15, 12, 0), "requests": 2100},
    {"server": "CN-East", "timezone": "Asia/Shanghai", "timestamp": datetime(2023, 6, 15, 22, 0), "requests": 3200},
    {"server": "CN-East", "timezone": "Asia/Shanghai", "timestamp": datetime(2023, 6, 15, 23, 0), "requests": 2800},
    {"server": "CN-East", "timezone": "Asia/Shanghai", "timestamp": datetime(2023, 6, 16, 0, 0), "requests": 1900},
    {"server": "EU-West", "timezone": "Europe/London", "timestamp": datetime(2023, 6, 15, 15, 0), "requests": 1750},
    {"server": "EU-West", "timezone": "Europe/London", "timestamp": datetime(2023, 6, 15, 16, 0), "requests": 1920},
    {"server": "EU-West", "timezone": "Europe/London", "timestamp": datetime(2023, 6, 15, 17, 0), "requests": 1680},
]

# ❌ 传统方式：直接使用本地时间（无法正确聚合）
print("\n[传统方式] 直接使用本地时间（不同时区无法对比）：\n")

print(f"{'服务器':<12} {'本地时间':<20} {'请求数':>8}")
print("-" * 45)
for log in server_logs[:6]:
    print(f"{log['server']:<12} "
          f"{log['timestamp'].strftime('%m-%d %H:%M'):<20} "
          f"{log['requests']:>8,}")

# ✅ 使用 zoneinfo：统一转换为 UTC 进行分析
print("\n[使用 zoneinfo] 转换为 UTC 统一分析：\n")

# 为每条日志添加 UTC 时间
for log in server_logs:
    # 将本地时间标记为带时区
    local_time = log['timestamp'].replace(tzinfo=ZoneInfo(log['timezone']))
    # 转换为 UTC
    log['utc_timestamp'] = local_time.astimezone(ZoneInfo("UTC"))

# 显示转换后的数据
print(f"{'服务器':<12} {'本地时间':<25} {'UTC时间':<20} {'请求数':>8}")
print("-" * 75)
for log in server_logs[:6]:
    local_tz = ZoneInfo(log['timezone'])
    local_time = log['timestamp'].replace(tzinfo=local_tz)
    
    print(f"{log['server']:<12} "
          f"{local_time.strftime('%m-%d %H:%M %Z'):<25} "
          f"{log['utc_timestamp'].strftime('%m-%d %H:%M %Z'):<20} "
          f"{log['requests']:>8,}")

# 示例 2：按小时聚合（UTC）
print("\n[示例 2] 按 UTC 小时聚合所有服务器请求：\n")

hourly_requests = defaultdict(int)

for log in server_logs:
    # 使用 UTC 时间的小时作为键
    hour_key = log['utc_timestamp'].strftime('%Y-%m-%d %H:00')
    hourly_requests[hour_key] += log['requests']

# 排序并显示
print(f"{'UTC 时间':<20} {'总请求数':>10}")
print("-" * 35)
for hour, count in sorted(hourly_requests.items()):
    print(f"{hour:<20} {count:>10,}")

# 示例 3：峰值时间分析（转换回各时区）
print("\n[示例 3] 各时区的峰值时间：\n")

def find_peak_hour(logs, timezone_name):
    """找出指定时区的峰值小时"""
    tz = ZoneInfo(timezone_name)
    hourly_stats = defaultdict(int)
    
    for log in logs:
        # 转换为目标时区
        local_time = log['utc_timestamp'].astimezone(tz)
        hour_key = local_time.hour
        hourly_stats[hour_key] += log['requests']
    
    # 找出峰值
    if hourly_stats:
        peak_hour = max(hourly_stats.items(), key=lambda x: x[1])
        return peak_hour
    return None, 0

timezones = {
    "America/New_York": "纽约",
    "Asia/Shanghai": "上海",
    "Europe/London": "伦敦"
}

for tz_name, city_name in timezones.items():
    peak_hour, peak_requests = find_peak_hour(server_logs, tz_name)
    print(f"{city_name} 时区峰值: {peak_hour:02d}:00 ({peak_requests:,} 请求)")

# 示例 4：时间序列对齐
print("\n[示例 4] 不同时区数据对齐到同一基准：\n")

# 创建一个 UTC 基准时间范围
start_utc = datetime(2023, 6, 15, 14, 0, tzinfo=ZoneInfo("UTC"))
time_points = [start_utc + timedelta(hours=i) for i in range(4)]

# 显示各时区的对应时间
print(f"{'UTC':<25} {'纽约':<25} {'上海':<25} {'伦敦':<25}")
print("-" * 105)

for utc_time in time_points:
    ny_time = utc_time.astimezone(ZoneInfo("America/New_York"))
    sh_time = utc_time.astimezone(ZoneInfo("Asia/Shanghai"))
    ld_time = utc_time.astimezone(ZoneInfo("Europe/London"))
    
    print(f"{utc_time.strftime('%m-%d %H:%M %Z'):<25} "
          f"{ny_time.strftime('%m-%d %H:%M %Z'):<25} "
          f"{sh_time.strftime('%m-%d %H:%M %Z'):<25} "
          f"{ld_time.strftime('%m-%d %H:%M %Z'):<25}")

# 示例 5：数据导出（保留时区信息）
print("\n[示例 5] 导出数据（ISO 8601 格式）：\n")

# 准备导出数据
export_data = []
for log in server_logs[:3]:
    export_data.append({
        'server': log['server'],
        'timestamp_iso': log['utc_timestamp'].isoformat(),  # ISO 8601 格式
        'requests': log['requests']
    })

import json
print("JSON 导出示例：")
print(json.dumps(export_data, indent=2))

# 示例 6：跨天统计（不同时区的"天"不同）
print("\n[示例 6] 按日期聚合（考虑时区）：\n")

def aggregate_by_date(logs, timezone_name):
    """按指定时区的日期聚合"""
    tz = ZoneInfo(timezone_name)
    daily_stats = defaultdict(int)
    
    for log in logs:
        local_time = log['utc_timestamp'].astimezone(tz)
        date_key = local_time.strftime('%Y-%m-%d')
        daily_stats[date_key] += log['requests']
    
    return daily_stats

# 分别按不同时区统计
for tz_name, city_name in timezones.items():
    daily = aggregate_by_date(server_logs, tz_name)
    print(f"{city_name} 时区的日统计:")
    for date, count in sorted(daily.items()):
        print(f"  {date}: {count:,} 请求")
    print()

print("💡 总结：统一转换为 UTC 进行分析，按需转换回本地时区展示")

