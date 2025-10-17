"""
场景 1：基本用法

应用：创建带时区的 datetime 对象，进行基本的时区操作
"""

try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("错误: zoneinfo 需要 Python 3.9+")
    print("Windows 用户请安装: pip install tzdata")
    exit(1)

from datetime import datetime

print("=" * 60)
print("场景 1：zoneinfo 基本用法")
print("=" * 60)

# 示例 1：创建带时区的 datetime
print("\n[示例 1] 创建带时区的 datetime：\n")

# 方式 1：在创建时指定时区
dt_shanghai = datetime(2023, 6, 15, 14, 30, tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"上海时间: {dt_shanghai}")
print(f"  ISO 格式: {dt_shanghai.isoformat()}")

# 方式 2：获取当前时间（指定时区）
now_beijing = datetime.now(ZoneInfo("Asia/Shanghai"))
print(f"\n当前北京时间: {now_beijing}")
print(f"  格式化: {now_beijing.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# 示例 2：UTC 时间
print("\n[示例 2] UTC 时间：\n")

utc_time = datetime.now(ZoneInfo("UTC"))
print(f"当前 UTC 时间: {utc_time}")
print(f"  ISO 格式: {utc_time.isoformat()}")

# 与 timezone.utc 的对比
from datetime import timezone
utc_time_old = datetime.now(timezone.utc)
print(f"\ntimezone.utc: {utc_time_old}")
print(f"ZoneInfo('UTC'): {utc_time}")
print(f"结果相同: {utc_time.replace(microsecond=0) == utc_time_old.replace(microsecond=0)}")

# 示例 3：常见时区
print("\n[示例 3] 常见时区示例：\n")

timezones = [
    ("Asia/Shanghai", "中国上海"),
    ("America/New_York", "美国纽约"),
    ("Europe/London", "英国伦敦"),
    ("Asia/Tokyo", "日本东京"),
    ("Australia/Sydney", "澳大利亚悉尼")
]

base_time = datetime(2023, 6, 15, 12, 0)  # naive datetime

for tz_name, tz_desc in timezones:
    tz_time = base_time.replace(tzinfo=ZoneInfo(tz_name))
    print(f"{tz_desc:15s} ({tz_name:20s}): {tz_time.strftime('%H:%M %Z')}")

# 示例 4：时区信息
print("\n[示例 4] 时区对象信息：\n")

tz_shanghai = ZoneInfo("Asia/Shanghai")
print(f"时区名称: {tz_shanghai.key}")

# 创建时间并查看偏移量
dt = datetime(2023, 6, 15, 12, 0, tzinfo=tz_shanghai)
print(f"UTC 偏移: {dt.strftime('%z')}")  # +0800
print(f"时区缩写: {dt.strftime('%Z')}")  # CST

# 示例 5：naive vs aware datetime
print("\n[示例 5] naive vs aware datetime：\n")

# naive datetime（无时区）
dt_naive = datetime(2023, 6, 15, 12, 0)
print(f"Naive datetime: {dt_naive}")
print(f"  tzinfo: {dt_naive.tzinfo}")
print(f"  是 naive: {dt_naive.tzinfo is None}")

# aware datetime（有时区）
dt_aware = datetime(2023, 6, 15, 12, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"\nAware datetime: {dt_aware}")
print(f"  tzinfo: {dt_aware.tzinfo}")
print(f"  是 aware: {dt_aware.tzinfo is not None}")

# naive 转 aware
print("\n将 naive 转为 aware:")
dt_made_aware = dt_naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
print(f"  结果: {dt_made_aware}")

# 示例 6：时区列表（部分）
print("\n[示例 6] 部分可用时区：\n")

from zoneinfo import available_timezones

# 获取所有时区
all_timezones = sorted(available_timezones())

# 显示亚洲时区（前10个）
print("亚洲时区（部分）:")
asia_zones = [tz for tz in all_timezones if tz.startswith("Asia/")]
for tz in asia_zones[:10]:
    print(f"  - {tz}")

print(f"\n总共有 {len(all_timezones)} 个时区")

print("\n💡 总结：zoneinfo 提供标准库级别的时区支持，使用简单直观")

